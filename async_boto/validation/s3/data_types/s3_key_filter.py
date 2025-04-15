from pydantic import BaseModel

from .filter_rule import FilterRule


class S3KeyFilter(BaseModel):
    """
    A container for object key name prefix and suffix filtering rules.

    Attributes
    ----------
    FilterRules : Optional[List[FilterRule]]
        A list of containers for the key-value pair that defines the criteria
        for the filter rule.
    """

    FilterRules: list[FilterRule] | None
