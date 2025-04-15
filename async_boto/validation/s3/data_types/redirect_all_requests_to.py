from typing import Literal

from pydantic import BaseModel


class RedirectAllRequestsTo(BaseModel):
    """
    Specifies the redirect behavior of all requests to a website endpoint
    of an Amazon S3 bucket.

    Attributes
    ----------
    HostName : str
        Name of the host where requests are redirected.
    Protocol : Optional[Literal["http", "https"]]
        Protocol to use when redirecting requests.
    """

    HostName: str
    Protocol: Literal["http", "https"] | None = None
