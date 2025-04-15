from typing import Literal

from pydantic import BaseModel


class FilterRule(BaseModel):
    """
    Specifies the Amazon S3 object key name to filter on.

    Attributes
    ----------
    Name : Optional[Literal["prefix", "suffix"]]
        The object key name prefix or suffix identifying one or more objects to which
        the filtering rule applies.
    Value : Optional[str]
        The value that the filter searches for in object key names.
    """

    Name: Literal["prefix", "suffix"] | None
    Value: str | None
