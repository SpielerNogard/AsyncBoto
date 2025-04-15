from pydantic import BaseModel

from .inventory_s3_bucket_destination import InventoryS3BucketDestination


class InventoryDestination(BaseModel):
    """
    Specifies the inventory configuration for an Amazon S3 bucket.

    Attributes
    ----------
    S3BucketDestination : InventoryS3BucketDestination
        Contains the bucket name, file format, bucket owner (optional),
        and prefix (optional)
        where inventory results are published.
    """

    S3BucketDestination: InventoryS3BucketDestination
