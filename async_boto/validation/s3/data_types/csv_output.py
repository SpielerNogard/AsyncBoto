from pydantic import BaseModel
from typing import Optional, Literal

class CSVOutput(BaseModel):
    """
    Describes how uncompressed comma-separated values (CSV)-formatted results are formatted.

    Attributes
    ----------
    FieldDelimiter : Optional[str]
        The value used to separate individual fields in a record.
    QuoteCharacter : Optional[str]
        A single character used for escaping when the field delimiter is part of the value.
    QuoteEscapeCharacter : Optional[str]
        The single character used for escaping the quote character inside an already escaped value.
    QuoteFields : Optional[Literal["ALWAYS", "ASNEEDED"]]
        Indicates whether to use quotation marks around output fields.
    RecordDelimiter : Optional[str]
        A single character used to separate individual records in the output.
    """
    FieldDelimiter: Optional[str] = None
    QuoteCharacter: Optional[str] = None
    QuoteEscapeCharacter: Optional[str] = None
    QuoteFields: Optional[Literal["ALWAYS", "ASNEEDED"]] = None
    RecordDelimiter: Optional[str] = None