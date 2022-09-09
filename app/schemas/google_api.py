from pydantic import BaseModel


class GoogleApiSchema(BaseModel):
    name: str
    completion: float
    description: str
