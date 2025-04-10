import pytest
import uuid
from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    CreateTableRequest,
    ListTablesRequest,
    ListTablesResponse, DeleteTableResponse, DeleteTableRequest,
)

@pytest.mark.asyncio
async def test_paginate(dynamodb_client: AsyncDynamoDBClient):
    table_names = []
    try:
        # Create 150 tables
        for _ in range(150):
            table_name = f"test-table-{uuid.uuid4()}"
            table_names.append(table_name)
            create_request = CreateTableRequest(
                TableName=table_name,
                KeySchema=[
                    {"AttributeName": "hash", "KeyType": "HASH"},
                    {"AttributeName": "sort", "KeyType": "RANGE"},
                ],
                BillingMode="PAY_PER_REQUEST",
                AttributeDefinitions=[
                    {"AttributeName": "hash", "AttributeType": "S"},
                    {"AttributeName": "sort", "AttributeType": "S"},
                ],
            )
            await dynamodb_client.create_table(create_request)

        # Test pagination
        found_table_names = []
        request = ListTablesRequest()
        async for page in dynamodb_client.paginate(
            request=request, method_name="list_tables"
        ):
            assert isinstance(page, ListTablesResponse)
            found_table_names.extend(page.TableNames)

        assert all(table_name in found_table_names for table_name in table_names)

    finally:
        # Delete all created tables
        for table_name in table_names:
            await dynamodb_client.delete_table(DeleteTableRequest(**{"TableName": table_name}))