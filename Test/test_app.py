import pytest
from httpx import ASGITransport, AsyncClient
from load import app

@pytest.mark.asyncio
async def test_create_post():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post(
            "/posts/",
            json={"title": "Test Post", "content": "This is a test post", "owner_id": 1}
        )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Post"
    assert data["content"] == "This is a test post"
    assert data["owner_id"] == 1
    assert "id" in data

@pytest.mark.asyncio
async def test_get_post():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

