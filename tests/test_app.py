import pytest

from hash_service.app import app

ABC_SHA256 = "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"


@pytest.fixture
def client():
    return app.test_client()


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_hash(client):
    response = client.post("/hash", json={"text": "abc"})
    assert response.status_code == 200
    assert response.json == {"algorithm": "sha256", "hash": ABC_SHA256}


def test_hash_without_text(client):
    response = client.post("/hash", json={})
    assert response.status_code == 400


def test_hash_bad_algorithm(client):
    response = client.post("/hash", json={"text": "abc", "algorithm": "crc32"})
    assert response.status_code == 400


def test_verify_match(client):
    response = client.post("/verify", json={"text": "abc", "hash": ABC_SHA256})
    assert response.json == {"match": True}


def test_verify_mismatch(client):
    response = client.post("/verify", json={"text": "abc", "hash": "0" * 64})
    assert response.json == {"match": False}


def test_verify_without_hash(client):
    response = client.post("/verify", json={"text": "abc"})
    assert response.status_code == 400
