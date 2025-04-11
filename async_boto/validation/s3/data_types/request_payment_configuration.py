from pydantic import BaseModel
from typing import Literal

class RequestPaymentConfiguration(BaseModel):
    """
    Container for Payer.

    Attributes
    ----------
    Payer : Literal["Requester", "BucketOwner"]
        Specifies who pays for the download and request fees.
    """
    Payer: Literal["Requester", "BucketOwner"]