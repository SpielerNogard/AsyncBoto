from pydantic import BaseModel

from .stats import Stats


class StatsEvent(BaseModel):
    """
    Container for the Stats Event.

    Attributes
    ----------
    Details : Optional[Stats]
        The Stats event details.
    """

    Details: Stats | None
