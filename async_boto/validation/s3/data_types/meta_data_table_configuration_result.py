from pydantic import BaseModel

from .s3_tables_destination_result import S3TablesDestinationResult


class MetadataTableConfigurationResult(BaseModel):
    """
    The metadata table configuration for a general purpose bucket.

    Attributes
    ----------
    S3TablesDestinationResult : S3TablesDestinationResult
        The destination information for the metadata table configuration.
        The destination table bucket must
        be in the same Region and AWS account as the general purpose bucket.
        The specified metadata table
        name must be unique within the aws_s3_metadata namespace in the destination
        table bucket.
    """

    S3TablesDestinationResult: S3TablesDestinationResult
