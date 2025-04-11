from pydantic import BaseModel
from typing import Optional, Literal
from .bucket_info import BucketInfo
from .location_info import LocationInfo

class CreateBucketConfiguration(BaseModel):
    """
    The configuration information for the bucket.

    Attributes
    ----------
    Bucket : Optional[BucketInfo]
        Specifies the information about the bucket that will be created.
    Location : Optional[LocationInfo]
        Specifies the location where the bucket will be created.
    LocationConstraint : Optional[Literal[
        "af-south-1", "ap-east-1", "ap-northeast-1", "ap-northeast-2", "ap-northeast-3",
        "ap-south-1", "ap-south-2", "ap-southeast-1", "ap-southeast-2", "ap-southeast-3",
        "ap-southeast-4", "ap-southeast-5", "ca-central-1", "cn-north-1", "cn-northwest-1",
        "EU", "eu-central-1", "eu-central-2", "eu-north-1", "eu-south-1", "eu-south-2",
        "eu-west-1", "eu-west-2", "eu-west-3", "il-central-1", "me-central-1", "me-south-1",
        "sa-east-1", "us-east-2", "us-gov-east-1", "us-gov-west-1", "us-west-1", "us-west-2"
    ]]
        Specifies the Region where the bucket will be created.
    """
    Bucket: Optional[BucketInfo] = None
    Location: Optional[LocationInfo] = None
    LocationConstraint: Optional[Literal[
        "af-south-1", "ap-east-1", "ap-northeast-1", "ap-northeast-2", "ap-northeast-3",
        "ap-south-1", "ap-south-2", "ap-southeast-1", "ap-southeast-2", "ap-southeast-3",
        "ap-southeast-4", "ap-southeast-5", "ca-central-1", "cn-north-1", "cn-northwest-1",
        "EU", "eu-central-1", "eu-central-2", "eu-north-1", "eu-south-1", "eu-south-2",
        "eu-west-1", "eu-west-2", "eu-west-3", "il-central-1", "me-central-1", "me-south-1",
        "sa-east-1", "us-east-2", "us-gov-east-1", "us-gov-west-1", "us-west-1", "us-west-2"
    ]] = None