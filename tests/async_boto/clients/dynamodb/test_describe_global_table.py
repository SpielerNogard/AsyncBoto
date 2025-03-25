import uuid

import pytest

from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    CreateGlobalTableRequest,
    CreateGlobalTableResponse, DescribeGlobalTableResponse, DescribeGlobalTableRequest
)


@pytest.mark.asyncio
async def test_describe_global_table(
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

    request = DescribeGlobalTableRequest(GlobalTableName=name)
    response = await dynamodb_client.describe_global_table(request=request)

    assert isinstance(response, DescribeGlobalTableResponse)
    assert response.GlobalTableDescription.GlobalTableName == name

