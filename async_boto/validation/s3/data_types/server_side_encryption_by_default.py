from pydantic import BaseModel


class ServerSideEncryptionByDefault(BaseModel):
    """
    Describes the default server-side encryption to apply to new objects in the bucket.

    Attributes
    ----------
    SSEAlgorithm : str
        Server-side encryption algorithm to use for the default encryption.
    KMSMasterKeyID : Optional[str]
        AWS Key Management Service (KMS) customer managed key ID to use
        for the default encryption.
    """

    SSEAlgorithm: str
    KMSMasterKeyID: str | None
