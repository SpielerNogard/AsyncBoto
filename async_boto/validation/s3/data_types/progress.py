from pydantic import BaseModel


class Progress(BaseModel):
    """
    This data type contains information about the progress of an operation.

    Attributes
    ----------
    BytesProcessed : Optional[int]
        The current number of uncompressed object bytes processed.
    BytesReturned : Optional[int]
        The current number of bytes of records payload data returned.
    BytesScanned : Optional[int]
        The current number of object bytes scanned.
    """

    BytesProcessed: int | None = None
    BytesReturned: int | None = None
    BytesScanned: int | None = None
