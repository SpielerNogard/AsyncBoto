from pydantic import BaseModel


class MetadataEntry(BaseModel):
    """
    A metadata key-value pair to store with an object.

    Attributes
    ----------
    Name : Optional[str]
        Name of the object.
    Value : Optional[str]
        Value of the object.
    """

    Name: str | None = None
    Value: str | None = None
