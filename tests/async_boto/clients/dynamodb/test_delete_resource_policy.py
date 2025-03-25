import pytest

from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    CreateBackupRequest,
    CreateBackupResponse,
    DeleteBackupResponse,
    DeleteBackupRequest,
    PutResourcePolicyResponse,
    PutResourcePolicyRequest,
    DeleteResourcePolicyResponse,
    DeleteResourcePolicyRequest,
    CreateTableResponse,
    CreateTableRequest,
    DescribeTableRequest,
    DeleteTableRequest,
)
import os
import uuid
import asyncio
import json


skip_special = os.getenv("SKIP_SPECIAL_TESTS") == "1"


@pytest.mark.skipif(
    skip_special, reason="Skipping this test because it is not supported by localstack"
)
@pytest.mark.asyncio
async def test_delete_resource_policy(
    dynamodb_client: AsyncDynamoDBClient
):
    name = str(uuid.uuid4())

    request = CreateTableRequest(
        TableName=name,
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST",
    )
    try:
        # Call the create_table method
        response = await dynamodb_client.create_table(request)
        # Assert the response
        assert isinstance(response, CreateTableResponse)
        assert response.TableDescription.TableName == name

        status = "test"
        while status != "ACTIVE":
            await asyncio.sleep(1)
            response_ = await dynamodb_client.describe_table(
                DescribeTableRequest(TableName=name)
            )
            status = response_.Table.TableStatus

        request = PutResourcePolicyRequest(
            Policy=json.dumps(
                {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": "*",
                            "Action": "dynamodb:*",
                            "Resource": response.TableDescription.TableArn,
                        }
                    ],
                }
            ),
            ResourceArn=response.TableDescription.TableArn,
        )

        response = await dynamodb_client.put_resource_policy(request)

        request = DeleteResourcePolicyRequest(
            ResourceArn=response.TableDescription.TableArn,
            RevisionId=response.RevisionId,
        )
        response = await dynamodb_client.delete_resource_policy(request)
        assert isinstance(response, DeleteResourcePolicyResponse)

    finally:
        status = "test"
        while status != "ACTIVE":
            await asyncio.sleep(1)
            response = await dynamodb_client.describe_table(
                DescribeTableRequest(TableName=name)
            )
            status = response.Table.TableStatus
        # Clean up the table
        await dynamodb_client.delete_table(
            request=DeleteTableRequest(TableName=name)
        )
