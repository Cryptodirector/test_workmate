from fastapi import (
    APIRouter,
    Depends
)
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
from app.schemas.v1.cat_schemas import (
    CatDTO
)
from app.schemas.v1.breed_schema import BreedDTO
from app.service.v1.breed_service import BreedService
from typing import List


router = APIRouter(
    prefix='/api/v1',
    tags=['Breed']
)


# Получение списка котят определенной породы


@router.get(
    '/cats/breed/{id}',
    response_model=List[CatDTO]
)
async def get_cats_filter(
    id: int,
    skip: int = 0,
    limit: int = 10,
    session: AsyncSession = Depends(get_async_session)
) -> List[CatDTO]:
    return await BreedService.get_cats_filter(
        skip=skip,
        limit=limit,
        id=id,
        session=session
    )


# Получение списка всех пород


@router.get(
    '/breed',
    response_model=List[BreedDTO]
)
async def get_breeds(
    skip: int = 0,
    limit: int = 10,
    session: AsyncSession = Depends(get_async_session)
) -> List[BreedDTO]:
    return await BreedService.get_breed(
        skip=skip,
        limit=limit,
        session=session
    )
