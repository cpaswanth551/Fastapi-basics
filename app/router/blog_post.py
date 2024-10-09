from typing import Dict, List, Optional
from fastapi import APIRouter, Body, Path, Query
from pydantic import BaseModel

router = APIRouter(prefix="/blog", tags=["blog"])


class BlogModel(BaseModel):
    title: str
    description: str
    nb_comments: int
    published: Optional[bool]


@router.post("/new")
def blog_create(blog: BlogModel):
    return {"data": blog}


@router.post("/new/{id}")
def blog_create_with_id(blog: BlogModel, id: int, version: int = 1):
    return {"data": {"id": id, "data": blog, "version": version}}


class Image(BaseModel):
    url: str
    alias: str


@router.post("/new/{id}/comment/{comment_id}")
def create_comment(
    blog: BlogModel,
    id: int,
    comment_title: str = Query(
        description="description for comment title",
        title="title of the comment",
        alias="title",
        deprecated=True,
    ),
    phone_number: str = Body(..., max_length=10, regex="^\d{10}$"),
    content: str = Body(..., max_length=15, min_length=10, regex="^[a-z\s]*$"),
    v: Optional[List[str]] = Query(None),
    option: Optional[List[str]] = Query(["1", "2", "3"]),
    comment_id: int = Path(..., gt=2, lt=15),
    tags: List[str] = ["tag1", "tag2"],
    metadata: Dict[str, str] = {"key1": "value1"},
    image: Optional[Image] = None,
):
    return {
        "data": blog,
        "id": id,
        "comment_ID": comment_id,
        "content": content,
        "phone_number": phone_number,
        "version": v,
        "option": option,
        "comment_title": comment_title,
        "tags": tags,
        "metadata": metadata,
        "image": image,
    }


def req_functionality():
    return {"message": "this is required functionality for all"}
