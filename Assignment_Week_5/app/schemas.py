from pydantic import BaseModel, EmailStr
from datetime import datetime
from app.models import UserRole

class UserRegister(BaseModel):
    email: EmailStr
    password: str
    role: UserRole
    name: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserResponse(BaseModel):
    id: int
    email: str
    role: UserRole
    name: str

    class Config:
        from_attributes = True

class AvailabilityCreate(BaseModel):
    start_time: datetime
    end_time: datetime

class AvailabilityResponse(BaseModel):
    id: int
    doctor_id: int
    start_time: datetime
    end_time: datetime

    class Config:
        from_attributes = True

class AppointmentCreate(BaseModel):
    doctor_id: int
    start_time: datetime
    end_time: datetime

class AppointmentResponse(BaseModel):
    id: int
    doctor_id: int
    patient_id: int
    start_time: datetime
    end_time: datetime
    status: str

    class Config:
        from_attributes = True

class ForgotPassword(BaseModel):
    email: EmailStr
