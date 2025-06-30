from sqlalchemy.orm import Session
from .models import User

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, email: str, full_name: str):
    user = User(email=email, full_name=full_name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
