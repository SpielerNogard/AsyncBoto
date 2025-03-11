import pytest
import boto3
from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    DeleteTableRequest,
    DescribeTableRequest,
)
from async_boto.validation.dynamodb.create_table import (
    CreateTableRequest,
    CreateTableResponse,
)
import asyncio

@pytest.mark.asyncio
async def test_create_table(dynamodb_client):
    # Define the request
    request = CreateTableRequest(
        TableName="test-table",
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST",
    )
    try:
        # Call the create_table method
        response = await dynamodb_client.create_table(request)
        # Assert the response
        assert isinstance(response, CreateTableResponse)
        assert response.TableDescription.TableName == "test-table"
    finally:
        status = 'test'
        while status != 'ACTIVE':
            await asyncio.sleep(1)
            response = await dynamodb_client.describe_table(
                DescribeTableRequest(TableName="test-table")
            )
            status = response.Table.TableStatus
        # Clean up the table
        await dynamodb_client.delete_table(
            request=DeleteTableRequest(TableName="test-table")
        )
