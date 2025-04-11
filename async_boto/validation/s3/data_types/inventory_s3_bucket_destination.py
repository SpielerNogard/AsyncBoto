from pydantic import BaseModel
from typing import Optional
from .inventory_encryption import InventoryEncryption

class InventoryS3BucketDestination(BaseModel):
    """
    Contains the bucket name, file format, bucket owner (optional), and prefix (optional)
    where inventory results are published.

    Attributes
    ----------
    Bucket : str
        The Amazon Resource Name (ARN) of the bucket where inventory results will be published.
    Format : str
        Specifies the output format of the inventory results.
    AccountId : Optional[str]
        The account ID that owns the destination S3 bucket.
    Encryption : Optional[InventoryEncryption]
        Contains the type of server-side encryption used to encrypt the inventory results.
    Prefix : Optional[str]
        The prefix that is prepended to all inventory results.
    """
    Bucket: str
    Format: str
    AccountId: Optional[str]
    Encryption: Optional[InventoryEncryption]
    Prefix: Optional[str]