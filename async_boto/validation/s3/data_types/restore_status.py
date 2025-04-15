from datetime import datetime

from pydantic import BaseModel


class RestoreStatus(BaseModel):
    """
    Specifies the restoration status of an object. Objects in certain storage classes
    must be restored before they can be retrieved.

    Attributes
    ----------
    IsRestoreInProgress : Optional[bool]
        Specifies whether the object is currently being restored.
    RestoreExpiryDate : Optional[datetime]
        Indicates when the restored copy will expire.
    """

    IsRestoreInProgress: bool | None
    RestoreExpiryDate: datetime | None
