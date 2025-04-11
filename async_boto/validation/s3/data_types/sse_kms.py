from pydantic import BaseModel

class SSEKMS(BaseModel):
    """
    Specifies the use of SSE-KMS to encrypt delivered inventory reports.

    Attributes
    ----------
    KeyId : str
        Specifies the ID of the AWS KMS symmetric encryption customer managed key
        to use for encrypting inventory reports.
    """
    KeyId: str