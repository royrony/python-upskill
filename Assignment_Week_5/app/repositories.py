from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import User, Availability, Appointment, UserRole
from datetime import datetime

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, email: str, password_hash: str, role: UserRole, name: str) -> User:
        user = User(email=email, password_hash=password_hash, role=role, name=name)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def get_by_email(self, email: str) -> User | None:
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def get_by_id(self, user_id: int) -> User | None:
        result = await self.db.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    async def get_all_doctors(self) -> list[User]:
        result = await self.db.execute(select(User).where(User.role == UserRole.DOCTOR))
        return list(result.scalars().all())

class AvailabilityRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, doctor_id: int, start_time: datetime, end_time: datetime) -> Availability:
        availability = Availability(doctor_id=doctor_id, start_time=start_time, end_time=end_time)
        self.db.add(availability)
        await self.db.commit()
        await self.db.refresh(availability)
        return availability

    async def get_by_doctor(self, doctor_id: int) -> list[Availability]:
        result = await self.db.execute(select(Availability).where(Availability.doctor_id == doctor_id))
        return list(result.scalars().all())

class AppointmentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, doctor_id: int, patient_id: int, start_time: datetime, end_time: datetime) -> Appointment:
        appointment = Appointment(doctor_id=doctor_id, patient_id=patient_id, start_time=start_time, end_time=end_time)
        self.db.add(appointment)
        await self.db.commit()
        await self.db.refresh(appointment)
        return appointment

    async def get_by_doctor(self, doctor_id: int) -> list[Appointment]:
        result = await self.db.execute(select(Appointment).where(Appointment.doctor_id == doctor_id))
        return list(result.scalars().all())

    async def check_conflict(self, doctor_id: int, start_time: datetime, end_time: datetime) -> bool:
        result = await self.db.execute(
            select(Appointment).where(
                Appointment.doctor_id == doctor_id,
                Appointment.status == "confirmed",
                Appointment.start_time < end_time,
                Appointment.end_time > start_time
            )
        )
        return result.scalar_one_or_none() is not None

    async def get_by_id(self, appointment_id: int) -> Appointment | None:
        result = await self.db.execute(select(Appointment).where(Appointment.id == appointment_id))
        return result.scalar_one_or_none()

    async def cancel(self, appointment: Appointment) -> None:
        appointment.status = "cancelled"
        await self.db.commit()
