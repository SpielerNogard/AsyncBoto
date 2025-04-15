import logging
from datetime import datetime
from typing import TypeVar

import boto3
from pydantic import BaseModel

from async_boto.core.base_client import BaseClient
from async_boto.core.session import AsyncAWSSession
from async_boto.validation.s3.get_object import GetObjectRequest, GetObjectResponse

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)


class AsyncS3Client(BaseClient):
    def __init__(self, aws_session: boto3.Session | AsyncAWSSession):
        super().__init__(aws_session=aws_session, service_name="s3")

    def _get_url(self, bucket_name: str, key: str = None):
        if key.startswith("/"):
            key = key[1:]

        return (
            f"https://{bucket_name}.s3.amazonaws.com/{key}"
            if key
            else f"https://{bucket_name}.s3.amazonaws.com"
        )

    async def get_object(self, request: GetObjectRequest) -> GetObjectResponse:
        """
        Retrieves objects from Amazon S3.
        """
        url = self._get_url(request.Bucket, key=request.Key)

        headers = {
            "If-Match": request.IfMatch,
            "If-Modified-Since": request.IfModifiedSince,
            "If-None-Match": request.IfNoneMatch,
            "If-Unmodified-Since": request.IfUnmodifiedSince,
            "Range": request.Range,
            "x-amz-server-side-encryption-customer-algorithm": request.XAmzServerSideEncryptionCustomerAlgorithm,  # noqa: E501
            "x-amz-server-side-encryption-customer-key": request.XAmzServerSideEncryptionCustomerKey,  # noqa: E501
            "x-amz-server-side-encryption-customer-key-MD5": request.XAmzServerSideEncryptionCustomerKeyMD5,  # noqa: E501
            "x-amz-request-payer": request.XAmzRequestPayer,
            "x-amz-expected-bucket-owner": request.XAmzExpectedBucketOwner,
            "x-amz-checksum-mode": request.XAmzChecksumMode,
        }
        # Remove None values from headers
        headers = {k: v for k, v in headers.items() if v is not None}
        headers["x-amz-content-sha256"] = "UNSIGNED-PAYLOAD"
        params = {
            "partNumber": request.PartNumber,
            "response-cache-control": request.ResponseCacheControl,
            "response-content-disposition": request.ResponseContentDisposition,
            "response-content-encoding": request.ResponseContentEncoding,
            "response-content-language": request.ResponseContentLanguage,
            "response-content-type": request.ResponseContentType,
            "response-expires": request.ResponseExpires,
            "versionId": request.VersionId,
        }
        # Remove None values from params
        params = {k: v for k, v in params.items() if v is not None}

        response = await self._get(url, headers=headers, params=params, json={})
        headers = response.headers
        body = response.content

        # Map headers to GetObjectResponse attributes
        return GetObjectResponse(
            AcceptRanges=headers.get("accept-ranges"),
            CacheControl=headers.get("Cache-Control"),
            ContentDisposition=headers.get("Content-Disposition"),
            ContentEncoding=headers.get("Content-Encoding"),
            ContentLanguage=headers.get("Content-Language"),
            ContentLength=int(headers.get("Content-Length", 0)),
            ContentRange=headers.get("Content-Range"),
            ContentType=headers.get("Content-Type"),
            ETag=headers.get("ETag"),
            Expires=datetime.strptime(headers["Expires"], "%a, %d %b %Y %H:%M:%S %Z")
            if "Expires" in headers
            else None,
            LastModified=datetime.strptime(
                headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z"
            )
            if "Last-Modified" in headers
            else None,
            XAmzChecksumCRC32=headers.get("x-amz-checksum-crc32"),
            XAmzChecksumCRC32C=headers.get("x-amz-checksum-crc32c"),
            XAmzChecksumCRC64NVME=headers.get("x-amz-checksum-crc64nvme"),
            XAmzChecksumSHA1=headers.get("x-amz-checksum-sha1"),
            XAmzChecksumSHA256=headers.get("x-amz-checksum-sha256"),
            XAmzChecksumType=headers.get("x-amz-checksum-type"),
            XAmzDeleteMarker=headers.get("x-amz-delete-marker") == "true",
            XAmzExpiration=headers.get("x-amz-expiration"),
            XAmzMissingMeta=int(headers.get("x-amz-missing-meta", 0))
            if "x-amz-missing-meta" in headers
            else None,
            XAmzMpPartsCount=int(headers.get("x-amz-mp-parts-count", 0))
            if "x-amz-mp-parts-count" in headers
            else None,
            XAmzObjectLockLegalHold=headers.get("x-amz-object-lock-legal-hold"),
            XAmzObjectLockMode=headers.get("x-amz-object-lock-mode"),
            XAmzObjectLockRetainUntilDate=datetime.strptime(
                headers["x-amz-object-lock-retain-until-date"], "%Y-%m-%dT%H:%M:%S.%fZ"
            )
            if "x-amz-object-lock-retain-until-date" in headers
            else None,
            XAmzReplicationStatus=headers.get("x-amz-replication-status"),
            XAmzRequestCharged=headers.get("x-amz-request-charged"),
            XAmzRestore=headers.get("x-amz-restore"),
            XAmzServerSideEncryption=headers.get("x-amz-server-side-encryption"),
            XAmzServerSideEncryptionAwsKmsKeyId=headers.get(
                "x-amz-server-side-encryption-aws-kms-key-id"
            ),
            XAmzServerSideEncryptionBucketKeyEnabled=headers.get(
                "x-amz-server-side-encryption-bucket-key-enabled"
            )
            == "true",
            XAmzServerSideEncryptionCustomerAlgorithm=headers.get(
                "x-amz-server-side-encryption-customer-algorithm"
            ),
            XAmzServerSideEncryptionCustomerKeyMD5=headers.get(
                "x-amz-server-side-encryption-customer-key-MD5"
            ),
            XAmzStorageClass=headers.get("x-amz-storage-class"),
            XAmzTaggingCount=int(headers.get("x-amz-tagging-count", 0))
            if "x-amz-tagging-count" in headers
            else None,
            XAmzVersionId=headers.get("x-amz-version-id"),
            XAmzWebsiteRedirectLocation=headers.get("x-amz-website-redirect-location"),
            Content=body,
        )
