from pydantic import BaseModel
from typing import Optional, Literal
from .csv_input import CSVInput
from .json_input import JSONInput
from .parquet_input import ParquetInput

class InputSerialization(BaseModel):
    """
    Describes the serialization format of the object.

    Attributes
    ----------
    CompressionType : Optional[Literal["NONE", "GZIP", "BZIP2"]]
        Specifies the object's compression format.
    CSV : Optional[CSVInput]
        Describes the serialization of a CSV-encoded object.
    JSON : Optional[JSONInput]
        Specifies JSON as the object's input serialization format.
    Parquet : Optional[ParquetInput]
        Specifies Parquet as the object's input serialization format.
    """
    CompressionType: Optional[Literal["NONE", "GZIP", "BZIP2"]]
    CSV: Optional[CSVInput]
    JSON: Optional[JSONInput]
    Parquet: Optional[ParquetInput]