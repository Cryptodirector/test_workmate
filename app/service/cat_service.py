from fastapi import HTTPException
from sqlalchemy import (
    select,
    insert,
    update,
    delete
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from typing import List
from app.models.cat_model import Cats, Breed
from app.schemas.cat_schemas import (
    CatPost,
    CatUpdate,
    BreedDTO,
    CatsDTO
)


class CatService:

    @staticmethod
    async def insert_cat(
            body: CatPost,
            session: AsyncSession
    ) -> CatPost:
        await session.execute(
            insert(Cats).values(body.model_dump())
        )
        await session.commit()
        return body

    @staticmethod
    async def update(
            id: int,
            body: CatUpdate,
            session: AsyncSession
    ) -> CatUpdate:

        result = await session.execute(
            select(Cats).where(Cats.id == id)
        )
        cat = result.scalar_one_or_none()

        if cat is None:
            raise HTTPException(
                status_code=404,
                detail="Cat not found"
            )

        await session.execute(
            update(Cats).values(body.model_dump()).where(Cats.id == id)
        )
        await session.commit()
        return body

    @staticmethod
    async def delete(
        id: int,
        session: AsyncSession
    ) -> None:

        result = await session.execute(
            select(Cats).where(Cats.id == id)
        )
        cat = result.scalar_one_or_none()

        if cat is None:
            raise HTTPException(
                status_code=404,
                detail="Cat not found"
            )

        await session.execute(
            delete(Cats).where(Cats.id == id)
        )

        await session.commit()

    @staticmethod
    async def get_breed(
        session: AsyncSession
    ):
        res = await session.execute(
            select(Breed)
        )

        model = res.scalars().all()
        return [
            BreedDTO.model_validate(row, from_attributes=True) for row in model
        ]

    @staticmethod
    async def get_cats(
        session: AsyncSession
    ) -> List[CatsDTO]:
        res = await session.execute(
            select(Cats).options(joinedload(Cats.breed))
        )

        model = res.scalars().all()

        return [
            CatsDTO.model_validate(row, from_attributes=True) for row in model
        ]

    @staticmethod
    async def get_cat_by_id(
        id: int,
        session: AsyncSession
    ) -> List[CatsDTO]:
        res = await session.execute(
            select(Cats).options(
                joinedload(Cats.breed)
            ).where(Cats.id == id)
        )

        model = res.scalars().all()

        return [
            CatsDTO.model_validate(row, from_attributes=True) for row in model
        ]

    @staticmethod
    async def get_cats_filter(
        id: int,
        session: AsyncSession
    ) -> List[CatsDTO]:
        res = await session.execute(
            select(Cats).options(
                joinedload(Cats.breed)
            ).where(Cats.id_breed == id)
        )

        model = res.scalars().all()

        return [
            CatsDTO.model_validate(row, from_attributes=True) for row in model
        ]