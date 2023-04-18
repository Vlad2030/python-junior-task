from pydantic import BaseModel


class Pets(BaseModel):
    name: str
    age: int
    type: str
    types: list = [
        "cat",
        "dog",
    ]