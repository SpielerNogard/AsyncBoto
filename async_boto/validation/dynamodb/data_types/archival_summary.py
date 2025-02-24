from pydantic import BaseModel, Field
from typing import Optional

class ArchivalSummary(BaseModel):
    ArchivalBackupArn: Optional[str] = Field(None, min_length=37, max_length=1024)
    ArchivalDateTime: Optional[float] = None
    ArchivalReason: Optional[str] = None