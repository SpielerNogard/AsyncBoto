from pydantic import BaseModel


class EncryptionConfiguration(BaseModel):
    """
    Specifies encryption-related information for an Amazon S3 bucket that is a
    destination for replicated objects.

    Attributes
    ----------
    ReplicaKmsKeyID : Optional[str]
        Specifies the ID (Key ARN or Alias ARN) of the customer managed AWS KMS key
        stored in AWS Key Management Service (KMS) for the destination bucket.
    """

    ReplicaKmsKeyID: str | None = None
