from pydantic import BaseModel, Field
from typing import Optional, Annotated


class CatPost(BaseModel):
    color: str
    months_old: int = Field(
        le=12,
        ge=0
    )
    descriptions: str = Field(
        min_length=8,
        max_length=1000
    )
    id_breed: int


class CatUpdate(BaseModel):
    color: Optional[str] = None
    months_old: Annotated[
        int, Field(
            le=12,
            ge=0
        )
    ] = None
    descriptions: Annotated[
        str,
        Field(
            min_length=8,
            max_length=1000
        )
    ] = None
    id_breed: Optional[int] = None


class BreedDTO(BaseModel):
    id: int
    title: str


class CatsDTO(CatPost):
    id: int
    breed: 'BreedDTO'
