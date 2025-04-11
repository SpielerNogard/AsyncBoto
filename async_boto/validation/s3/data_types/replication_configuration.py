from pydantic import BaseModel
from typing import List
from .replication_rule import ReplicationRule  # Assuming ReplicationRule is defined in a separate file

class ReplicationConfiguration(BaseModel):
    """
    A container for replication rules. You can add up to 1,000 rules.
    The maximum size of a replication configuration is 2 MB.

    Attributes
    ----------
    Role : str
        The ARN of the IAM role that Amazon S3 assumes when replicating objects.
    Rules : List[ReplicationRule]
        A container for one or more replication rules.
    """
    Role: str
    Rules: List[ReplicationRule]