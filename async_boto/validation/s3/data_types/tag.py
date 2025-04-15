from pydantic import BaseModel, Field


class Tag(BaseModel):
    """
    A container of a key-value name pair.

    Attributes
    ----------
    Key : str
        Name of the object key. Must have a minimum length of 1.
    Value : str
        Value of the tag.
    """

    Key: str = Field(..., min_length=1)
    Value: str
