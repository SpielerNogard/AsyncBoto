from pydantic import BaseModel


class RequestProgress(BaseModel):
    """
    Container for specifying if periodic QueryProgress messages should be sent.

    Attributes
    ----------
    Enabled : Optional[bool]
        Specifies whether periodic QueryProgress frames should be sent.
        Valid values: TRUE, FALSE. Default value: FALSE.
    """

    Enabled: bool | None = False
