from fastapi import (
    APIRouter,
    Depends
)
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
from app.schemas.v1.cat_schemas import (
    CreateCatSchema,
    CatUpdateSchema,
    CatDTO
)
from app.service.v1.cat_service import CatService
from typing import List

router = APIRouter(
    prefix='/api/v1',
    tags=['Cat']
)


# Добавление котенка

@router.post(
    '/cats/create',
    response_model=CreateCatSchema
)
async def create_cat(
    body: CreateCatSchema,
    session: AsyncSession = Depends(get_async_session)
) -> CreateCatSchema:
    return await CatService.insert_cat(
        body=body,
        session=session
    )


# Изменение информации о котенке


@router.patch(
    '/cats/update/{id}',
    response_model=CatUpdateSchema
)
async def update_cat(
    id: int,
    body: CatUpdateSchema,
    session: AsyncSession = Depends(get_async_session)
) -> CatUpdateSchema:
    return await CatService.update_cat(
        id=id,
        body=body,
        session=session
    )


# Удаление информации о котенке


@router.delete('/cats/delete/{id}')
async def delete_cat(
    id: int,
    session: AsyncSession = Depends(get_async_session)
) -> None:
    return await CatService.delete_cat(
        id=id,
        session=session
    )


# Получение списка всех котят


@router.get(
    '/cats',
    response_model=List[CatDTO]
)
async def get_cats(
    skip: int = 0,
    limit: int = 10,
    session: AsyncSession = Depends(get_async_session)
) -> List[CatDTO]:
    return await CatService.get_cats(
        skip=skip,
        limit=limit,
        session=session
    )


# Получение информации о конкретном котенке


@router.get(
    '/cats/{id}',
    response_model=List[CatDTO]
)
async def get_cat_by_id(
    id: int,
    session: AsyncSession = Depends(get_async_session)
) -> List[CatDTO]:
    return await CatService.get_cat_by_id(
        id=id,
        session=session
    )
