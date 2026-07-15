from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model_loader import clf


class Predictions(BaseModel):
    text: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/test")
def hello():
    return {"message": "hello"}


@app.post("/predict")
def predict(request: Predictions):
    result = clf(request.text)[0]
    return {
        "text": request.text,
        "label": result["label"],
        "score": result["score"],
        "message": f"{result['label']} ({result['score']:.3f})",
    }
