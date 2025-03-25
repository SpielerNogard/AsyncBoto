import pytest

from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    CreateBackupRequest,
    CreateBackupResponse,
)
import os

skip_special = os.getenv("SKIP_SPECIAL_TESTS") == "1"


@pytest.mark.skipif(
    skip_special, reason="Skipping this test because it is not supported by localstack"
)
@pytest.mark.asyncio
async def test_create_backup(dynamodb_client: AsyncDynamoDBClient, test_table: str):
    request = CreateBackupRequest(BackupName="my-backup", TableName=test_table)
    response = await dynamodb_client.create_backup(request=request)

    assert isinstance(response, CreateBackupResponse)
    assert response.BackupDetails.BackupName == "my-backup"
