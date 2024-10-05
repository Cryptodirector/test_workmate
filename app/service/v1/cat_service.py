from fastapi import HTTPException
from starlette.status import (
    HTTP_404_NOT_FOUND,
    HTTP_204_NO_CONTENT
)
from sqlalchemy import (
    extract,
    func,
    insert,
    update,
    delete,
    select
)

from app.schemas.v1.cat_schemas import (
    CreateCatSchema,
    CatUpdateSchema,
    CatDTO
)

from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.models.v1.cat_model import Cat, Breed

from app.schemas.v1.breed_schema import BreedDTO


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

    @staticmethod
    async def get_cat_by_id(
        id: int,
        session: AsyncSession
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
            .where(Cat.id == id)
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
