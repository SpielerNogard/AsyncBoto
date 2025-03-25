import pytest

from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    BatchGetItemRequest,
    BatchGetItemResponse,
    PutItemRequest,
)


@pytest.mark.asyncio
async def test_batch_get_item(dynamodb_client: AsyncDynamoDBClient, test_table: str):
    # prepare
    request = PutItemRequest.from_python_dict(
        data={"hash": "hash2", "sort": "sort2"},
        TableName=test_table,
        ReturnConsumedCapacity="TOTAL",
    )
    await dynamodb_client.put_item(request=request)

    request = BatchGetItemRequest(
        RequestItems={
            test_table: {"Keys": [{"hash": {"S": "hash2"}, "sort": {"S": "sort2"}}]}
        }
    )
    response = await dynamodb_client.batch_get_item(request=request)

    assert isinstance(response, BatchGetItemResponse)
    assert response.Responses[test_table][0].to_python_dict() == {
        "hash": "hash2",
        "sort": "sort2",
    }
