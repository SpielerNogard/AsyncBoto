from typing import Literal

from pydantic import BaseModel

from .encryption import Encryption
from .grant import Grant
from .metadata_entry import MetadataEntry
from .tagging import Tagging


class S3Location(BaseModel):
    """
    Describes an Amazon S3 location that will receive the results of the restore request.

    Attributes
    ----------
    BucketName : str
        The name of the bucket where the restore results will be placed.
    Prefix : str
        The prefix that is prepended to the restore results for this request.
    AccessControlList : Optional[List[Grant]]
        A list of grants that control access to the staged results.
    CannedACL : Optional[Literal["private", "public-read", "public-read-write", "authenticated-read",
                                 "aws-exec-read", "bucket-owner-read", "bucket-owner-full-control"]]
        The canned ACL to apply to the restore results.
    Encryption : Optional[Encryption]
        Contains the type of server-side encryption used.
    StorageClass : Optional[Literal["STANDARD", "REDUCED_REDUNDANCY", "STANDARD_IA", "ONEZONE_IA",
                                    "INTELLIGENT_TIERING", "GLACIER", "DEEP_ARCHIVE", "OUTPOSTS",
                                    "GLACIER_IR", "SNOW", "EXPRESS_ONEZONE"]]
        The class of storage used to store the restore results.
    Tagging : Optional[Tagging]
        The tag-set that is applied to the restore results.
    UserMetadata : Optional[List[MetadataEntry]]
        A list of metadata to store with the restore results in S3.
    """  # noqa: E501

    BucketName: str
    Prefix: str
    AccessControlList: list[Grant] | None
    CannedACL: (
        Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ]
        | None
    )
    Encryption: Encryption | None
    StorageClass: (
        Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
            "OUTPOSTS",
            "GLACIER_IR",
            "SNOW",
            "EXPRESS_ONEZONE",
        ]
        | None
    )
    Tagging: Tagging | None
    UserMetadata: list[MetadataEntry] | None
