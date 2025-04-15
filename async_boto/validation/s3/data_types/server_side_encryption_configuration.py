from pydantic import BaseModel

from .server_side_encryption_rule import ServerSideEncryptionRule


class ServerSideEncryptionConfiguration(BaseModel):
    """
    Specifies the default server-side-encryption configuration.

    Attributes
    ----------
    Rules : List[ServerSideEncryptionRule]
        Container for information about a particular server-side encryption
        configuration rule.
    """

    Rules: list[ServerSideEncryptionRule]
