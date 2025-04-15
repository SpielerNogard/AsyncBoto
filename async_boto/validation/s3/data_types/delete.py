from pydantic import BaseModel

from .object_identifier import ObjectIdentifier


class Delete(BaseModel):
    """
    Container for the objects to delete.

    Attributes
    ----------
    Objects : List[ObjectIdentifier]
        The objects to delete.
    Quiet : Optional[bool]
        Element to enable quiet mode for the request. Defaults to None.
    """

    Objects: list[ObjectIdentifier]
    Quiet: bool | None = None
