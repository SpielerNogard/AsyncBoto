import pytest
import boto3
from async_boto.clients.dynamodb import AsyncDynamoDBClient
import os
import pytest
import boto3
import asyncio
from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    CreateTableRequest,
    DeleteTableRequest,
    DescribeTableRequest,
)


@pytest.fixture(scope="session")
async def dynamodb_client():
    if os.environ.get("mode", "local") == "local":
        # Mock AWS session
        session = boto3.Session(region_name="us-west-2")
        client = AsyncDynamoDBClient(
            aws_session=session, endpoint_url="http://localhost:4566"
        )
        yield client
        # Add any necessary cleanup here
    else:
        session = boto3.Session(profile_name=os.environ["mode"])
        client = AsyncDynamoDBClient(aws_session=session)
        yield client


@pytest.fixture()
async def test_table(dynamodb_client):
    table_name = "test-table-consistent"
    # Setup: create a table
    create_request = CreateTableRequest(
        TableName=table_name,
        KeySchema=[
            {"AttributeName": "hash", "KeyType": "HASH"},
            {"AttributeName": "sort", "KeyType": "RANGE"},
        ],
        BillingMode="PAY_PER_REQUEST",
        AttributeDefinitions=[
            {"AttributeName": "hash", "AttributeType": "S"},
            {"AttributeName": "sort", "AttributeType": "S"},
        ],
    )
    await dynamodb_client.create_table(create_request)

    # Wait until the table is active
    status = "CREATING"
    while status != "ACTIVE":
        await asyncio.sleep(1)
        response = await dynamodb_client.describe_table(
            DescribeTableRequest(TableName=table_name)
        )
        status = response.Table.TableStatus

    yield table_name

    # Teardown: delete the table
    await dynamodb_client.delete_table(DeleteTableRequest(TableName=table_name))
