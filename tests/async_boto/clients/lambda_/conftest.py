import os

import boto3
import pytest

from async_boto.clients.lambda_ import AsyncLambdaClient
from async_boto.core.session import AsyncAWSSession

@pytest.fixture(scope="session")
async def lambda_client():
    mode = os.environ.get("mode", "local-boto")
    if mode == "local-boto":
        # Mock AWS session
        session = boto3.Session(region_name="us-west-2")
        client = AsyncLambdaClient(
            aws_session=session, endpoint_url="http://localhost:4566"
        )
        yield client
        # Add any necessary cleanup here
    if mode == "local-async":
        # Mock AWS session
        session = AsyncAWSSession(region_name="us-west-2")
        client = AsyncLambdaClient(
            aws_session=session, endpoint_url="http://localhost:4566"
        )
        yield client
        # Add any necessary cleanup here
    else:
        session = boto3.Session()
        client = AsyncLambdaClient(aws_session=session)
        yield client
