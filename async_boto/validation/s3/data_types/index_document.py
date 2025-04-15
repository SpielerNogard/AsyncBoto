from pydantic import BaseModel, constr


class IndexDocument(BaseModel):
    """
    Container for the Suffix element.

    Attributes
    ----------
    Suffix : str
        A suffix that is appended to a request for a directory on the website endpoint.
        The suffix must not be empty and must not include a slash character.
    """

    Suffix: constr(min_length=1)
