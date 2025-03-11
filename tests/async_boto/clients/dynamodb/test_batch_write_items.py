import pytest

from async_boto.clients.dynamodb import (
    BatchWriteItemRequest,
    BatchWriteItemsResponse,
)


@pytest.mark.asyncio
async def test_batch_write_items(dynamodb_client, test_table):
    request = BatchWriteItemRequest(
        RequestItems={
            test_table: [
                {
                    "PutRequest": {
                        "Item": {"hash": {"S": "hash1"}, "sort": {"S": "sort1"}}
                    }
                }
            ]
        }
    )

    response = await dynamodb_client.batch_write_items(request=request)
    assert isinstance(response, BatchWriteItemsResponse)
    assert response.UnprocessedItems == {}
