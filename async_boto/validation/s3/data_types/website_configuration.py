from pydantic import BaseModel, root_validator

from .error_document import ErrorDocument
from .index_document import IndexDocument
from .redirect_all_requests_to import RedirectAllRequestsTo
from .routing_rule import RoutingRule


class WebsiteConfiguration(BaseModel):
    """
    Specifies website configuration parameters for an Amazon S3 bucket.

    Attributes
    ----------
    ErrorDocument : Optional[ErrorDocument]
        The name of the error document for the website.
    IndexDocument : Optional[IndexDocument]
        The name of the index document for the website.
    RedirectAllRequestsTo : Optional[RedirectAllRequestsTo]
        The redirect behavior for every request to this bucket's website endpoint.
    RoutingRules : Optional[List[RoutingRule]]
        Rules that define when a redirect is applied and the redirect behavior.
    """

    ErrorDocument: ErrorDocument | None
    IndexDocument: IndexDocument | None
    RedirectAllRequestsTo: RedirectAllRequestsTo | None
    RoutingRules: list[RoutingRule] | None

    @root_validator
    def validate_redirect_all_requests_to(cls, values):
        if values.get("RedirectAllRequestsTo") is not None:
            if any(
                values.get(field) is not None
                for field in ["ErrorDocument", "IndexDocument", "RoutingRules"]
            ):
                raise ValueError(
                    "If RedirectAllRequestsTo is specified, no other property can "
                    "be set."
                )
        return values
