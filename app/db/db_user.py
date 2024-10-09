from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from app.db.hash import Hash
from app.db.models import DbUser
from app.schemas import UserBase
from app.exceptions import StoryException

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def retreive_all_users(db: Session):
    return db.query(DbUser).all()


def retreive_user_byId(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"user with {id} not found"
        )
    return user


def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update(
        {
            DbUser.username: request.username,
            DbUser.email: request.email,
            DbUser.password: Hash.bcrypt(request.password),
        }
    )
    db.commit()
    return "ok"


def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    db.delete(user)
    db.commit()
    return "ok"
