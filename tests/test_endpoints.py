import pytest
import httpx

BASE_URL = "http://app:8000"  

@pytest.mark.asyncio
async def test_create_message():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.post("/messages/", json={"content": "Hello, world!"})
        assert response.status_code == 200
        data = response.json()
        assert "id" in data
        assert data["content"] == "Hello, world!"

@pytest.mark.asyncio
async def test_get_message():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        create_response = await client.post("/messages/", json={"content": "Test message"})
        assert create_response.status_code == 200
        message_id = create_response.json()["id"]
        response = await client.get(f"/messages/{message_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == message_id
        assert data["content"] == "Test message"

@pytest.mark.asyncio
async def test_update_message():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        create_response = await client.post("/messages/", json={"content": "Old content"})
        assert create_response.status_code == 200
        message_id = create_response.json()["id"]
        update_response = await client.put(f"/messages/{message_id}", json={"content": "New content"})
        assert update_response.status_code == 200
        updated_data = update_response.json()
        assert updated_data["content"] == "New content"

@pytest.mark.asyncio
async def test_delete_message():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        create_response = await client.post("/messages/", json={"content": "Delete me"})
        assert create_response.status_code == 200
        message_id = create_response.json()["id"]
        delete_response = await client.delete(f"/messages/{message_id}")
        assert delete_response.status_code == 200
        get_response = await client.get(f"/messages/{message_id}")
        assert get_response.status_code == 404
