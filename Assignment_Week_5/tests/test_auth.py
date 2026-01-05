import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_register_user(client: AsyncClient):
    response = await client.post("/auth/register", json={
        "email": "newuser@test.com",
        "password": "password123",
        "role": "Patient",
        "name": "New User"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "newuser@test.com"
    assert data["role"] == "Patient"

@pytest.mark.asyncio
async def test_register_duplicate_email(client: AsyncClient):
    await client.post("/auth/register", json={
        "email": "duplicate@test.com",
        "password": "password123",
        "role": "Patient",
        "name": "User One"
    })
    
    response = await client.post("/auth/register", json={
        "email": "duplicate@test.com",
        "password": "password123",
        "role": "Doctor",
        "name": "User Two"
    })
    assert response.status_code == 400

@pytest.mark.asyncio
async def test_login_success(client: AsyncClient, test_patient):
    response = await client.post("/auth/login", json={
        "email": "patient@test.com",
        "password": "password123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

@pytest.mark.asyncio
async def test_login_invalid_credentials(client: AsyncClient, test_patient):
    response = await client.post("/auth/login", json={
        "email": "patient@test.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_forgot_password(client: AsyncClient, test_patient):
    response = await client.post("/auth/forgot-password", json={
        "email": "patient@test.com"
    })
    assert response.status_code == 200
    assert "message" in response.json()
