from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import AppointmentCreate, AppointmentResponse
from app.services import PatientService
from app.security import get_current_user
from app.models import User, UserRole

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("", response_model=AppointmentResponse)
async def book_appointment(appointment: AppointmentCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.PATIENT:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only patients can book appointments")
    
    service = PatientService(db)
    return await service.book_appointment(current_user.id, appointment.doctor_id, appointment.start_time, appointment.end_time)

@router.delete("/{appointment_id}")
async def cancel_appointment(appointment_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.PATIENT:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only patients can cancel appointments")
    
    service = PatientService(db)
    return await service.cancel_appointment(appointment_id, current_user.id)
