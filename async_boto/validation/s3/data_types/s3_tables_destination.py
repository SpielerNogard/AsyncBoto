from pydantic import BaseModel

class S3TablesDestination(BaseModel):
    """
    The destination information for the metadata table configuration.

    Attributes
    ----------
    TableBucketArn : str
        The Amazon Resource Name (ARN) for the table bucket specified as the destination.
    TableName : str
        The name for the metadata table in your metadata table configuration.
    """
    TableBucketArn: str
    TableName: str