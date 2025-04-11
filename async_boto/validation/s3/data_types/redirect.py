from pydantic import BaseModel
from typing import Optional, Literal

class Redirect(BaseModel):
    """
    Specifies how requests are redirected. In the event of an error, you can specify
    a different error code to return.

    Attributes
    ----------
    HostName : Optional[str]
        The host name to use in the redirect request.
    HttpRedirectCode : Optional[str]
        The HTTP redirect code to use on the response.
    Protocol : Optional[Literal["http", "https"]]
        Protocol to use when redirecting requests.
    ReplaceKeyPrefixWith : Optional[str]
        The object key prefix to use in the redirect request.
    ReplaceKeyWith : Optional[str]
        The specific object key to use in the redirect request.
    """
    HostName: Optional[str] = None
    HttpRedirectCode: Optional[str] = None
    Protocol: Optional[Literal["http", "https"]] = None
    ReplaceKeyPrefixWith: Optional[str] = None
    ReplaceKeyWith: Optional[str] = None