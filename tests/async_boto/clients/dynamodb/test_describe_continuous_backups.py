import pytest

from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    DescribeContinuousBackupsRequest,
    DescribeContinuousBackupsResponse,
)


@pytest.mark.asyncio
async def test_describe_continuous_backups(
    dynamodb_client: AsyncDynamoDBClient, test_table: str
):
    request = DescribeContinuousBackupsRequest(TableName=test_table)
    response = await dynamodb_client.describe_continuous_backups(request=request)

    assert isinstance(response, DescribeContinuousBackupsResponse)
    assert response.ContinuousBackupsDescription.ContinuousBackupsStatus == "ENABLED"
