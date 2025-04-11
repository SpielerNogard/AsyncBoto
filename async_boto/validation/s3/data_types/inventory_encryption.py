from pydantic import BaseModel
from typing import Optional
from .sse_kms import SSEKMS
from .sse_s3 import SSES3

class InventoryEncryption(BaseModel):
    """
    Contains the type of server-side encryption used to encrypt the inventory results.

    Attributes
    ----------
    SSEKMS : Optional[SSEKMS]
        Specifies the use of SSE-KMS to encrypt delivered inventory reports.
    SSES3 : Optional[SSES3]
        Specifies the use of SSE-S3 to encrypt delivered inventory reports.
    """
    SSEKMS: Optional[SSEKMS]
    SSES3: Optional[SSES3]