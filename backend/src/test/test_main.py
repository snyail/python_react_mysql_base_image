from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_status_ok():
    response = client.get("/health")

    assert response.status_code == 200
    body = response.json()

    assert body["status"] == "ok"
    assert "db_type" in body
