import os

import pytest

from async_boto.clients.dynamodb import (
    DescribeEndpointsResponse,
)

skip_special = os.getenv("SKIP_SPECIAL_TESTS") == "1"


@pytest.mark.skipif(
    skip_special, reason="Skipping this test because it is not supported by localstack"
)
@pytest.mark.asyncio
async def test_describe_endpoints(dynamodb_client):
    resp = await dynamodb_client.describe_endpoints()
    assert isinstance(resp, DescribeEndpointsResponse)
