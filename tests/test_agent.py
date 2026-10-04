from fastapi.testclient import TestClient
from aicloudops.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'optimize idle', **{'payload': {'idle': True}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["actions"] == ["rightsize"]
    refused = client.post("/agent/run", json={"goal": 'stop vm now'}).json()
    assert refused["refused"] is True
