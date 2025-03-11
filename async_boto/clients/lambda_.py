import logging
from typing import TypeVar

import boto3
from pydantic import BaseModel

from async_boto.core.base_client import BaseClient
from async_boto.validation.lambda_.add_layer_version_permissions import (
    AddLayerVersionPermissionRequest,
    AddLayerVersionPermissionResponse,
)
from async_boto.validation.lambda_.add_permission import (
    AddPermissionRequest,
    AddPermissionResponse,
)
from async_boto.validation.lambda_.create_alias import (
    CreateAliasRequest,
    CreateAliasResponse,
)
from async_boto.validation.lambda_.list_functions import (
    ListFunctionsRequest,
    ListFunctionsResponse,
)

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)


class AsyncLambdaClient(BaseClient):
    def __init__(self, aws_session: boto3.Session):
        super().__init__(aws_session=aws_session, service_name="lambda")
        self._url = f"https://lambda.{self._aws_session.region_name}.amazonaws.com"

    async def add_layer_version_permission(
        self, request: AddLayerVersionPermissionRequest
    ) -> AddLayerVersionPermissionResponse:
        headers = {
            "Content-Type": "application/x-amz-json-1.0",
        }
        url = (
            f"{self._url}/2018-10-31/layers/{request.LayerName}/"
            f"versions/{request.VersionNumber}/policy"
        )
        resp = await self._post(
            url=url,
            headers=headers,
            json=request.model_dump(
                exclude_defaults=True,
                exclude_none=True,
                exclude={"LayerName", "VersionNumber", "RevisionId"},
            ),
            params={"RevisionId": request.RevisionId} if request.RevisionId else {},
        )
        resp.raise_for_status()
        return AddLayerVersionPermissionResponse(**resp.json)

    async def add_permission(
        self, request: AddPermissionRequest
    ) -> AddPermissionResponse:
        headers = {
            "Content-Type": "application/x-amz-json-1.0",
        }
        url = self._url + f"/2015-03-31/functions/{request.FunctionName}/policy"
        resp = await self._post(
            url=url,
            headers=headers,
            json=request.model_dump(
                exclude_defaults=True,
                exclude_none=True,
                exclude={"FunctionName", "Qualifier"},
            ),
            params={"Qualifier": request.Qualifier} if request.Qualifier else {},
        )
        resp.raise_for_status()
        return AddPermissionResponse(**resp.json)

    async def create_alias(self, request: CreateAliasRequest) -> CreateAliasResponse:
        headers = {
            "Content-Type": "application/x-amz-json-1.0",
        }
        url = self._url + f"/2015-03-31/functions/{request.FunctionName}/aliases"
        resp = await self._post(
            url=url,
            headers=headers,
            json=request.model_dump(
                exclude_defaults=True,
                exclude_none=True,
                exclude={"FunctionName"},
            ),
        )
        resp.raise_for_status()
        return CreateAliasResponse(**resp.json)

    async def list_functions(
        self, request: ListFunctionsRequest
    ) -> ListFunctionsResponse:
        headers = {
            "Content-Type": "application/x-amz-json-1.0",
        }
        url = self._url + "/2015-03-31/functions/"
        resp = await self._get(
            url=url,
            headers=headers,
            json={},
            params=request.model_dump(exclude_defaults=True, exclude_none=True),
        )
        print(resp.json)
        resp.raise_for_status()
        return ListFunctionsResponse(**resp.json)


if __name__ == "__main__":
    import asyncio

    obj = AsyncLambdaClient(boto3.Session(profile_name="bestoraged-stage"))
    request = ListFunctionsRequest()
    loop = asyncio.get_event_loop()
    response = loop.run_until_complete(obj.list_functions(request))
    print(response)

    loop.close()
