import pytest

from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    DescribeTableRequest,
    DescribeTableResponse,
ListTablesRequest, ListTablesResponse,
)


@pytest.mark.asyncio
async def test_list_tables(dynamodb_client: AsyncDynamoDBClient, test_table: str):
    request = ListTablesRequest()
    response = await dynamodb_client.list_tables(request=request)

    assert isinstance(response, ListTablesResponse)
    assert test_table in response.TableNames
