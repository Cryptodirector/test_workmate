from fastapi import HTTPException
from starlette.status import (
    HTTP_404_NOT_FOUND,
    HTTP_204_NO_CONTENT
)
from sqlalchemy import (
    select,
    insert,
    update,
    delete
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from typing import List
from app.models.v1.cat_model import Cat
from app.schemas.v1.cat_schemas import (
    CreateCatSchema,
    CatUpdateSchema,
    CatDTO
)


class CatService:

    @staticmethod
    async def insert_cat(
            body: CreateCatSchema,
            session: AsyncSession
    ) -> CreateCatSchema:
        await session.execute(
            insert(Cat).values(body.model_dump())
        )
        await session.commit()
        return body

    @staticmethod
    async def update_cat(
            id: int,
            body: CatUpdateSchema,
            session: AsyncSession
    ) -> CatUpdateSchema:

        cat = await session.execute(
            update(Cat).values(
                body.model_dump()
            ).where(Cat.id == id).returning(Cat.id)
        )

        if cat.scalar() is None:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND,
                detail="Cat not found"
            )
        await session.commit()
        return body

    @staticmethod
    async def delete_cat(
        id: int,
        session: AsyncSession
    ) -> None:

        await session.execute(
            delete(Cat).where(Cat.id == id)
        )
        await session.commit()
        raise HTTPException(
            status_code=HTTP_204_NO_CONTENT
        )

    @staticmethod
    async def get_cats(
        session: AsyncSession,
        skip: int = 0,
        limit: int = 10,
    ) -> List[CatDTO]:
        res = await session.execute(
            select(Cat).options(
                joinedload(Cat.breed)
            ).limit(limit).offset(skip)
        )

        model = res.scalars().all()

        return [
            CatDTO.model_validate(row, from_attributes=True) for row in model
        ]

    @staticmethod
    async def get_cat_by_id(
        id: int,
        session: AsyncSession
    ) -> List[CatDTO]:
        res = await session.execute(
            select(Cat).options(
                joinedload(Cat.breed)
            ).where(Cat.id == id)
        )

        model = res.scalars().all()

        return [
            CatDTO.model_validate(row, from_attributes=True) for row in model
        ]
