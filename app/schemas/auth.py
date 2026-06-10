from pydantic import BaseModel, EmailStr
from app.models.user import UserRole


class LoginRequest(BaseModel):
    phone: str
    password: str


class RegisterRequest(BaseModel):
    phone: str
    password: str
    name: str
    email: EmailStr
    district: str
    state: str = "Tamil Nadu"
    preferred_language: str = "en"
    role: UserRole = UserRole.FARMER


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user_id: str
    role: str
    preferred_language: str


class UserOut(BaseModel):
    id: str
    phone: str
    role: UserRole
    preferred_language: str
    is_active: bool

    class Config:
        from_attributes = True
