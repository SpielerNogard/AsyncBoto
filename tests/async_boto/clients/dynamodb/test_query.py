import pytest

from async_boto.clients.dynamodb import (
    PutItemResponse,
    PutItemRequest,
    AsyncDynamoDBClient,
    ScanRequest,
    ScanResponse,
    QueryResponse,
    QueryRequest,
)


@pytest.mark.asyncio
async def test_query(dynamodb_client: AsyncDynamoDBClient, test_table: str):
    # prepare
    request = PutItemRequest.from_python_dict(
        data={"hash": "hash2", "sort": "sort2"},
        TableName=test_table,
        ReturnConsumedCapacity="TOTAL",
    )
    await dynamodb_client.put_item(request=request)

    request = QueryRequest(
        TableName=test_table,
        ExpressionAttributeValues={
            ":v1": {
                "S": "hash2",
            },
        },
        KeyConditionExpression="#h=:v1",
        ExpressionAttributeNames={
            "#h": "hash",
        },
    )
    response = await dynamodb_client.query(request=request)

    assert isinstance(response, QueryResponse)

    items = [item.to_python_dict() for item in response.Items]
    assert items == [{"hash": "hash2", "sort": "sort2"}]
