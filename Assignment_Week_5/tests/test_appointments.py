import pytest
from httpx import AsyncClient
from datetime import datetime, timedelta
from app.security import create_access_token

@pytest.mark.asyncio
async def test_book_appointment(client: AsyncClient, test_doctor, test_patient):
    token = create_access_token({"sub": test_patient.id})
    headers = {"Authorization": f"Bearer {token}"}
    
    start_time = datetime.utcnow() + timedelta(days=1)
    end_time = start_time + timedelta(hours=1)
    
    response = await client.post("/appointments", json={
        "doctor_id": test_doctor.id,
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat()
    }, headers=headers)
    
    assert response.status_code == 200
    data = response.json()
    assert data["doctor_id"] == test_doctor.id
    assert data["patient_id"] == test_patient.id

@pytest.mark.asyncio
async def test_book_appointment_conflict(client: AsyncClient, test_doctor, test_patient):
    token = create_access_token({"sub": test_patient.id})
    headers = {"Authorization": f"Bearer {token}"}
    
    start_time = datetime.utcnow() + timedelta(days=1)
    end_time = start_time + timedelta(hours=1)
    
    await client.post("/appointments", json={
        "doctor_id": test_doctor.id,
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat()
    }, headers=headers)
    
    response = await client.post("/appointments", json={
        "doctor_id": test_doctor.id,
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat()
    }, headers=headers)
    
    assert response.status_code == 409

@pytest.mark.asyncio
async def test_cancel_appointment(client: AsyncClient, test_doctor, test_patient):
    token = create_access_token({"sub": test_patient.id})
    headers = {"Authorization": f"Bearer {token}"}
    
    start_time = datetime.utcnow() + timedelta(days=1)
    end_time = start_time + timedelta(hours=1)
    
    book_response = await client.post("/appointments", json={
        "doctor_id": test_doctor.id,
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat()
    }, headers=headers)
    
    appointment_id = book_response.json()["id"]
    
    response = await client.delete(f"/appointments/{appointment_id}", headers=headers)
    assert response.status_code == 200
