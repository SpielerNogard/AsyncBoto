from pydantic import BaseModel, Field


class DeletedObject(BaseModel):
    """
    Information about the deleted object.

    Attributes
    ----------
    DeleteMarker : Optional[bool]
        Indicates whether the specified object version that was permanently deleted was
        a delete marker.
    DeleteMarkerVersionId : Optional[str]
        The version ID of the delete marker created as a result of the DELETE operation.
    Key : Optional[str]
        The name of the deleted object. Must have a minimum length of 1.
    VersionId : Optional[str]
        The version ID of the deleted object.
    """

    DeleteMarker: bool | None = None
    DeleteMarkerVersionId: str | None = None
    Key: str | None = Field(None, min_length=1)
    VersionId: str | None = None
