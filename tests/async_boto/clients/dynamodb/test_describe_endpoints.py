import pytest
import boto3
from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    DeleteTableRequest,
    DescribeTableRequest,
DescribeEndpointsResponse
)
from async_boto.validation.dynamodb.create_table import (
    CreateTableRequest,
    CreateTableResponse,
)
import asyncio

@pytest.mark.asyncio
async def test_describe_endpoints(dynamodb_client):
    resp = await dynamodb_client.describe_endpoints()
    assert isinstance(resp, DescribeEndpointsResponse)