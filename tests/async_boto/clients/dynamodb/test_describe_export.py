import os

import pytest

from async_boto.clients.dynamodb import (
    AsyncDynamoDBClient,
    DescribeExportRequest,
    DescribeExportResponse,
    ExportTableToPointInTimeRequest,
)

skip_special = os.getenv("SKIP_SPECIAL_TESTS") == "1"


@pytest.mark.skipif(
    skip_special, reason="Skipping this test because it is not supported by localstack"
)
@pytest.mark.asyncio
async def test_describe_export(dynamodb_client: AsyncDynamoDBClient, test_table: str):
    request = ExportTableToPointInTimeRequest(
        TableArn=f"arn:aws:dynamodb:us-west-2:123456789012:table/{test_table}",
        S3Bucket="test_bucket",
    )
    response = await dynamodb_client.export_table_to_point_in_time(request)

    request = DescribeExportRequest(ExportArn=response.ExportArn)
    response = await dynamodb_client.describe_export(request=request)

    assert isinstance(response, DescribeExportResponse)
    assert (
        response.ExportDescription.TableArn
        == f"arn:aws:dynamodb:us-west-2:123456789012:table/{test_table}"
    )
