

def test_create_cat(test_client):
    response = test_client.post(
        "/api/cats/create",
        json={
            "color": "string",
            "months_old": 12,
            "descriptions": "stringst",
            "id_breed": 1
        }

    )
    assert response.status_code == 200


def test_create_cat_bad_months(test_client):
    response = test_client.post(
        "/api/cats/create",
        json={
            "color": "string",
            "months_old": 14,
            "descriptions": "stringst",
            "id_breed": 1
        }
    )
    assert response.status_code == 422


def test_create_cat_bad_descript(test_client):
    response = test_client.post(
        "/api/cats/create",
        json={
            "color": "string",
            "months_old": 12,
            "descriptions": "str",
            "id_breed": 1
        }
    )
    assert response.status_code == 422


def test_update_cat(test_client):
    response = test_client.patch(
        "/api/cats/update/1",
        json={
            "color": "string",
            "months_old": 12,
            "descriptions": "stringst",
            "id_breed": 1
        }

    )
    assert response.status_code == 200


def test_update_cat_bad_id(test_client):
    response = test_client.patch(
        "/api/cats/update/0",
        json={
            "color": "string",
            "months_old": 12,
            "descriptions": "stringst",
            "id_breed": 1
        }

    )
    assert response.status_code == 404


def test_delete_cat(test_client):
    response = test_client.delete(
        "/api/cats/delete/1"
    )
    assert response.status_code == 200


def test_delete_cat_bad_id(test_client):
    response = test_client.delete(
        "/api/cats/delete/0"
    )
    assert response.status_code == 404


def test_get_breeds(test_client):
    response = test_client.get(
        "/api/breed"
    )
    assert response.status_code == 200


def test_get_cats_filter(test_client):
    response = test_client.get(
        "/api/cats/breed/15"
    )
    assert response.status_code == 200


def test_get_cats(test_client):
    response = test_client.get(
        "/api/cats"
    )
    assert response.status_code == 200


def test_get_cats_by_id(test_client):
    response = test_client.get(
        "/api/cats/15"
    )
    assert response.status_code == 200
