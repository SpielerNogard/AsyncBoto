from datetime import datetime

from pydantic import BaseModel


class SessionCredentials(BaseModel):
    """
    The established temporary security credentials of the session.

    Attributes
    ----------
    AccessKeyId : str
        A unique identifier associated with a secret access key.
    Expiration : datetime
        The expiration time of the temporary security credentials.
    SecretAccessKey : str
        A key used with the access key ID to sign AWS requests.
    SessionToken : str
        A token used to validate the temporary security credentials.
    """

    AccessKeyId: str
    Expiration: datetime
    SecretAccessKey: str
    SessionToken: str
