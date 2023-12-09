from pydantic import BaseModel

class ProdPyd(BaseModel):
    name: str
    description: str
    value: float

class ProdVarPyd(BaseModel):
    model: str
    color: str
    size: str