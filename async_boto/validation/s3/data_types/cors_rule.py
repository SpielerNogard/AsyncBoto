from pydantic import BaseModel


class CORSRule(BaseModel):
    """
    Specifies a cross-origin access rule for an Amazon S3 bucket.

    Attributes
    ----------
    AllowedMethods : List[str]
        An HTTP method that you allow the origin to execute. Valid values are
        GET, PUT, HEAD, POST, and DELETE.
    AllowedOrigins : List[str]
        One or more origins you want customers to be able to access the bucket from.
    AllowedHeaders : Optional[List[str]]
        Headers allowed in a preflight OPTIONS request.
    ExposeHeaders : Optional[List[str]]
        Headers in the response that you want customers to access.
    ID : Optional[str]
        Unique identifier for the rule (max 255 characters).
    MaxAgeSeconds : Optional[int]
        Time in seconds for caching the preflight response.
    """

    AllowedMethods: list[str]
    AllowedOrigins: list[str]
    AllowedHeaders: list[str] | None = None
    ExposeHeaders: list[str] | None = None
    ID: str | None = None
    MaxAgeSeconds: int | None = None
