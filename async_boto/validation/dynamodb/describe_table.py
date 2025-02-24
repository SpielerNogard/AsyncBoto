from pydantic import Field, BaseModel

from .data_types.table_description import TableDescription


class DescribeTableRequest(BaseModel):
    TableName: str = Field(..., min_length=1, max_length=1024)


class DescribeTableResponse(BaseModel):
    Table: TableDescription
