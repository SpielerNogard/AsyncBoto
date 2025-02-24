from pydantic import BaseModel, constr
from typing import Optional

class DeleteResourcePolicyRequest(BaseModel):
    """
    Deletes the resource-based policy attached to the resource, which can be a table or stream.

    Attributes
    ----------
    ResourceArn : str
        The Amazon Resource Name (ARN) of the DynamoDB resource from which the policy will be removed.
    ExpectedRevisionId : Optional[str]
        A string value that you can use to conditionally delete your policy.
    """
    ResourceArn: constr(min_length=1, max_length=1283)
    ExpectedRevisionId: Optional[constr(min_length=1, max_length=255)] = None


class DeleteResourcePolicyResponse(BaseModel):
    """
    Response for the DeleteResourcePolicy operation.

    Attributes
    ----------
    RevisionId : str
        A unique string that represents the revision ID of the policy.
    """
    RevisionId: Optional[constr(min_length=1, max_length=255)] = None