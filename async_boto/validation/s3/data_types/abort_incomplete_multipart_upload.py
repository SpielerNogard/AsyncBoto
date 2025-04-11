from pydantic import BaseModel, conint

class AbortIncompleteMultipartUpload(BaseModel):
    """
    Specifies the days since the initiation of an incomplete multipart upload
    that Amazon S3 will wait before permanently removing all parts of the upload.
    """
    DaysAfterInitiation: conint(ge=1) = None