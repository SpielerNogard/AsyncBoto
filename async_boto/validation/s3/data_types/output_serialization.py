from pydantic import BaseModel

from .csv_output import CSVOutput
from .json_output import JSONOutput


class OutputSerialization(BaseModel):
    """
    Describes how results of the Select job are serialized.

    Attributes
    ----------
    CSV : Optional[CSVOutput]
        Describes the serialization of CSV-encoded Select results.
    JSON : Optional[JSONOutput]
        Specifies JSON as the request's output serialization format.
    """

    CSV: CSVOutput | None = None
    JSON: JSONOutput | None = None
