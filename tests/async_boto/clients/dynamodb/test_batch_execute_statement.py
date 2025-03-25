import pytest

from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    BatchExecuteStatementRequest,
    BatchExecuteStatementResponse,
    PutItemRequest,
)
from async_boto.validation.dynamodb.data_types.batch_statement_request import (
    BatchStatementRequest,
)


@pytest.mark.asyncio
async def test_batch_execute_statement(
    dynamodb_client: AsyncDynamoDBClient, test_table: str
):
    # prepare

    request = PutItemRequest.from_python_dict(
        data={"hash": "hash2", "sort": "sort2"},
        TableName=test_table,
        ReturnConsumedCapacity="TOTAL",
    )
    await dynamodb_client.put_item(request=request)

    batch_statement_request = BatchStatementRequest(
        Statement=f"SELECT * FROM \"{test_table}\" WHERE hash = 'hash2' and sort='sort2'",
        ConsistentRead=True,
    )
    request = BatchExecuteStatementRequest(Statements=[batch_statement_request])
    response = await dynamodb_client.batch_execute_statement(request=request)

    assert isinstance(response, BatchExecuteStatementResponse)
    assert response.Responses[0].Item.to_python_dict() == {
        "hash": "hash2",
        "sort": "sort2",
    }
