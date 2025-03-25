import pytest
import boto3
from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    DeleteTableRequest,
    DescribeTableRequest, DeleteTableResponse
)
from async_boto.validation.dynamodb.create_table import (
    CreateTableRequest,
    CreateTableResponse,
)
import asyncio
import uuid

from async_boto.validation.dynamodb.put_resource_policy import PutResourcePolicyResponse


@pytest.mark.asyncio
async def test_delete_table(dynamodb_client):
    # Define the request
    name = str(uuid.uuid4())
    request = CreateTableRequest(
        TableName=name,
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST",
    )
    try:
        # Call the create_table method
        response = await dynamodb_client.create_table(request)
        # Assert the response
        assert isinstance(response, CreateTableResponse)
        assert response.TableDescription.TableName == name
    finally:
        status = 'test'
        while status != 'ACTIVE':
            await asyncio.sleep(1)
            response = await dynamodb_client.describe_table(
                DescribeTableRequest(TableName=name)
            )
            status = response.Table.TableStatus
        # Clean up the table
        resp = await dynamodb_client.delete_table(
            request=DeleteTableRequest(TableName=name)
        )
        assert isinstance(resp, DeleteTableResponse)
        assert resp.TableDescription.TableName == name
