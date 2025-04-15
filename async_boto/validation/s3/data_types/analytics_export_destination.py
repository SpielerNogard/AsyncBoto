from pydantic import BaseModel

from .analytics_s3_bucket_destination import AnalyticsS3BucketDestination


class AnalyticsExportDestination(BaseModel):
    """
    Specifies where to publish the analytics results.

    Attributes
    ----------
    S3BucketDestination : AnalyticsS3BucketDestination
        A destination signifying output to an S3 bucket.
    """

    S3BucketDestination: AnalyticsS3BucketDestination
