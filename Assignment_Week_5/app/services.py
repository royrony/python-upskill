from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories import UserRepository, AvailabilityRepository, AppointmentRepository
from app.security import hash_password, verify_password, create_access_token
from app.models import User, UserRole
from datetime import datetime

class AuthService:
    def __init__(self, db: AsyncSession):
        self.user_repo = UserRepository(db)

    async def register(self, email: str, password: str, role: UserRole, name: str) -> User:
        existing_user = await self.user_repo.get_by_email(email)
        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
        
        password_hash = hash_password(password)
        return await self.user_repo.create(email, password_hash, role, name)

    async def login(self, email: str, password: str) -> str:
        user = await self.user_repo.get_by_email(email)
        if not user or not verify_password(password, user.password_hash):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        
        return create_access_token({"sub": user.id})

    async def forgot_password(self, email: str) -> dict:
        user = await self.user_repo.get_by_email(email)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        return {"message": "Password reset link sent to email"}

class DoctorService:
    def __init__(self, db: AsyncSession):
        self.availability_repo = AvailabilityRepository(db)
        self.appointment_repo = AppointmentRepository(db)

    async def set_availability(self, doctor_id: int, start_time: datetime, end_time: datetime):
        if start_time >= end_time:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid time range")
        
        return await self.availability_repo.create(doctor_id, start_time, end_time)

    async def get_appointments(self, doctor_id: int):
        return await self.appointment_repo.get_by_doctor(doctor_id)

class PatientService:
    def __init__(self, db: AsyncSession):
        self.user_repo = UserRepository(db)
        self.availability_repo = AvailabilityRepository(db)
        self.appointment_repo = AppointmentRepository(db)

    async def get_all_doctors(self):
        return await self.user_repo.get_all_doctors()

    async def get_doctor_availability(self, doctor_id: int):
        doctor = await self.user_repo.get_by_id(doctor_id)
        if not doctor or doctor.role != UserRole.DOCTOR:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found")
        
        return await self.availability_repo.get_by_doctor(doctor_id)

    async def book_appointment(self, patient_id: int, doctor_id: int, start_time: datetime, end_time: datetime):
        doctor = await self.user_repo.get_by_id(doctor_id)
        if not doctor or doctor.role != UserRole.DOCTOR:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found")
        
        if start_time >= end_time:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid time range")
        
        has_conflict = await self.appointment_repo.check_conflict(doctor_id, start_time, end_time)
        if has_conflict:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Time slot already booked")
        
        return await self.appointment_repo.create(doctor_id, patient_id, start_time, end_time)

    async def cancel_appointment(self, appointment_id: int, patient_id: int):
        appointment = await self.appointment_repo.get_by_id(appointment_id)
        if not appointment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")
        
        if appointment.patient_id != patient_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
        
        await self.appointment_repo.cancel(appointment)
        return {"message": "Appointment cancelled"}
