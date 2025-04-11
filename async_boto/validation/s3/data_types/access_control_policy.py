from typing import List
from .grant import Grant
from .owner import Owner
from typing import Optional
from typing import List
from pydantic import BaseModel

class AccessControlList(BaseModel):
    """
    Contains the elements that set the ACL permissions for an object per grantee.
    """
    Grants: Optional[List[Grant]]
    Owner: Optional[Owner]