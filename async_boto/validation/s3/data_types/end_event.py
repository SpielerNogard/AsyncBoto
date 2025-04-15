from pydantic import BaseModel


class EndEvent(BaseModel):
    """
    A message that indicates the request is complete and no more messages will be sent.
    """

    pass
