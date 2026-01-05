from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import init_db
from app.routers import auth, doctors, appointments

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(title="Doctor Appointment API", version="1.0.0", lifespan=lifespan)

app.include_router(auth.router)
app.include_router(doctors.router)
app.include_router(appointments.router)

@app.get("/")
async def root():
    return {"message": "Doctor Appointment API"}
