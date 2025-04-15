import datetime
import hashlib
import hmac
import urllib.parse
from typing import Any
from urllib.parse import urlparse

import boto3


def sign_request_aws_sigv4(
    session: boto3.Session,
    service: str,
    url: str,
    method: str,
    headers: dict[str, Any] = None,
    query: list[tuple[str, str]] = None,
    payload: str = None,
) -> dict[str, str]:
    """
    Sign an AWS request using Signature Version 4

    Parameters
    ----------
    session: boto3.Session
        The boto3 session to get credentials from
    service: str
        AWS service name (e.g., 's3', 'ec2')
    url: str
        Request URL
    method: str
        HTTP method (e.g., 'GET', 'POST')
    headers: dict[str, str]
        Optional headers to include in the request
    query: list[tuple[str, str]]
        Optional query parameters to include in the request
    payload: str
        Optional payload to include in the request

    Returns
    -------
    dict[str, str]
        Updated headers with Authorization and other AWS required
        headers
    """
    # Initialize default values
    headers = headers or {}
    query = query or []
    payload = payload or ""

    # Get credentials from boto3 session
    credentials = session.get_credentials()
    if not credentials:
        raise ValueError("No AWS credentials found in boto3 session")

    access_key = credentials.access_key
    secret_key = credentials.secret_key
    session_token = credentials.token  # For temporary credentials

    # Get region from boto3 session
    region = session.region_name
    if not region:
        raise ValueError("No AWS region found in boto3 session")

    # Create a copy of headers to work with
    headers_copy = {k.lower().strip(): str(v).strip() for k, v in headers.items()}

    # Add security token to headers BEFORE calculating signature
    if session_token:
        headers_copy["x-amz-security-token"] = session_token

    # Ensure required headers are present
    parsed_url = urlparse(url)
    if "host" not in headers_copy:
        headers_copy["host"] = parsed_url.netloc

    # Add x-amz-date header if not present
    now = datetime.datetime.utcnow()
    amz_date = now.strftime("%Y%m%dT%H%M%SZ")
    headers_copy["x-amz-date"] = amz_date

    # Get date for credential scope
    date_stamp = amz_date[:8]

    # Parse URL for canonical URI
    canonical_uri = urllib.parse.quote(
        parsed_url.path if parsed_url.path else "/", safe="/-_.~"
    )

    # Process query parameters
    canonical_query_items = []

    # First add any existing query parameters from the URL
    url_query_params = urllib.parse.parse_qs(parsed_url.query)
    for key in sorted(url_query_params.keys()):
        for value in sorted(url_query_params[key]):
            canonical_query_items.append(
                f"{urllib.parse.quote(key, safe='/-_.~')}={urllib.parse.quote(value, safe='/-_.~')}"  # noqa: E501
            )

    # Then add the query parameters passed as list of tuples
    for key, value in sorted(query, key=lambda x: x[0]):
        canonical_query_items.append(
            f"{urllib.parse.quote(str(key), safe='/-_.~')}={urllib.parse.quote(str(value), safe='/-_.~')}"  # noqa: E501
        )

    canonical_query_string = "&".join(canonical_query_items)

    # Create canonical headers string
    sorted_headers = sorted(headers_copy.keys())
    canonical_headers_string = "".join(
        f"{header}:{headers_copy[header]}\n" for header in sorted_headers
    )

    # Create signed headers string
    signed_headers = ";".join(sorted_headers)

    # Hash the payload
    if payload is None:
        payload = ""

    if isinstance(payload, str):
        payload_bytes = payload.encode("utf-8")
    else:
        payload_bytes = payload

    # For S3 with UNSIGNED-PAYLOAD
    if (
        service == "s3"
        and "x-amz-content-sha256" in headers_copy
        and headers_copy["x-amz-content-sha256"] == "UNSIGNED-PAYLOAD"
    ):
        payload_hash = "UNSIGNED-PAYLOAD"
    else:
        payload_hash = hashlib.sha256(payload_bytes).hexdigest()

    # Ensure x-amz-content-sha256 is set for S3
    if service == "s3" and "x-amz-content-sha256" not in headers_copy:
        headers_copy["x-amz-content-sha256"] = payload_hash
        sorted_headers = sorted(headers_copy.keys())
        canonical_headers_string = "".join(
            f"{header}:{headers_copy[header]}\n" for header in sorted_headers
        )
        signed_headers = ";".join(sorted_headers)

    # Create canonical request
    canonical_request = f"{method}\n{canonical_uri}\n{canonical_query_string}\n{canonical_headers_string}\n{signed_headers}\n{payload_hash}"  # noqa: E501

    # Create string to sign
    algorithm = "AWS4-HMAC-SHA256"
    credential_scope = f"{date_stamp}/{region}/{service}/aws4_request"
    canonical_request_hash = hashlib.sha256(
        canonical_request.encode("utf-8")
    ).hexdigest()
    string_to_sign = (
        f"{algorithm}\n{amz_date}\n{credential_scope}\n{canonical_request_hash}"
    )

    # Derive signing key
    def get_signature_key(key, date_stamp, region_name, service_name):
        k_date = hmac.new(
            f"AWS4{key}".encode(), date_stamp.encode("utf-8"), hashlib.sha256
        ).digest()
        k_region = hmac.new(
            k_date, region_name.encode("utf-8"), hashlib.sha256
        ).digest()
        k_service = hmac.new(
            k_region, service_name.encode("utf-8"), hashlib.sha256
        ).digest()
        k_signing = hmac.new(k_service, b"aws4_request", hashlib.sha256).digest()
        return k_signing

    # Calculate signature
    signing_key = get_signature_key(secret_key, date_stamp, region, service)
    signature = hmac.new(
        signing_key, string_to_sign.encode("utf-8"), hashlib.sha256
    ).hexdigest()

    # Create authorization header
    authorization_header = (
        f"{algorithm} "
        f"Credential={access_key}/{credential_scope}, "
        f"SignedHeaders={signed_headers}, "
        f"Signature={signature}"
    )

    # Create result headers
    result_headers = headers.copy()  # Start with original headers
    result_headers.update(
        {"Authorization": authorization_header, "x-amz-date": amz_date}
    )

    # Add security token to result headers
    if session_token:
        result_headers["x-amz-security-token"] = session_token

    # For S3, make sure content-sha256 is included in result headers
    if service == "s3" and "x-amz-content-sha256" in headers_copy:
        result_headers["x-amz-content-sha256"] = headers_copy["x-amz-content-sha256"]

    return result_headers


aws_sig_v4_headers = sign_request_aws_sigv4
