from typing import Literal

from pydantic import BaseModel


class RequestPaymentConfiguration(BaseModel):
    """
    Container for Payer.

    Attributes
    ----------
    Payer : Literal["Requester", "BucketOwner"]
        Specifies who pays for the download and request fees.
    """

    Payer: Literal["Requester", "BucketOwner"]
