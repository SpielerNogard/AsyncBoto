import pytest

from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    DescribeTableRequest,
    DescribeTableResponse,
)


@pytest.mark.asyncio
async def test_describe_table(dynamodb_client: AsyncDynamoDBClient, test_table: str):
    request = DescribeTableRequest(
        TableName=test_table,
    )
    response = await dynamodb_client.describe_table(request=request)

    assert isinstance(response, DescribeTableResponse)
    assert response.Table.TableName == test_table
