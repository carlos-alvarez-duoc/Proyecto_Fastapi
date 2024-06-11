"""docstring"""
from sqlalchemy.orm import Session
from app.models.user import User  # Importación absoluta del modelo User
from app.schemas.user import UserCreate  # Importación absoluta del esquema UserCreate
from app.security import get_password_hash  # Importación absoluta de la función get_password_hash

def get_user_by_email(db: Session, email: str):
    """docstring"""
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    """docstring"""
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
