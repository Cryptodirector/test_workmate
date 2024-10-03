from fastapi import (
    APIRouter,
    Depends
)
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
from app.schemas.cat_schemas import (
    CatPost,
    CatUpdate,
    BreedDTO,
    CatsDTO
)
from app.service.cat_service import CatService
from typing import List

router = APIRouter(
    prefix='/api',
    tags=['Кошки']
)


# Добавление котенка

@router.post(
    '/cats/create',
    response_model=CatPost
)
async def create_cat(
    body: CatPost,
    session: AsyncSession = Depends(get_async_session)
) -> CatPost:
    return await CatService.insert_cat(
        body,
        session
    )


# Изменение информации о котенке


@router.patch(
    '/cats/update/{id}',
    response_model=CatUpdate
)
async def update_cat(
    id: int,
    body: CatUpdate,
    session: AsyncSession = Depends(get_async_session)
) -> CatPost:
    return await CatService.update(
        id,
        body,
        session
    )


# Удаление информации о котенке


@router.delete('/cats/delete/{id}')
async def delete_cat(
    id: int,
    session: AsyncSession = Depends(get_async_session)
) -> None:
    return await CatService.delete(
        id,
        session
    )


# Получение списка всех пород


@router.get(
    '/breed',
    response_model=List[BreedDTO]
)
async def get_breeds(
    session: AsyncSession = Depends(get_async_session)
) -> List[BreedDTO]:
    return await CatService.get_breed(session)


# Получение списка котят определенной породы


@router.get(
    '/cats/breed/{id}',
    response_model=List[CatsDTO]
)
async def get_cats_filter(
    id: int,
    session: AsyncSession = Depends(get_async_session)
) -> List[CatsDTO]:
    return await CatService.get_cats_filter(
        id,
        session
    )


# Получение списка всех котят


@router.get(
    '/cats',
    response_model=List[CatsDTO]
)
async def get_cats(
    session: AsyncSession = Depends(get_async_session)
) -> List[CatsDTO]:
    return await CatService.get_cats(session)


# Получение информации о конкретном котенке


@router.get(
    '/cats/{id}',
    response_model=List[CatsDTO]
)
async def get_cat_by_id(
    id: int,
    session: AsyncSession = Depends(get_async_session)
) -> List[CatsDTO]:
    return await CatService.get_cat_by_id(
        id,
        session
    )
