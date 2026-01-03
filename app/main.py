""" Main Module """

from contextlib import asynccontextmanager
import asyncpg
from fastapi import FastAPI


async def db_connection_manager():
    return asyncpg.connect(
        host="",
        password="",
        database="",
        user=""
    )

@asynccontextmanager
async def lifespan_event(app: FastAPI):
    print("App Started ")
    yield
    print("Add Shutdown")


# FastApi Instance Creation
app = FastAPI(lifespan=lifespan_event)




@app.get("/")
async def home():
    return {
      "data" : "Hello WOrld"  
    } 