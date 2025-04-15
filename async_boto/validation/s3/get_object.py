from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class GetObjectRequest(BaseModel):
    """
    Represents the request parameters for the GetObject operation in Amazon S3.

    Attributes
    ----------
    Bucket : str
        The bucket name containing the object.
    Key : str
        Key of the object to get.
    IfMatch : Optional[str]
        Return the object only if its ETag matches the specified value.
    IfModifiedSince : Optional[datetime]
        Return the object only if it has been modified since the specified time.
    IfNoneMatch : Optional[str]
        Return the object only if its ETag is different from the specified value.
    IfUnmodifiedSince : Optional[datetime]
        Return the object only if it has not been modified since the specified time.
    PartNumber : Optional[int]
        Part number of the object being read.
    Range : Optional[str]
        Downloads the specified byte range of an object.
    ResponseCacheControl : Optional[str]
        Sets the Cache-Control header of the response.
    ResponseContentDisposition : Optional[str]
        Sets the Content-Disposition header of the response.
    ResponseContentEncoding : Optional[str]
        Sets the Content-Encoding header of the response.
    ResponseContentLanguage : Optional[str]
        Sets the Content-Language header of the response.
    ResponseContentType : Optional[str]
        Sets the Content-Type header of the response.
    ResponseExpires : Optional[datetime]
        Sets the Expires header of the response.
    VersionId : Optional[str]
        Version ID used to reference a specific version of the object.
    XAmzChecksumMode : Optional[Literal["ENABLED"]]
        To retrieve the checksum, this mode must be enabled.
    XAmzExpectedBucketOwner : Optional[str]
        The account ID of the expected bucket owner.
    XAmzRequestPayer : Optional[Literal["requester"]]
        Confirms that the requester knows they will be charged for the request.
    XAmzServerSideEncryptionCustomerAlgorithm : Optional[str]
        Specifies the algorithm to use when decrypting the object.
    XAmzServerSideEncryptionCustomerKey : Optional[str]
        Specifies the customer-provided encryption key.
    XAmzServerSideEncryptionCustomerKeyMD5 : Optional[str]
        Specifies the MD5 digest of the customer-provided encryption key.
    """

    Bucket: str = Field(..., min_length=1)
    Key: str = Field(..., min_length=1)
    IfMatch: str | None = None
    IfModifiedSince: datetime | None = None
    IfNoneMatch: str | None = None
    IfUnmodifiedSince: datetime | None = None
    PartNumber: int | None = Field(None, ge=1, le=10000)
    Range: str | None = None
    ResponseCacheControl: str | None = None
    ResponseContentDisposition: str | None = None
    ResponseContentEncoding: str | None = None
    ResponseContentLanguage: str | None = None
    ResponseContentType: str | None = None
    ResponseExpires: datetime | None = None
    VersionId: str | None = None
    XAmzChecksumMode: Literal["ENABLED"] | None = None
    XAmzExpectedBucketOwner: str | None = None
    XAmzRequestPayer: Literal["requester"] | None = None
    XAmzServerSideEncryptionCustomerAlgorithm: str | None = None
    XAmzServerSideEncryptionCustomerKey: str | None = None
    XAmzServerSideEncryptionCustomerKeyMD5: str | None = None


class GetObjectResponse(BaseModel):
    """
    Represents the response elements for the GetObject operation in Amazon S3.

    Attributes
    ----------
    AcceptRanges : Optional[str]
        Indicates that a range of bytes was specified in the request.
    CacheControl : Optional[str]
        Specifies caching behavior along the request/reply chain.
    ContentDisposition : Optional[str]
        Specifies presentational information for the object.
    ContentEncoding : Optional[str]
        Indicates what content encodings have been applied to the object.
    ContentLanguage : Optional[str]
        The language the content is in.
    ContentLength : Optional[int]
        Size of the body in bytes.
    ContentRange : Optional[str]
        The portion of the object returned in the response.
    ContentType : Optional[str]
        A standard MIME type describing the format of the object data.
    ETag : Optional[str]
        An entity tag (ETag) assigned by the web server.
    Expires : Optional[datetime]
        The date and time at which the object is no longer cacheable.
    LastModified : Optional[datetime]
        Date and time when the object was last modified.
    XAmzChecksumCRC32 : Optional[str]
        The Base64 encoded, 32-bit CRC32 checksum of the object.
    XAmzChecksumCRC32C : Optional[str]
        The Base64 encoded, 32-bit CRC32C checksum of the object.
    XAmzChecksumCRC64NVME : Optional[str]
        The Base64 encoded, 64-bit CRC64NVME checksum of the object.
    XAmzChecksumSHA1 : Optional[str]
        The Base64 encoded, 160-bit SHA1 digest of the object.
    XAmzChecksumSHA256 : Optional[str]
        The Base64 encoded, 256-bit SHA256 digest of the object.
    XAmzChecksumType : Optional[Literal["COMPOSITE", "FULL_OBJECT"]]
        The checksum type for multipart objects.
    XAmzDeleteMarker : Optional[bool]
        Indicates whether the object retrieved was a Delete Marker.
    XAmzExpiration : Optional[str]
        Object expiration information.
    XAmzMissingMeta : Optional[int]
        The number of metadata entries not returned in the headers.
    XAmzMpPartsCount : Optional[int]
        The count of parts this object has.
    XAmzObjectLockLegalHold : Optional[Literal["ON", "OFF"]]
        Indicates whether this object has an active legal hold.
    XAmzObjectLockMode : Optional[Literal["GOVERNANCE", "COMPLIANCE"]]
        The Object Lock mode in place for this object.
    XAmzObjectLockRetainUntilDate : Optional[datetime]
        The date and time when this object's Object Lock will expire.
    XAmzReplicationStatus : Optional[Literal["COMPLETE", "PENDING", "FAILED", "REPLICA", "COMPLETED"]]
        Replication status of the object.
    XAmzRequestCharged : Optional[Literal["requester"]]
        Indicates that the requester was successfully charged for the request.
    XAmzRestore : Optional[str]
        Provides information about object restoration action and expiration time.
    XAmzServerSideEncryption : Optional[Literal["AES256", "aws:kms", "aws:kms:dsse"]]
        The server-side encryption algorithm used.
    XAmzServerSideEncryptionAwsKmsKeyId : Optional[str]
        The ID of the KMS key used for object encryption.
    XAmzServerSideEncryptionBucketKeyEnabled : Optional[bool]
        Indicates whether the object uses an S3 Bucket Key for SSE-KMS.
    XAmzServerSideEncryptionCustomerAlgorithm : Optional[str]
        The encryption algorithm used for SSE-C.
    XAmzServerSideEncryptionCustomerKeyMD5 : Optional[str]
        The MD5 digest of the customer-provided encryption key.
    XAmzStorageClass : Optional[Literal["STANDARD", "REDUCED_REDUNDANCY", "STANDARD_IA", "ONEZONE_IA", "INTELLIGENT_TIERING", "GLACIER", "DEEP_ARCHIVE", "OUTPOSTS", "GLACIER_IR", "SNOW", "EXPRESS_ONEZONE"]]
        Storage class information of the object.
    XAmzTaggingCount : Optional[int]
        The number of tags on the object.
    XAmzVersionId : Optional[str]
        Version ID of the object.
    XAmzWebsiteRedirectLocation : Optional[str]
        Redirects requests for this object to another object or URL.
    """  # noqa: E501

    AcceptRanges: str | None = None
    CacheControl: str | None = None
    ContentDisposition: str | None = None
    ContentEncoding: str | None = None
    ContentLanguage: str | None = None
    ContentLength: int | None = None
    ContentRange: str | None = None
    ContentType: str | None = None
    ETag: str | None = None
    Expires: datetime | None = None
    LastModified: datetime | None = None
    XAmzChecksumCRC32: str | None = None
    XAmzChecksumCRC32C: str | None = None
    XAmzChecksumCRC64NVME: str | None = None
    XAmzChecksumSHA1: str | None = None
    XAmzChecksumSHA256: str | None = None
    XAmzChecksumType: Literal["COMPOSITE", "FULL_OBJECT"] | None = None
    XAmzDeleteMarker: bool | None = None
    XAmzExpiration: str | None = None
    XAmzMissingMeta: int | None = None
    XAmzMpPartsCount: int | None = None
    XAmzObjectLockLegalHold: Literal["ON", "OFF"] | None = None
    XAmzObjectLockMode: Literal["GOVERNANCE", "COMPLIANCE"] | None = None
    XAmzObjectLockRetainUntilDate: datetime | None = None
    XAmzReplicationStatus: (
        Literal["COMPLETE", "PENDING", "FAILED", "REPLICA", "COMPLETED"] | None
    ) = None
    XAmzRequestCharged: Literal["requester"] | None = None
    XAmzRestore: str | None = None
    XAmzServerSideEncryption: Literal["AES256", "aws:kms", "aws:kms:dsse"] | None = None
    XAmzServerSideEncryptionAwsKmsKeyId: str | None = None
    XAmzServerSideEncryptionBucketKeyEnabled: bool | None = None
    XAmzServerSideEncryptionCustomerAlgorithm: str | None = None
    XAmzServerSideEncryptionCustomerKeyMD5: str | None = None
    XAmzStorageClass: (
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
    ) = None
    XAmzTaggingCount: int | None = None
    XAmzVersionId: str | None = None
    XAmzWebsiteRedirectLocation: str | None = None
    Content: bytes | None = None
