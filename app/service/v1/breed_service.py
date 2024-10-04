from sqlalchemy import (
    select
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
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
        res = await session.execute(
            select(Cat).options(
                joinedload(Cat.breed)
            ).where(Cat.breed_id == id).limit(limit).offset(skip)
        )

        model = res.scalars().all()

        return [
            CatDTO.model_validate(row, from_attributes=True) for row in model
        ]
