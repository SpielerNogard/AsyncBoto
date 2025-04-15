from typing import Literal

from pydantic import BaseModel


class CSVInput(BaseModel):
    """
    Describes how an uncompressed comma-separated values (CSV)-formatted input object
    is formatted.

    Attributes
    ----------
    AllowQuotedRecordDelimiter : Optional[bool]
        Specifies that CSV field values may contain quoted record delimiters.
        Default is False.
    Comments : Optional[str]
        A single character used to indicate that a row should be ignored when present
        at the start of the row. Default is '#'.
    FieldDelimiter : Optional[str]
        A single character used to separate individual fields in a record.
    FileHeaderInfo : Optional[Literal["USE", "IGNORE", "NONE"]]
        Describes the first line of input. Valid values are USE, IGNORE, or NONE.
    QuoteCharacter : Optional[str]
        A single character used for escaping when the field delimiter is part of the
        value. Default is '"'.
    QuoteEscapeCharacter : Optional[str]
        A single character used for escaping the quotation mark character inside an
        already escaped value.
    RecordDelimiter : Optional[str]
        A single character used to separate individual records in the input.
    """

    AllowQuotedRecordDelimiter: bool | None = False
    Comments: str | None = "#"
    FieldDelimiter: str | None = None
    FileHeaderInfo: Literal["USE", "IGNORE", "NONE"] | None = None
    QuoteCharacter: str | None = '"'
    QuoteEscapeCharacter: str | None = None
    RecordDelimiter: str | None = None
