import pytest
from httpx import AsyncClient
from datetime import datetime, timedelta
from app.security import create_access_token

@pytest.mark.asyncio
async def test_get_all_doctors(client: AsyncClient, test_doctor, test_patient):
    token = create_access_token({"sub": test_patient.id})
    headers = {"Authorization": f"Bearer {token}"}
    
    response = await client.get("/doctors", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]["role"] == "Doctor"

@pytest.mark.asyncio
async def test_set_availability(client: AsyncClient, test_doctor):
    token = create_access_token({"sub": test_doctor.id})
    headers = {"Authorization": f"Bearer {token}"}
    
    start_time = datetime.utcnow() + timedelta(days=1)
    end_time = start_time + timedelta(hours=8)
    
    response = await client.post("/doctors/availability", json={
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat()
    }, headers=headers)
    
    assert response.status_code == 200
    data = response.json()
    assert data["doctor_id"] == test_doctor.id

@pytest.mark.asyncio
async def test_get_doctor_availability(client: AsyncClient, test_doctor, test_patient):
    doctor_token = create_access_token({"sub": test_doctor.id})
    patient_token = create_access_token({"sub": test_patient.id})
    
    start_time = datetime.utcnow() + timedelta(days=1)
    end_time = start_time + timedelta(hours=8)
    
    await client.post("/doctors/availability", json={
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat()
    }, headers={"Authorization": f"Bearer {doctor_token}"})
    
    response = await client.get(f"/doctors/{test_doctor.id}/availability", headers={"Authorization": f"Bearer {patient_token}"})
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
