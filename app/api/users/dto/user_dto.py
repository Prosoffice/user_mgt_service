from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_admin: Optional[bool] = False


class UserCreateDto(UserBase):
    password: str


class UserUpdateDto(UserBase):
    password: Optional[str] = None


class UserInDbBase(UserBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True


class User(UserInDbBase):
    pass


class UserInDb(UserInDbBase):
    hashed_password: str
