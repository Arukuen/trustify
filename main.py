from fastapi import FastAPI
from pydantic import BaseModel
import model_api

class Text(BaseModel):
    data: str

app = FastAPI()


@app.get("/")
def is_alive():
    return {"is_alive": True}

@app.post("/api/text/")
async def process_text(text: Text):
    is_fake = model_api.predict(text.data)
    response_data = {"is_fake": is_fake}
    return response_data