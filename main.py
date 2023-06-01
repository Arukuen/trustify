from fastapi import FastAPI
from pydantic import BaseModel
import random

class Text(BaseModel):
    data: str

app = FastAPI()

def faker_model(text: str) -> bool:
    random.seed(len(text))
    return random.randint(0, 10) >= 5

@app.get("/")
def is_alive():
    return {"is_alive": True}

@app.post("/text")
async def process_text(text: Text):
    is_fake = faker_model(text.data)
    response_data = {'fake': is_fake}
    return response_data