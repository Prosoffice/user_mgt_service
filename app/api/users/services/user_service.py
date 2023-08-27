from typing import Optional, Any
from sqlalchemy.orm import Session
from app.api.users.dto.user_dto import UserCreateDto, UserUpdateDto
from app.api.users.models.user_model import User
from app.api.users.services import BaseService
from app.core.security import get_password_hash


class UserService(BaseService[User, UserCreateDto, UserUpdateDto]):

    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def get(self, db: Session, id: Any) -> Optional[User]:
        return db.query(User).filter(User.id == id).first()

    def create(self, db: Session, *, obj_in: UserCreateDto) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            first_name=obj_in.first_name,
            last_name=obj_in.last_name,
            is_admin=obj_in.is_admin,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


userService = UserService(User)
