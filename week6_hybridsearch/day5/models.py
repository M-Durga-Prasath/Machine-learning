from pydantic import BaseModel, field_validator


class ChatRequest(BaseModel):

    session_id: str
    message: str

    @field_validator("message")
    @classmethod
    def validate_message(cls, value):

        if not value.strip():
            raise ValueError("Message cannot be empty.")

        if len(value) > 4000:
            raise ValueError("Message is too long.")

        return value


class ChatResponse(BaseModel):

    answer: str
    sources: list[str]
    session_id: str