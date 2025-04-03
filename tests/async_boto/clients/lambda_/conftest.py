import os

import boto3
import pytest

from async_boto.clients.lambda_ import AsyncLambdaClient


@pytest.fixture(scope="session")
async def lambda_client():
    if os.environ.get("mode", "local") == "local":
        # Mock AWS session
        session = boto3.Session(region_name="us-west-2")
        client = AsyncLambdaClient(
            aws_session=session, endpoint_url="http://localhost:4566"
        )
        yield client
        # Add any necessary cleanup here
    else:
        session = boto3.Session()
        client = AsyncLambdaClient(aws_session=session)
        yield client
