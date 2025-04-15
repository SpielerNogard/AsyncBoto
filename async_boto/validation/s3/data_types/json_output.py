from pydantic import BaseModel


class JSONOutput(BaseModel):
    """
    Specifies JSON as request's output serialization format.

    Attributes
    ----------
    RecordDelimiter : Optional[str]
        The value used to separate individual records in the output.
        If no value is specified,
        Amazon S3 uses a newline character ('\\n').
    """

    RecordDelimiter: str | None
