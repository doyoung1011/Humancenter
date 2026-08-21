from pydantic import BaseModel,Field


class Todo(BaseModel):
    id:int
    item:str=''