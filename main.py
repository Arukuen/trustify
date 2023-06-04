from fastapi import FastAPI
from pydantic import BaseModel
import random
import model_api

class Text(BaseModel):
    data: str

app = FastAPI()

def faker_model(text: str) -> bool:
    random.seed(len(text))
    return random.randint(0, 10) >= 5

@app.get("/")
def is_alive():
    return {"is_alive": True}

@app.post("/api/text/")
async def process_text(text: Text):
    is_fake = model_api.predict(text.data)
    print(is_fake)
    response_data = {"is_fake": is_fake}
    return response_data