from pydantic import BaseModel, Field

from .metrics_filter import MetricsFilter


class MetricsConfiguration(BaseModel):
    """
    Specifies a metrics configuration for the CloudWatch request metrics from an Amazon
    S3 bucket.

    Attributes
    ----------
    Id : str
        The ID used to identify the metrics configuration. The ID has a 64 character
        limit and can only
        contain letters, numbers, periods, dashes, and underscores.
    Filter : Optional[MetricsFilter]
        Specifies a metrics configuration filter. The metrics configuration will only
        include objects
        that meet the filter's criteria. A filter must be a prefix, an object tag, an
        access point ARN,
        or a conjunction (MetricsAndOperator).
    """

    Id: str = Field(..., max_length=64, pattern=r"^[a-zA-Z0-9._-]+$")
    Filter: MetricsFilter | None = None
