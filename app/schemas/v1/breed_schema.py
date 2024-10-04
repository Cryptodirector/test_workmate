from pydantic import BaseModel


class BreedDTO(BaseModel):
    id: int
    title: str
