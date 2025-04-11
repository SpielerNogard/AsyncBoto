from pydantic import BaseModel

class S3TablesDestinationResult(BaseModel):
    """
    The destination information for the metadata table configuration.

    Attributes
    ----------
    TableArn : str
        The Amazon Resource Name (ARN) for the metadata table in the metadata table configuration.
    TableBucketArn : str
        The Amazon Resource Name (ARN) for the table bucket specified as the destination.
    TableName : str
        The name for the metadata table in your metadata table configuration.
    TableNamespace : str
        The table bucket namespace for the metadata table in your metadata table configuration.
    """
    TableArn: str
    TableBucketArn: str
    TableName: str
    TableNamespace: str