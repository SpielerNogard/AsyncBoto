from pydantic import BaseModel


class Stats(BaseModel):
    """
    Container for the stats details.

    Attributes
    ----------
    BytesProcessed : Optional[int]
        The total number of uncompressed object bytes processed.
    BytesReturned : Optional[int]
        The total number of bytes of records payload data returned.
    BytesScanned : Optional[int]
        The total number of object bytes scanned.
    """

    BytesProcessed: int | None
    BytesReturned: int | None
    BytesScanned: int | None
