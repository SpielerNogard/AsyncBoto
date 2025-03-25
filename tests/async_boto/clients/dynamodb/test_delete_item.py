import pytest

from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    BatchGetItemResponse,
    DeleteItemRequest,
    PutItemRequest, DeleteItemResponse, ScanRequest, ScanResponse,
)


@pytest.mark.asyncio
async def test_delete_item(dynamodb_client: AsyncDynamoDBClient, test_table: str):
    # prepare
    request = PutItemRequest.from_python_dict(
        data={"hash": "hash2", "sort": "sort2"},
        TableName=test_table,
        ReturnConsumedCapacity="TOTAL",
    )
    await dynamodb_client.put_item(request=request)

    request = DeleteItemRequest.from_python_dict({"hash": "hash2", "sort": "sort2"}, TableName=test_table)
    response = await dynamodb_client.delete_item(request=request)

    assert isinstance(response, DeleteItemResponse)

    request = ScanRequest(TableName=test_table)
    response = await dynamodb_client.scan(request=request)


    assert isinstance(response, ScanResponse)

    items = [item.to_python_dict() for item in response.Items]
    assert items == []
