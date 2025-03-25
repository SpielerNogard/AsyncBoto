import uuid

import pytest

from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    CreateGlobalTableRequest,
    CreateGlobalTableResponse, DescribeGlobalTableSettingsRequest, DescribeGlobalTableSettingsResponse
)

import os

skip_special = os.getenv("SKIP_SPECIAL_TESTS") == "1"


@pytest.mark.skipif(
    skip_special, reason="Skipping this test because it is not supported by localstack"
)
@pytest.mark.asyncio
async def test_describe_global_table_settings(
    dynamodb_client: AsyncDynamoDBClient, test_table: str
):
    # prepare
    name = str(uuid.uuid4())
    request = CreateGlobalTableRequest(
        GlobalTableName=name, ReplicationGroup=[{"Region": "us-west-2"}]
    )
    response = await dynamodb_client.create_global_table(request=request)

    assert isinstance(response, CreateGlobalTableResponse)
    assert response.GlobalTableDescription.GlobalTableName == name

    request = DescribeGlobalTableSettingsRequest(GlobalTableName=name)
    response = await dynamodb_client.describe_global_table_settings(request=request)

    assert isinstance(response, DescribeGlobalTableSettingsResponse)
    assert response.GlobalTableName == name

