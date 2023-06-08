from fastapi import FastAPI
from pydantic import BaseModel
import model_api

class Text(BaseModel):
    data: str

app = FastAPI()

# Route for Testing Purposes
@app.get("/")
def is_alive():
    return {"is_alive": True}

# Route for the actual API
@app.post("/api/text/")
async def process_text(text: Text):
    is_fake = model_api.predict(text.data) # call model_api.predict
    response_data = {"is_fake": is_fake[0],
                     "is_fake_svm": is_fake[1],
                     "is_fake_logistic_regression": is_fake[2]} # create response
    return response_data # respond to HTTP POST request