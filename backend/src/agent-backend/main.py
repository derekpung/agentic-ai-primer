# backend.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Prompt(BaseModel):
    text: str


@app.post("/generate")
def generate(prompt: Prompt):
    # response = run_llm(prompt.text)
    response = f"You said '{prompt.text}'..."
    return {"response": response}
