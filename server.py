from fastapi import FastAPI
from pydantic import BaseModel
from app.model_handler import generate_hint, generate_follow_up

app = FastAPI()

class CodeInput(BaseModel):
    code: str
    task_description: str
    is_completed: bool

@app.post("/hint/")
async def get_hint(data: CodeInput):
    hint = generate_hint(data.code, data.task_description)
    return {"hint": hint}

@app.post("/followup/")
async def get_follow_up(data: CodeInput):
    if data.is_completed:
        follow_up = generate_follow_up(data.task_description)
        return {"follow_up_question": follow_up}
    return {"follow_up_question": None}
