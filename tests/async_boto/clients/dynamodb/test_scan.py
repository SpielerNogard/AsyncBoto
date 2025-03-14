import pytest

from async_boto.clients.dynamodb import (
    PutItemResponse,
    PutItemRequest,
    AsyncDynamoDBClient,
ScanRequest, ScanResponse,
)


@pytest.mark.asyncio
async def test_scan(dynamodb_client: AsyncDynamoDBClient, test_table: str):

    # prepare
    request = PutItemRequest.from_python_dict(
        data={"hash": "hash2", "sort": "sort2"},
        TableName=test_table,
        ReturnConsumedCapacity="TOTAL",
    )
    await dynamodb_client.put_item(request=request)

    request = ScanRequest(TableName=test_table)
    response = await dynamodb_client.scan(request=request)


    assert isinstance(response, ScanResponse)

    items = [item.to_python_dict() for item in response.Items]
    assert items == [{'hash': 'hash2', 'sort': 'sort2'}]
