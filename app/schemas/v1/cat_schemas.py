from pydantic import BaseModel, Field
from typing import Annotated
from datetime import date

from app.schemas.v1.breed_schema import BreedDTO


class CreateCatSchema(BaseModel):
    color: str
    birthdate: date
    descriptions: str = Field(
        min_length=8,
        max_length=1000
    )
    breed_id: int


class CatUpdateSchema(BaseModel):
    color: str | None = None
    birthdate: Annotated[date, None]
    descriptions: Annotated[
        str,
        Field(
            min_length=8,
            max_length=1000
        ),
        None
    ]
    breed_id: int | None = None


class CatDTO(CreateCatSchema):
    id: int
    breed: 'BreedDTO'
    months_old: int
