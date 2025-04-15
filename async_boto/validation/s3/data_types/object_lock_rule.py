from pydantic import BaseModel

from .default_retention import DefaultRetention


class ObjectLockRule(BaseModel):
    """
    Represents an Object Lock rule.

    Attributes
    ----------
    DefaultRetention : Optional[DefaultRetention]
        The default Object Lock retention mode and period for new objects in the bucket.
    """

    DefaultRetention: DefaultRetention | None = None
