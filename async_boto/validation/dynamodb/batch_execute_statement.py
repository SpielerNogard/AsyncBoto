from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Literal, Union
from .data_types.batch_statement_request import BatchStatementRequest
from .data_types.batch_statement_response import BatchStatementResponse
from .data_types.consumed_capacity import ConsumedCapacity as ConsumedCapacityModel


class BatchExecuteStatementRequest(BaseModel):
    Statements: List[BatchStatementRequest]
    ReturnConsumedCapacity: Optional[Literal["INDEXES", "TOTAL", "NONE"]] = None


class BatchExecuteStatementResponse(BaseModel):
    ConsumedCapacity: Optional[List[ConsumedCapacityModel]] = None
    Responses: Optional[List[BatchStatementResponse]] = None
