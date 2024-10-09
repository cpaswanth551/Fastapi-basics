from typing import List
from fastapi import APIRouter, Depends


from sqlalchemy.orm import Session

from app.db import db_article
from app.db.database import get_db
from app.schemas import Article, ArticleBase, ArticleDisplay
from app.auth.oauth2 import get_current_user, oath2_schema
from app.schemas import User

router = APIRouter(prefix="/article", tags=["article"])


# create article


@router.post("/", response_model=ArticleDisplay)
def create_article(
    request: ArticleBase,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return db_article.create_article(db, request)


@router.get("/{id}")
def get_article(
    id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)
):
    article = db_article.get_article(db, id)
    return {"data": article, "current_user": user}
