from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_and_retrieve_project():
    created = client.post(
        "/api/v1/projects",
        json={"name": "Demo garden", "description": "Prototype parcel"},
    )
    assert created.status_code == 201
    project_id = created.json()["id"]

    retrieved = client.get(f"/api/v1/projects/{project_id}")
    assert retrieved.status_code == 200
    assert retrieved.json()["name"] == "Demo garden"


def test_add_scene_object():
    created = client.post("/api/v1/projects", json={"name": "Test project"})
    project_id = created.json()["id"]

    response = client.post(
        f"/api/v1/projects/{project_id}/scene-objects",
        json={
            "name": "Oak tree",
            "object_type": "tree",
            "position": [2.0, 0.0, 4.0],
        },
    )
    assert response.status_code == 201
    assert len(response.json()["scene_objects"]) == 1
    assert response.json()["scene_objects"][0]["name"] == "Oak tree"
