from pydantic import BaseModel

from .continuation_event import ContinuationEvent
from .end_event import EndEvent
from .progress_event import ProgressEvent
from .records_event import RecordsEvent
from .stats_event import StatsEvent


class SelectObjectContentEventStream(BaseModel):
    """
    The container for selecting objects from a content event stream.

    Attributes
    ----------
    Cont : Optional[ContinuationEvent]
        The Continuation Event.
    End : Optional[EndEvent]
        The End Event.
    Progress : Optional[ProgressEvent]
        The Progress Event.
    Records : Optional[RecordsEvent]
        The Records Event.
    Stats : Optional[StatsEvent]
        The Stats Event.
    """

    Cont: ContinuationEvent | None
    End: EndEvent | None
    Progress: ProgressEvent | None
    Records: RecordsEvent | None
    Stats: StatsEvent | None
