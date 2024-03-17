from typing import Optional
from pydantic import BaseModel
class STackAdd(BaseModel):
    name:str
    description: Optional[str] = None

class STask(STackAdd):
    id: int

class STaskId(BaseModel):
    ok: bool = True
    task_id: int