from pydantic import BaseModel, root_validator

from .partitioned_prefix import PartitionedPrefix
from .simple_prefix import SimplePrefix


class TargetObjectKeyFormat(BaseModel):
    """
    Amazon S3 key format for log objects. Only one format, PartitionedPrefix or
    SimplePrefix, is allowed.

    Attributes
    ----------
    PartitionedPrefix : Optional[PartitionedPrefix]
        Partitioned S3 key for log objects.
    SimplePrefix : Optional[SimplePrefix]
        To use the simple format for S3 keys for log objects.
    """

    PartitionedPrefix: PartitionedPrefix | None
    SimplePrefix: SimplePrefix | None

    @root_validator
    def validate_exclusive_fields(cls, values):
        if values.get("PartitionedPrefix") and values.get("SimplePrefix"):
            raise ValueError(
                "Only one of PartitionedPrefix or SimplePrefix can be set."
            )
        return values
