from pydantic import BaseModel

class ClientData(BaseModel):
    age: int
    income: float
