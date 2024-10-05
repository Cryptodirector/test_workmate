from sqlalchemy import (
    select,
    extract, func
)
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.models.v1.cat_model import Cat, Breed
from app.schemas.v1.cat_schemas import (
    CatDTO
)

from app.schemas.v1.breed_schema import BreedDTO


class BreedService:

    @staticmethod
    async def get_breed(
            session: AsyncSession,
            skip: int = 0,
            limit: int = 10
    ) -> List[BreedDTO]:
        res = await session.execute(
            select(Breed).limit(limit).offset(skip)
        )

        model = res.scalars().all()
        return [
            BreedDTO.model_validate(row, from_attributes=True) for row in model
        ]

    @staticmethod
    async def get_cats_filter(
            id: int,
            session: AsyncSession,
            skip: int = 0,
            limit: int = 10
    ) -> List[CatDTO]:
        months_column = (
                (extract('year', func.now()) - extract('year', Cat.birthdate)
                 ) * 12).label('months_old')

        res = await session.execute(
            select(
                Cat.id,
                Cat.color,
                Cat.birthdate,
                Cat.descriptions,
                Cat.breed_id,
                Breed.id.label('breed_id'),
                Breed.title.label('breed_title'),
                months_column
            )
            .join(Breed, Breed.id == Cat.breed_id)
            .where(Cat.breed_id == id)
            .limit(limit)
            .offset(skip)
        )

        model = res.mappings().all()

        return [
            CatDTO(
                id=row["id"],
                color=row["color"],
                birthdate=row["birthdate"],
                descriptions=row["descriptions"],
                breed=BreedDTO(id=row["breed_id"], title=row["breed_title"]),
                months_old=row["months_old"],
                breed_id=row["breed_id"]
            ) for row in model
        ]