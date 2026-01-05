from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import AvailabilityCreate, AvailabilityResponse, AppointmentResponse, UserResponse
from app.services import DoctorService, PatientService
from app.security import get_current_user
from app.models import User, UserRole

router = APIRouter(prefix="/doctors", tags=["Doctors"])

@router.get("", response_model=list[UserResponse])
async def get_all_doctors(db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    service = PatientService(db)
    return await service.get_all_doctors()

@router.get("/{doctor_id}/availability", response_model=list[AvailabilityResponse])
async def get_doctor_availability(doctor_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    service = PatientService(db)
    return await service.get_doctor_availability(doctor_id)

@router.post("/availability", response_model=AvailabilityResponse)
async def set_availability(availability: AvailabilityCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.DOCTOR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only doctors can set availability")
    
    service = DoctorService(db)
    return await service.set_availability(current_user.id, availability.start_time, availability.end_time)

@router.get("/appointments", response_model=list[AppointmentResponse])
async def get_appointments(db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.DOCTOR:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only doctors can view their appointments")
    
    service = DoctorService(db)
    return await service.get_appointments(current_user.id)
