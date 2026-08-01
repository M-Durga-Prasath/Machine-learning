from fastapi import FastAPI

from .models import ChatRequest, ChatResponse

app = FastAPI()


@app.post("/chat")

def chat(request: ChatRequest):

    return ChatResponse(

        answer="This is a fake response.",

        sources=[
            "Employee Handbook",
            "HR Policy"
        ],

        session_id=request.session_id
    )
