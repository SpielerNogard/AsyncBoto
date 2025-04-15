from typing import Literal

from pydantic import BaseModel

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

    CompressionType: Literal["NONE", "GZIP", "BZIP2"] | None
    CSV: CSVInput | None
    JSON: JSONInput | None
    Parquet: ParquetInput | None
