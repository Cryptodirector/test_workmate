from fastapi.testclient import TestClient


def test_create_cat(
        test_client: TestClient
) -> None:
    response = test_client.post(
        "/api/v1/cats/create",
        json={
            "color": "string",
            "months_old": 12,
            "descriptions": "stringst",
            "breed_id": 1
        }

    )
    assert response.status_code == 200


def test_create_cat_bad_months(
        test_client: TestClient
) -> None:
    response = test_client.post(
        "/api/v1/cats/create",
        json={
            "color": "string",
            "months_old": 14,
            "descriptions": "stringst",
            "breed_id": 1
        }
    )
    assert response.status_code == 422


def test_create_cat_bad_descript(
        test_client: TestClient
) -> None:
    response = test_client.post(
        "/api/v1/cats/create",
        json={
            "color": "string",
            "months_old": 12,
            "descriptions": "str",
            "breed_id": 1
        }
    )
    assert response.status_code == 422


def test_update_cat(
        test_client: TestClient
) -> None:
    response = test_client.patch(
        "/api/v1/cats/update/1",
        json={
            "color": "string",
            "months_old": 12,
            "descriptions": "stringst",
            "breed_id": 1
        }

    )
    assert response.status_code == 200


def test_update_cat_bad_id(
        test_client: TestClient
) -> None:
    response = test_client.patch(
        "/api/v1/cats/update/0",
        json={
            "color": "string",
            "months_old": 12,
            "descriptions": "stringst",
            "breed_id": 1
        }

    )
    assert response.status_code == 404


def test_delete_cat(
        test_client: TestClient
) -> None:
    response = test_client.delete(
        "/api/v1/cats/delete/1"
    )
    assert response.status_code == 204


def test_get_breeds(
        test_client: TestClient
) -> None:
    response = test_client.get(
        "/api/v1/breed"
    )
    assert response.status_code == 200


def test_get_cats_filter(
        test_client: TestClient
) -> None:
    response = test_client.get(
        "/api/v1/cats/breed/15"
    )
    assert response.status_code == 200


def test_get_cats(
        test_client: TestClient
) -> None:
    response = test_client.get(
        "/api/v1/cats"
    )
    assert response.status_code == 200


def test_get_cats_by_id(
        test_client: TestClient
) -> None:
    response = test_client.get(
        "/api/v1/cats/15"
    )
    assert response.status_code == 200
