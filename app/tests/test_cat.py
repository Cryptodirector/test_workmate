from httpx import AsyncClient


async def test_create_cat(
        ac: AsyncClient
) -> None:
    response = await ac.post(
        "/api/v1/cats/create",
        json={
            "color": "string",
            "birthdate": "2024-10-05",
            "descriptions": "stringst",
            "breed_id": 1
        }

    )
    assert response.status_code == 200


async def test_create_cat_bad_months(
        ac: AsyncClient
) -> None:
    response = await ac.post(
        "/api/v1/cats/create",
        json={
            "color": "string",
            "months_old": 14,
            "descriptions": "stringst",
            "breed_id": 1
        }
    )
    assert response.status_code == 422


async def test_create_cat_bad_descript(
        ac: AsyncClient
) -> None:
    response = await ac.post(
        "/api/v1/cats/create",
        json={
            "color": "string",
            "months_old": 12,
            "descriptions": "str",
            "breed_id": 1
        }
    )
    assert response.status_code == 422


async def test_update_cat(
        ac: AsyncClient
) -> None:
    response = await ac.patch(
        "/api/v1/cats/update/1",
        json={
            "color": "string",
            "months_old": 12,
            "descriptions": "stringst",
            "breed_id": 1
        }

    )
    assert response.status_code == 200


async def test_update_cat_bad_id(
        ac: AsyncClient
) -> None:
    response = await ac.patch(
        "/api/v1/cats/update/0",
        json={
            "color": "string",
            "months_old": 12,
            "descriptions": "stringst",
            "breed_id": 1
        }

    )
    assert response.status_code == 404


async def test_get_breeds(
        ac: AsyncClient
) -> None:
    response = await ac.get(
        "/api/v1/breed"
    )
    assert response.status_code == 200


async def test_get_cats_filter(
        ac: AsyncClient
) -> None:
    response = await ac.get(
        "/api/v1/cats/breed/1"
    )
    assert response.status_code == 200


async def test_get_cats(
        ac: AsyncClient
) -> None:
    response = await ac.get(
        "/api/v1/cats"
    )
    assert response.status_code == 200


async def test_get_cats_by_id(
        ac: AsyncClient
) -> None:
    response = await ac.get(
        "/api/v1/cats/1"
    )
    assert response.status_code == 200


async def test_delete_cat(
        ac: AsyncClient
) -> None:
    response = await ac.delete(
        "/api/v1/cats/delete/1"
    )
    assert response.status_code == 204
