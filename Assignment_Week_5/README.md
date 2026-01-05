# Doctor Appointment API

Production-ready RESTful API for managing doctor appointments with JWT authentication and role-based access control.

## Tech Stack

- Python 3.12+
- FastAPI
- PostgreSQL
- SQLAlchemy (Async)
- JWT Authentication
- Docker & Docker Compose
- Pytest

## Quick Start

### Using Docker Compose (Recommended)

```bash
docker-compose up
```

The API will be available at `http://localhost:8000`

### Manual Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create `.env` file:
```bash
cp .env.example .env
```

3. Start PostgreSQL database

4. Run the application:
```bash
uvicorn app.main:app --reload
```

## API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Authentication Flow

### Registration
Users register with email, password, role (Doctor/Patient), and name. Passwords are hashed using bcrypt before storage.

### Login
Users authenticate with email and password. Upon successful authentication, a JWT token is issued with the user ID in the payload.

### Protected Routes
All business endpoints require a valid JWT token in the Authorization header:
```
Authorization: Bearer <token>
```

The token is validated on each request, and the current user is extracted from the token payload.

## RBAC Design

### Roles
- **Doctor**: Can set availability and view their appointments
- **Patient**: Can view doctors, check availability, book and cancel appointments

### Access Control
Role-based checks are performed at the endpoint level:
- Doctors can only access doctor-specific endpoints
- Patients can only access patient-specific endpoints
- Unauthorized access returns 403 Forbidden

## Architecture

### Service/Repository Pattern

**Repositories** (`app/repositories.py`):
- Handle database operations
- Provide data access abstraction
- Return domain models

**Services** (`app/services.py`):
- Contain business logic
- Validate operations
- Coordinate between repositories
- Raise appropriate HTTP exceptions

**Routers** (`app/routers/`):
- Define API endpoints
- Handle request/response validation
- Delegate to services
- Enforce authentication and authorization

## API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login and get JWT token
- `POST /auth/forgot-password` - Password reset (mock)

### Doctors
- `GET /doctors` - List all doctors (authenticated)
- `GET /doctors/{id}/availability` - View doctor availability (authenticated)
- `POST /doctors/availability` - Set availability (doctors only)
- `GET /doctors/appointments` - View appointments (doctors only)

### Appointments
- `POST /appointments` - Book appointment (patients only)
- `DELETE /appointments/{id}` - Cancel appointment (patients only)

## Testing

Run tests:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov=app tests/
```

## Security Features

- Password hashing with bcrypt
- JWT token-based authentication
- Token expiration (30 minutes default)
- Role-based access control
- SQL injection prevention via SQLAlchemy ORM
- Request validation with Pydantic

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── config.py            # Configuration settings
│   ├── database.py          # Database setup
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── security.py          # Auth utilities
│   ├── repositories.py      # Data access layer
│   ├── services.py          # Business logic layer
│   └── routers/             # API endpoints
│       ├── auth.py
│       ├── doctors.py
│       └── appointments.py
├── tests/                   # Test suite
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```
