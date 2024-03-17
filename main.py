from typing import Annotated
from fastapi import Depends, FastAPI

from contextlib import asynccontextmanager

from datebase import create_tables, delete_tables
from schemas import STackAdd
from router import router as tasks_router
@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("clear")
    await create_tables()
    print("ready")
    yield
    print('close')


app = FastAPI(lifespan=lifespan)

app.include_router(tasks_router)




