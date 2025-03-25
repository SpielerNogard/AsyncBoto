import pytest

from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    DescribeContinuousBackupsRequest,
    DescribeContinuousBackupsResponse,DescribeContributorInsightsRequest, DescribeContributorInsightsResponse,
)

import os

skip_special = os.getenv("SKIP_SPECIAL_TESTS") == "1"


@pytest.mark.skipif(
    skip_special, reason="Skipping this test because it is not supported by localstack"
)
@pytest.mark.asyncio
async def test_describe_contributor_insights(
    dynamodb_client: AsyncDynamoDBClient, test_table: str
):
    request = DescribeContributorInsightsRequest(TableName=test_table)
    response = await dynamodb_client.describe_contributor_insights(request=request)

    assert isinstance(response, DescribeContributorInsightsResponse)
    assert response.TableName == test_table
