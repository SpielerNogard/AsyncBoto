import pytest
import boto3
from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    DeleteTableRequest,
    DescribeTableRequest,
    DescribeEndpointsResponse,
)
from async_boto.validation.dynamodb.create_table import (
    CreateTableRequest,
    CreateTableResponse,
)
import asyncio
import os

skip_special = os.getenv("SKIP_SPECIAL_TESTS") == "1"


@pytest.mark.skipif(
    skip_special, reason="Skipping this test because it is not supported by localstack"
)
@pytest.mark.asyncio
async def test_describe_endpoints(dynamodb_client):
    resp = await dynamodb_client.describe_endpoints()
    assert isinstance(resp, DescribeEndpointsResponse)
