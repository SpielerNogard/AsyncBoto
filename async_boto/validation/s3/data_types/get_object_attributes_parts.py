from pydantic import BaseModel

from .object_part import ObjectPart


class GetObjectAttributesParts(BaseModel):
    """
    A collection of parts associated with a multipart upload.

    Attributes
    ----------
    IsTruncated : Optional[bool]
        Indicates whether the returned list of parts is truncated.
    MaxParts : Optional[int]
        The maximum number of parts allowed in the response.
    NextPartNumberMarker : Optional[int]
        Specifies the last part in the list when the list is truncated.
    PartNumberMarker : Optional[int]
        The marker for the current part.
    Parts : Optional[List[ObjectPart]]
        A container for elements related to a particular part.
    TotalPartsCount : Optional[int]
        The total number of parts.
    """

    IsTruncated: bool | None
    MaxParts: int | None
    NextPartNumberMarker: int | None
    PartNumberMarker: int | None
    Parts: list[ObjectPart] | None
    TotalPartsCount: int | None
