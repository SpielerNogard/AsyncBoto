import pytest

from async_boto.clients.dynamodb import (
    PutItemResponse,
    PutItemRequest,
    AsyncDynamoDBClient,
)


@pytest.mark.asyncio
async def test_put_item(dynamodb_client: AsyncDynamoDBClient, test_table: str):
    request = PutItemRequest.from_python_dict(
        data={"hash": "hash2", "sort": "sort2"},
        TableName=test_table,
        ReturnConsumedCapacity="TOTAL",
    )

    response = await dynamodb_client.put_item(request=request)
    assert isinstance(response, PutItemResponse)
    assert response.ConsumedCapacity.CapacityUnits == 1.0
    assert response.ConsumedCapacity.TableName == test_table
