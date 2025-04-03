import pytest

from async_boto.clients.lambda_ import (
    AsyncLambdaClient,
    ListFunctionsRequest,
    ListFunctionsResponse,
)


@pytest.mark.asyncio
async def test_list_functions(lambda_client: AsyncLambdaClient):
    request = ListFunctionsRequest()
    response = await lambda_client.list_functions(request=request)

    assert isinstance(response, ListFunctionsResponse)
