from pydantic import BaseModel, root_validator
from typing import Optional
from .replication_rule_and_operator import ReplicationRuleAndOperator
from .tag import Tag  # Assuming Tag is defined in a separate file

class ReplicationRuleFilter(BaseModel):
    """
    A filter that identifies the subset of objects to which the replication rule applies.
    A Filter must specify exactly one of Prefix, Tag, or And.

    Attributes
    ----------
    And : Optional[ReplicationRuleAndOperator]
        A container for specifying rule filters when more than one filter is used.
    Prefix : Optional[str]
        An object key name prefix that identifies the subset of objects to which the rule applies.
    Tag : Optional[Tag]
        A container for specifying a tag key and value.
    """
    And: Optional[ReplicationRuleAndOperator] = None
    Prefix: Optional[str] = None
    Tag: Optional[Tag] = None

    @root_validator
    def validate_exclusive_fields(cls, values):
        """
        Ensures that exactly one of And, Prefix, or Tag is specified.
        """
        fields = [values.get("And"), values.get("Prefix"), values.get("Tag")]
        if sum(field is not None for field in fields) != 1:
            raise ValueError("Exactly one of 'And', 'Prefix', or 'Tag' must be specified.")
        return values