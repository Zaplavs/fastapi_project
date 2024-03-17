from typing import Annotated

from fastapi import Depends,APIRouter

from repository import TaskRepository
from schemas import STackAdd,STask, STaskId
router = APIRouter(
    prefix="/tasks",
    tags=["taski"]
)

@router.post("")
async def add_task(
    task: Annotated[STackAdd, Depends()],

) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return{"ok": True, "task_id": task_id}


@router.get("")
async def get_home() -> STask:
    tasks= await TaskRepository.find_all()
    return {"deta":tasks}