from pydantic import BaseModel

from .progress import Progress


class ProgressEvent(BaseModel):
    """
    This data type contains information about the progress event of an operation.

    Attributes
    ----------
    Details : Optional[Progress]
        The Progress event details.
    """

    Details: Progress | None = None
