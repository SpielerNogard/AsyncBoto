from pydantic import BaseModel
from .input_serialization import InputSerialization
from .output_serialization import OutputSerialization

class SelectParameters(BaseModel):
    """
    Describes the parameters for Select job types.

    Attributes
    ----------
    Expression : str
        The expression that is used to query the object.
    ExpressionType : str
        The type of the provided expression (e.g., SQL).
    InputSerialization : InputSerialization
        Describes the serialization format of the object.
    OutputSerialization : OutputSerialization
        Describes how the results of the Select job are serialized.
    """
    Expression: str
    ExpressionType: str
    InputSerialization: InputSerialization
    OutputSerialization: OutputSerialization