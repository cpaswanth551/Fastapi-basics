from typing import List
from fastapi import APIRouter, Depends

from app.auth.oauth2 import get_current_user
from app.db import db_user
from app.db.database import get_db
from app.schemas import UserBase, UserDisplay

from sqlalchemy.orm import Session


router = APIRouter(prefix="/user", tags=["user"])

# create user


@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# Read all user


@router.get("/", response_model=List[UserDisplay])
def get_all_users(
    db: Session = Depends(get_db), user: UserBase = Depends(get_current_user)
):
    return db_user.retreive_all_users(db)


# Read one User


@router.get("/{id}", response_model=UserDisplay)
def get_user(
    id: int, db: Session = Depends(get_db), user: UserBase = Depends(get_current_user)
):
    return db_user.retreive_user_byId(db, id)


# update a user


@router.post("/{id}/update")
def update_user(
    id: int,
    request: UserBase,
    db: Session = Depends(get_db),
    user: UserBase = Depends(get_current_user),
):
    return db_user.update_user(db, id, request)


# delete a user


@router.get("/{id}/delete")
def delete_user(
    id: int, db: Session = Depends(get_db), user: UserBase = Depends(get_current_user)
):
    return db_user.delete_user(db, id)
