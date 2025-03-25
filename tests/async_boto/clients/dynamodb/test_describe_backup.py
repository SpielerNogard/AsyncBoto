import uuid

import pytest

from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    CreateBackupRequest,
    CreateBackupResponse, DescribeBackupResponse, DescribeBackupRequest
)
import os

skip_special = os.getenv("SKIP_SPECIAL_TESTS") == "1"


@pytest.mark.skipif(
    skip_special, reason="Skipping this test because it is not supported by localstack"
)
@pytest.mark.asyncio
async def test_describe_backup(dynamodb_client: AsyncDynamoDBClient, test_table: str):
    name = f'{uuid.uuid4()}'
    request = CreateBackupRequest(BackupName=name, TableName=test_table)
    response = await dynamodb_client.create_backup(request=request)

    assert isinstance(response, CreateBackupResponse)
    assert response.BackupDetails.BackupName == name

    request = DescribeBackupRequest(BackupArn=response.BackupDetails.BackupArn)
    response = await dynamodb_client.describe_backup(request=request)
    assert isinstance(response, DescribeBackupResponse)
    assert response.BackupDescription.BackupDetails.BackupName == name
