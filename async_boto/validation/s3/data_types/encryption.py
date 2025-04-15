from typing import Literal

from pydantic import BaseModel


class Encryption(BaseModel):
    """
    Contains the type of server-side encryption used.

    Attributes
    ----------
    EncryptionType : Literal["AES256", "aws:kms", "aws:kms:dsse"]
        The server-side encryption algorithm used when storing job results in Amazon S3.
    KMSContext : Optional[str]
        Optional encryption context for restore results if the encryption type is
        aws:kms.
    KMSKeyId : Optional[str]
        Optional ID of the symmetric encryption customer managed key for aws:kms
        encryption.
    """

    EncryptionType: Literal["AES256", "aws:kms", "aws:kms:dsse"]
    KMSContext: str | None = None
    KMSKeyId: str | None = None
