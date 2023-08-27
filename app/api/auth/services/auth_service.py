from typing import Optional
from fastapi import HTTPException, status
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from app.api.auth.dto.token_dto import TokenPayload
from app.api.users.models.user_model import User
from app.api.users.services.user_service import userService
from app.core import security
from app.core.config import settings
from app.core.security import verify_password


class AuthenticationService:

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = userService.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def get_current_user(
            self, db: Session, token: str
    ) -> User:
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[security.ALGORITHM])
            token_data = TokenPayload(**payload)
        except (jwt.JWTError, ValidationError):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
            )
        user = userService.get(db, id=token_data.sub)
        if not user:
            raise HTTPException(status_code=400, detail="Inactive user")
        return user


authService = AuthenticationService()
