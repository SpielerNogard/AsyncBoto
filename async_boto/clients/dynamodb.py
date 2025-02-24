import logging
from typing import Type, TypeVar

import boto3
from pydantic import BaseModel

from async_boto.core.base_client import BaseClient
from async_boto.validation.dynamodb.describe_enpoints import DescribeEndpointsResponse
from async_boto.validation.dynamodb.batch_write_items import (
    BatchWriteItemRequest,
    BatchWriteItemsResponse,
)
from async_boto.validation.dynamodb.put_item import PutItemRequest, PutItemResponse
from async_boto.validation.dynamodb.scan import ScanRequest, ScanResponse
from async_boto.validation.dynamodb.query import QueryRequest, QueryResponse
from async_boto.validation.dynamodb.describe_table import (
    DescribeTableRequest,
    DescribeTableResponse,
)
from async_boto.validation.dynamodb.list_tables import (
    ListTablesRequest,
    ListTablesResponse,
)
from async_boto.validation.dynamodb.get_item import GetItemRequest, GetItemResponse
from async_boto.validation.dynamodb.batch_get_item import (
    BatchGetItemRequest,
    BatchGetItemResponse,
)
from async_boto.validation.dynamodb.delete_item import (
    DeleteItemRequest,
    DeleteItemResponse,
)
from async_boto.validation.dynamodb.create_backup import (
    CreateBackupRequest,
    CreateBackupResponse,
)
from async_boto.validation.dynamodb.batch_execute_statement import (
    BatchExecuteStatementRequest,
    BatchExecuteStatementResponse,
)
from async_boto.validation.dynamodb.create_global_table import (
    CreateGlobalTableRequest,
    CreateGlobalTableResponse,
)
from async_boto.validation.dynamodb.create_table import (
    CreateTableRequest,
    CreateTableResponse,
)
from async_boto.validation.dynamodb.delete_backup import (
    DeleteBackupRequest,
    DeleteBackupResponse,
)
from async_boto.validation.dynamodb.delete_resource_policy import (
    DeleteResourcePolicyResponse,
    DeleteResourcePolicyRequest,
)
from async_boto.validation.dynamodb.delete_table import DeleteTableRequest, DeleteTableResponse
from async_boto.validation.dynamodb.describe_backup import DescribeBackupRequest, DescribeBackupResponse
from async_boto.validation.dynamodb.describe_continous_backups import DescribeContinuousBackupsRequest, DescribeContinuousBackupsResponse
logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)


class AsyncDynamoDBClient(BaseClient):
    def __init__(self, aws_session: boto3.Session):
        super().__init__(aws_session=aws_session, service_name="dynamodb")
        self._url = f"https://dynamodb.{self._aws_session.region_name}.amazonaws.com"

    async def _make_request(
        self, target: str, request: BaseModel, response_cls: Type[T]
    ) -> T:
        headers = {
            "Content-Type": "application/x-amz-json-1.0",
            "X-Amz-Target": target,
        }
        resp = await self._post(
            url=self._url,
            headers=headers,
            json=request.model_dump(exclude_defaults=True, exclude_none=True),
        )
        resp.raise_for_status()
        print(resp.json)
        return response_cls(**resp.json)

    async def describe_endpoints(self) -> DescribeEndpointsResponse:
        return await self._make_request(
            "DynamoDB_20120810.DescribeEndpoints",
            BaseModel(),
            DescribeEndpointsResponse,
        )

    async def batch_write_items(
        self, request: BatchWriteItemRequest
    ) -> BatchWriteItemsResponse:
        return await self._make_request(
            "DynamoDB_20120810.BatchWriteItem", request, BatchWriteItemsResponse
        )

    async def put_item(self, request: PutItemRequest) -> PutItemResponse:
        return await self._make_request(
            "DynamoDB_20120810.PutItem", request, PutItemResponse
        )

    async def scan(self, request: ScanRequest) -> ScanResponse:
        return await self._make_request("DynamoDB_20120810.Scan", request, ScanResponse)

    async def query(self, request: QueryRequest) -> QueryResponse:
        return await self._make_request(
            "DynamoDB_20120810.Query", request, QueryResponse
        )

    async def describe_table(
        self, request: DescribeTableRequest
    ) -> DescribeTableResponse:
        return await self._make_request(
            "DynamoDB_20120810.DescribeTable", request, DescribeTableResponse
        )

    async def list_tables(self, request: ListTablesRequest) -> ListTablesResponse:
        return await self._make_request(
            "DynamoDB_20120810.ListTables", request, ListTablesResponse
        )

    async def get_item(self, request: GetItemRequest) -> GetItemResponse:
        return await self._make_request(
            "DynamoDB_20120810.GetItem", request, GetItemResponse
        )

    async def batch_get_item(
        self, request: BatchGetItemRequest
    ) -> BatchGetItemResponse:
        return await self._make_request(
            "DynamoDB_20120810.BatchGetItem", request, BatchGetItemResponse
        )

    async def delete_item(self, request: DeleteItemRequest) -> DeleteItemResponse:
        return await self._make_request(
            "DynamoDB_20120810.DeleteItem", request, DeleteItemResponse
        )

    async def create_backup(self, request: CreateBackupRequest) -> CreateBackupResponse:
        return await self._make_request(
            "DynamoDB_20120810.CreateBackup", request, CreateBackupResponse
        )

    async def batch_execute_statement(
        self, request: BatchExecuteStatementRequest
    ) -> BatchExecuteStatementResponse:
        return await self._make_request(
            "DynamoDB_20120810.BatchExecuteStatement",
            request,
            BatchExecuteStatementResponse,
        )

    async def create_global_table(
        self, request: CreateGlobalTableRequest
    ) -> CreateGlobalTableResponse:
        return await self._make_request(
            "DynamoDB_20120810.CreateGlobalTable", request, CreateGlobalTableResponse
        )

    async def create_table(self, request: CreateTableRequest) -> CreateTableResponse:
        return await self._make_request(
            "DynamoDB_20120810.CreateTable", request, CreateTableResponse
        )

    async def delete_backup(self, request: DeleteBackupRequest) -> DeleteBackupResponse:
        return await self._make_request(
            "DynamoDB_20120810.DeleteBackup", request, DeleteBackupResponse
        )

    async def delete_resource_policy(
        self, request: DeleteResourcePolicyRequest
    ) -> DeleteResourcePolicyResponse:
        return await self._make_request(
            "DynamoDB_20120810.DeleteResourcePolicy",
            request,
            DeleteResourcePolicyResponse,
        )

    async def delete_table(self, request: DeleteTableRequest) -> DeleteTableResponse:
        return await self._make_request(
            "DynamoDB_20120810.DeleteTable", request, DeleteTableResponse
        )

    async def describe_backup(self, request: DescribeBackupRequest) -> DescribeBackupResponse:
        return await self._make_request(
            "DynamoDB_20120810.DescribeBackup", request, DescribeBackupResponse
        )

    async def describe_continuous_backups(self, request: DescribeContinuousBackupsRequest) -> DescribeContinuousBackupsResponse:
        return await self._make_request(
            "DynamoDB_20120810.DescribeContinuousBackups", request, DescribeContinuousBackupsResponse
        )


if __name__ == "__main__":
    import asyncio
    from async_boto.core.errors import APIResponseException

    my_session = boto3.Session(profile_name="bestoraged-lab-crmuelle")
    client = AsyncDynamoDBClient(aws_session=my_session)

    loop = asyncio.get_event_loop()

    # # Example usage of batch_write_items
    # from async_boto.validation.dynamodb.data_types.write_request import WriteRequest
    # from async_boto.validation.dynamodb.data_types.put_request import PutRequest
    # items_to_write = [
    #     PutRequest.from_python_dict({"hash": "1", "sort": "Item 1"}),
    #     PutRequest.from_python_dict({"hash": "2", "sort": "Item 2"}),
    # ]
    #
    # try:
    #     resp = loop.run_until_complete(
    #         client.batch_write_items(
    #             BatchWriteItemRequest(
    #                 RequestItems={
    #                     "user_testing": [
    #                         WriteRequest.from_item(item) for item in items_to_write
    #                     ]
    #                 }
    #             )
    #         )
    #     )
    #     print(resp.model_dump())
    # except APIResponseException as e:
    #     print("Error")
    #     print(f"{e}")
    #     print(e.error_type)

    # # Example to put an item
    # item_to_put = {"hash": "123", "sort": "Sample Item", "value": 42}
    # put_resp = loop.run_until_complete(
    #     client.put_item(
    #         PutItemRequest.from_python_dict(item_to_put, TableName="user_testing")
    #     )
    # )
    # print("Put Item Response:", put_resp)
    #
    # # Example to scan table
    # item_to_put = {"hash": "123", "sort": "Sample Item", "value": 42}
    # put_resp = loop.run_until_complete(client.scan(
    #     ScanRequest(TableName="user_testing")))
    # [print(item.to_python_dict()) for item in put_resp.Items]
    # print("Put Item Response:", put_resp)

    # # Example of query items
    # query_resp = loop.run_until_complete(client.query(
    #     QueryRequest(TableName="user_testing", KeyConditionExpression="#hash = :hash",
    #         ExpressionAttributeNames={"#hash": "hash"},
    #         ExpressionAttributeValues={":hash": {"S": "123"}}, )
    # ))
    # print([item.to_python_dict() for item in query_resp.Items])
    # print("Query Response:", query_resp)
    #
    # # Example of describe table
    # describe_table_resp = loop.run_until_complete(client.describe_table(
    #     DescribeTableRequest(TableName="user_testing")
    # ))
    # print(describe_table_resp)

    # Example of list tables
    # list_tables_resp = loop.run_until_complete(client.list_tables(ListTablesRequest()))
    # print(list_tables_resp)
    #
    # # Example of get item
    # get_item_resp = loop.run_until_complete(
    #     client.get_item(
    #         GetItemRequest(
    #             TableName="user_testing",
    #             Key={"hash": {"S": "123"}, "sort": {"S": "Sample Item"}},
    #         )
    #     )
    # )
    # print(get_item_resp)

    # # Example of batch get item
    # batch_get_item_resp = loop.run_until_complete(
    #     client.batch_get_item(
    #         BatchGetItemRequest(
    #             RequestItems={
    #                 "user_testing": {
    #                     "Keys": [
    #                         {"hash": {"S": "123"}, "sort": {"S": "Sample Item"}},
    #                         {"hash": {"S": "1"}, "sort": {"S": "Item 1"}},
    #                     ]
    #                 }
    #             }
    #         )
    #     )
    # )
    # print(batch_get_item_resp)

    # # Example of delete item
    # delete_item_resp = loop.run_until_complete(
    #     client.delete_item(
    #         DeleteItemRequest(
    #             TableName="user_testing",
    #             Key={"hash": {"S": "123"}, "sort": {"S": "Sample Item"}},
    #         )
    #     )
    # )
    # print(delete_item_resp)

    # # Example of create backup
    # create_backup_resp = loop.run_until_complete(
    #     client.create_backup(
    #         CreateBackupRequest(
    #             BackupName="backup-1",
    #             TableName="user_testing",
    #         )
    #     )
    # )
    # print(create_backup_resp)

    # # Example of batch execute statement
    # batch_execute_statement_resp = loop.run_until_complete(
    #     client.batch_execute_statement(
    #         BatchExecuteStatementRequest(
    #             Statements=[
    #                 {
    #                     "Statement": "SELECT * FROM user_testing where HASH = '123'",
    #                     "ConsistentRead": True,
    #                 }
    #             ]
    #         )
    #     )
    # )
    # print(batch_execute_statement_resp)

    # # Example of create global table
    # create_global_table_resp = loop.run_until_complete(
    #     client.create_global_table(
    #         CreateGlobalTableRequest(
    #             GlobalTableName="user_testing",
    #             ReplicationGroup=[
    #                 {
    #                     "RegionName": "eu-central-1",
    #                 }
    #             ],
    #         )
    #     )
    # )
    # print(create_global_table_resp)

    # # Example of create table
    # create_table_resp = loop.run_until_complete(
    #     client.create_table(
    #         CreateTableRequest(
    #             TableName="user_testing_async",
    #             KeySchema=[
    #                 {"AttributeName": "hash", "KeyType": "HASH"},
    #                 {"AttributeName": "sort", "KeyType": "RANGE"},
    #             ],
    #             AttributeDefinitions=[
    #                 {"AttributeName": "hash", "AttributeType": "S"},
    #                 {"AttributeName": "sort", "AttributeType": "S"},
    #             ],
    #             BillingMode="PAY_PER_REQUEST"
    #         )
    #     )
    # )
    # print(create_table_resp)

    # # Example of delete backup
    # delete_backup_resp = loop.run_until_complete(
    #     client.delete_backup(
    #         DeleteBackupRequest(BackupArn=create_backup_resp.BackupDetails.BackupArn)
    #     )
    # )
    # print(delete_backup_resp)

    # # Example of delete table
    # delete_table_resp = loop.run_until_complete(
    #     client.delete_table(
    #         DeleteTableRequest(TableName="user_testing_async")
    #     )
    # )
    # print(delete_table_resp)

    # Example of describe backup
    backup_description = loop.run_until_complete(
        client.describe_backup(
            DescribeBackupRequest(BackupArn="arn:aws:dynamodb:eu-central-1:654654421974:table/user_testing/backup/01740392783544-d59f8800")
        )
    )
    print(backup_description)

    # Example of describe continuous backups
    continuous_backups_description = loop.run_until_complete(
        client.describe_continuous_backups(
            DescribeContinuousBackupsRequest(TableName="user_testing")
        )
    )
    loop.close()


# TODO
# async_boto.core.errors.APIResponseException: https://dynamodb.eu-central-1.amazonaws.com returned 400, content:{"__type":"com.amazon.coral.validate#ValidationException","message":"Supplied AttributeValue has more than one datatypes set, must contain exactly one of the supported datatypes"}, json:{'__type': 'com.amazon.coral.validate#ValidationException', 'message': 'Supplied AttributeValue has more than one datatypes set, must contain exactly one of the supported datatypes'}
