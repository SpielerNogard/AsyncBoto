from pydantic import BaseModel


class InventoryFilter(BaseModel):
    """
    Specifies an inventory filter. The inventory only includes objects that meet the
    filter's criteria.

    Attributes
    ----------
    Prefix : str
        The prefix that an object must have to be included in the inventory results.
    """

    Prefix: str
