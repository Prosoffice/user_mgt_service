from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Any
from app.api.auth.dto.token_dto import Token
from app.api.auth.factories.db_factory import get_db
from app.api.auth.services.auth_service import authService
from app.api.users.dto.user_dto import User, UserCreateDto
from app.api.users.services.user_service import userService
from app.core import security
from app.core.config import settings

router = APIRouter()


@router.post("/login/access-token", response_model=Token)
def login_access_token(db: Session() = Depends(get_db),
                       form_data: OAuth2PasswordRequestForm = Depends()
                       ) -> Any:
    user = authService.authenticate(
        db,
        email=form_data.username,
        password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email/password")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer"
    }


@router.post("/register", response_model=User)
async def create_user(
        *,
        db: Session = Depends(get_db),
        user_in: UserCreateDto,
) -> Any:
    user = userService.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system"
        )
    user = userService.create(db, obj_in=user_in)
    return user


@router.get("/validate_token/{token}", response_model=User)
async def create_user(
        *,
        db: Session = Depends(get_db),
        token: str
) -> Any:
    user = authService.get_current_user(db, token)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Invalid Token"
        )
    return user
