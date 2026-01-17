from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Prompt(BaseModel):
    text: str


@router.post("/chat")
def generate(prompt: Prompt):
    # response = run_llm(prompt.text)
    response = f"You said '{prompt.text}'..."
    return {"response": response}
