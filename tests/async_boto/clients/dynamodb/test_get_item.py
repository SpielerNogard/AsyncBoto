import pytest

from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    DescribeTableRequest,
    DescribeTableResponse,
    ListTablesRequest,
    ListTablesResponse,
    GetItemRequest,
    GetItemResponse,
)
import pytest

from async_boto.clients.dynamodb import (
    PutItemResponse,
    PutItemRequest,
    AsyncDynamoDBClient,
ScanRequest, ScanResponse,
)


@pytest.mark.asyncio
async def test_get_item(dynamodb_client: AsyncDynamoDBClient, test_table: str):
    # prepare
    request = PutItemRequest.from_python_dict(
        data={"hash": "hash2", "sort": "sort2"},
        TableName=test_table,
        ReturnConsumedCapacity="TOTAL",
    )
    await dynamodb_client.put_item(request=request)

    request = GetItemRequest(
        TableName=test_table, Key={"hash": {"S": "hash2"}, "sort": {"S": "sort2"}}
    )
    response = await dynamodb_client.get_item(request=request)

    assert isinstance(response, GetItemResponse)
    assert response.Item.to_python_dict() == {"hash": "hash2", "sort": "sort2"}
