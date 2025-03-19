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
from async_boto.validation.lambda_.create_code_signing_config import (
    CreateCodeSigningConfigRequest,
    CreateCodeSigningConfigResponse,
)
from async_boto.validation.lambda_.create_event_source_mapping import (
    CreateEventSourceMappingRequest,
    CreateEventSourceMappingResponse,
)
from async_boto.validation.lambda_.create_function import (
    CreateFunctionRequest,
    CreateFunctionResponse,
)
from async_boto.validation.lambda_.create_function_url_config import (
    CreateFunctionUrlConfigRequest,
    CreateFunctionUrlConfigResponse,
)
from async_boto.validation.lambda_.delete_alias import (
    DeleteAliasRequest,
    DeleteAliasResponse,
)
from async_boto.validation.lambda_.delete_code_signing_config import (
    DeleteCodeSigningConfigRequest,
    DeleteCodeSigningConfigResponse,
)
from async_boto.validation.lambda_.delete_event_source_mapping import (
    DeleteEventSourceMappingRequest,
    DeleteEventSourceMappingResponse,
)
from async_boto.validation.lambda_.delete_function import (
    DeleteFunctionRequest,
    DeleteFunctionResponse,
)
from async_boto.validation.lambda_.delete_function_code_signing_config import (
    DeleteFunctionCodeSigningConfigRequest,
    DeleteFunctionCodeSigningConfigResponse,
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

    async def create_code_signing_config(
        self, request: CreateCodeSigningConfigRequest
    ) -> CreateCodeSigningConfigResponse:
        headers = {
            "Content-Type": "application/x-amz-json-1.0",
        }
        url = self._url + "/2020-04-22/code-signing-configs"
        resp = await self._post(
            url=url,
            headers=headers,
            json=request.model_dump(exclude_defaults=True, exclude_none=True),
        )
        resp.raise_for_status()
        return CreateCodeSigningConfigResponse(**resp.json)

    async def create_event_source_mapping(
        self, request: CreateEventSourceMappingRequest
    ) -> CreateEventSourceMappingResponse:
        headers = {
            "Content-Type": "application/x-amz-json-1.0",
        }
        url = self._url + "/2015-03-31/event-source-mappings/"
        resp = await self._post(
            url=url,
            headers=headers,
            json=request.model_dump(exclude_defaults=True, exclude_none=True),
        )
        resp.raise_for_status()
        return CreateEventSourceMappingResponse(**resp.json)

    async def create_function(
        self, request: CreateFunctionRequest
    ) -> CreateFunctionResponse:
        headers = {
            "Content-Type": "application/x-amz-json-1.0",
        }
        url = self._url + "/2015-03-31/functions"
        resp = await self._post(
            url=url,
            headers=headers,
            json=request.model_dump(exclude_defaults=True, exclude_none=True),
        )
        resp.raise_for_status()
        return CreateFunctionResponse(**resp.json)

    async def create_function_url_config(
        self, request: CreateFunctionUrlConfigRequest
    ) -> CreateFunctionUrlConfigResponse:
        headers = {
            "Content-Type": "application/x-amz-json-1.0",
        }
        url = self._url + f"/2015-03-31/functions/{request.FunctionName}/url-config"
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
        return CreateFunctionUrlConfigResponse(**resp.json)

    async def delete_alias(self, request: DeleteAliasRequest) -> DeleteAliasResponse:
        headers = {
            "Content-Type": "application/x-amz-json-1.0",
        }
        url = (
            self._url
            + f"/2015-03-31/functions/{request.FunctionName}/aliases/{request.Name}"
        )
        resp = await self._delete(
            url=url,
            headers=headers,
            json=request.model_dump(exclude_defaults=True, exclude_none=True),
        )
        resp.raise_for_status()
        return DeleteAliasResponse(**resp.json)

    async def delete_code_signing_config(
        self, request: DeleteCodeSigningConfigRequest
    ) -> DeleteCodeSigningConfigResponse:
        headers = {
            "Content-Type": "application/x-amz-json-1.0",
        }
        url = (
            self._url
            + f"/2020-04-22/code-signing-configs/{request.CodeSigningConfigArn}"
        )
        resp = await self._delete(
            url=url,
            headers=headers,
            json=request.model_dump(
                exclude_defaults=True,
                exclude_none=True,
                exclude={"CodeSigningConfigArn"},
            ),
        )
        resp.raise_for_status()
        return DeleteCodeSigningConfigResponse(**resp.json)

    async def delete_event_source_mapping(
        self, request: DeleteEventSourceMappingRequest
    ) -> DeleteEventSourceMappingResponse:
        headers = {
            "Content-Type": "application/x-amz-json-1.0",
        }
        url = self._url + f"/2015-03-31/event-source-mappings/{request.UUID}"
        resp = await self._delete(
            url=url,
            headers=headers,
            json=request.model_dump(
                exclude_defaults=True, exclude_none=True, exclude={"UUID"}
            ),
        )
        resp.raise_for_status()
        return DeleteEventSourceMappingResponse(**resp.json)

    async def delete_function(
        self, request: DeleteFunctionRequest
    ) -> DeleteFunctionResponse:
        headers = {
            "Content-Type": "application/x-amz-json-1.0",
        }
        url = self._url + f"/2015-03-31/functions/{request.FunctionName}"
        resp = await self._delete(
            url=url,
            headers=headers,
            json=request.model_dump(
                exclude_defaults=True, exclude_none=True, exclude={"FunctionName"}
            ),
            params={"Qualifier": request.Qualifier} if request.Qualifier else {},
        )
        resp.raise_for_status()
        return DeleteFunctionResponse(**resp.json)

    async def delete_function_code_signing_config(
        self, request: DeleteFunctionCodeSigningConfigRequest
    ) -> DeleteFunctionCodeSigningConfigResponse:
        headers = {
            "Content-Type": "application/x-amz-json-1.0",
        }
        url = (
            self._url
            + f"/2020-06-30/functions/{request.FunctionName}/code-signing-config"
        )
        resp = await self._delete(
            url=url,
            headers=headers,
            json=request.model_dump(
                exclude_defaults=True, exclude_none=True, exclude={"FunctionName"}
            ),
        )
        resp.raise_for_status()
        return DeleteFunctionCodeSigningConfigResponse(**resp.json)

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
