from pydantic import BaseModel

class RequestModel(BaseModel):
    customer_message: str
    tone: str = "Professional"
    length: str = "Medium"

class ResponseModel(BaseModel):
    response: str