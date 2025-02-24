from pydantic import BaseModel, constr, conint
from typing import Literal, Optional
from datetime import datetime
from .s3_bucket_source import S3BucketSource as S3BucketSourceModel
from .input_format_options import InputFormatOptions as InputFormatOptionsModel
from .table_creation_parameters import TableCreationParameters as TableCreationParametersModel

class ImportTableDescription(BaseModel):
    """
    Represents the properties of the table being imported into.

    Attributes
    ----------
    ClientToken : Optional[constr(regex=r'^[^\$]+$')]
        The client token that was provided for the import task.
    CloudWatchLogGroupArn : Optional[constr(min_length=1, max_length=1024)]
        The Amazon Resource Number (ARN) of the Cloudwatch Log Group associated with the target table.
    EndTime : Optional[datetime]
        The time at which the creation of the table associated with this import task completed.
    ErrorCount : Optional[conint(ge=0)]
        The number of errors occurred on importing the source file into the target table.
    FailureCode : Optional[str]
        The error code corresponding to the failure that the import job ran into during execution.
    FailureMessage : Optional[str]
        The error message corresponding to the failure that the import job ran into during execution.
    ImportArn : Optional[constr(min_length=37, max_length=1024)]
        The Amazon Resource Number (ARN) corresponding to the import request.
    ImportedItemCount : Optional[conint(ge=0)]
        The number of items successfully imported into the new table.
    ImportStatus : Optional[Literal['IN_PROGRESS', 'COMPLETED', 'CANCELLING', 'CANCELLED', 'FAILED']]
        The status of the import.
    InputCompressionType : Optional[Literal['GZIP', 'ZSTD', 'NONE']]
        The compression options for the data that has been imported into the target table.
    InputFormat : Optional[Literal['DYNAMODB_JSON', 'ION', 'CSV']]
        The format of the source data going into the target table.
    InputFormatOptions : Optional[InputFormatOptions]
        The format options for the data that was imported into the target table.
    ProcessedItemCount : Optional[conint(ge=0)]
        The total number of items processed from the source file.
    ProcessedSizeBytes : Optional[conint(ge=0)]
        The total size of data processed from the source file, in Bytes.
    S3BucketSource : Optional[S3BucketSource]
        Values for the S3 bucket the source file is imported from.
    StartTime : Optional[datetime]
        The time when this import task started.
    TableArn : Optional[constr(min_length=1, max_length=1024)]
        The Amazon Resource Number (ARN) of the table being imported into.
    TableCreationParameters : Optional[TableCreationParameters]
        The parameters for the new table that is being imported into.
    TableId : Optional[constr(regex=r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')]
        The table id corresponding to the table created by import table process.
    """
    ClientToken: Optional[constr(pattern=r'^[^\$]+$')] = None
    CloudWatchLogGroupArn: Optional[constr(min_length=1, max_length=1024)] = None
    EndTime: Optional[datetime] = None
    ErrorCount: Optional[conint(ge=0)] = None
    FailureCode: Optional[str] = None
    FailureMessage: Optional[str] = None
    ImportArn: Optional[constr(min_length=37, max_length=1024)] = None
    ImportedItemCount: Optional[conint(ge=0)] = None
    ImportStatus: Optional[Literal['IN_PROGRESS', 'COMPLETED', 'CANCELLING', 'CANCELLED', 'FAILED']] = None
    InputCompressionType: Optional[Literal['GZIP', 'ZSTD', 'NONE']] = None
    InputFormat: Optional[Literal['DYNAMODB_JSON', 'ION', 'CSV']] = None
    InputFormatOptions: Optional[InputFormatOptionsModel] = None
    ProcessedItemCount: Optional[conint(ge=0)] = None
    ProcessedSizeBytes: Optional[conint(ge=0)] = None
    S3BucketSource: Optional[S3BucketSourceModel] = None
    StartTime: Optional[datetime] = None
    TableArn: Optional[constr(min_length=1, max_length=1024)] = None
    TableCreationParameters: Optional[TableCreationParametersModel] = None
    TableId: Optional[constr(pattern=r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')] = None