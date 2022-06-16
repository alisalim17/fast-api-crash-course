from ctypes import Union
from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hi this is route named 'index'"}



class CreatePostInput(BaseModel):
    name: str
    published:bool = True
    rating:Optional[int | str]


@app.post("/create-post")
async def create_post(payload:CreatePostInput):
    print(payload)
    return {"message": f"Hi,my name is {payload.name}"}
