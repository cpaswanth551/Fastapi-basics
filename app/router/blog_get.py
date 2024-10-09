from fastapi import APIRouter, Depends, Response, status
from enum import Enum
from typing import Optional

from app.router.blog_post import req_functionality

router = APIRouter(prefix="/blog", tags=["blog"])


@router.get(
    "/all",
    summary="Retreive all blogs",
    description="This api call stimulates fetching all blogs.",
    response_description="list of avialiable blogs",
)
def get_blog_all(
    page_size=10, page=1, req_parameter: dict = Depends(req_functionality)
):
    return {
        "message": f"message from all blogs in {page} of  {page_size} pages",
        "required": req_parameter,
    }


@router.get("/allsizes")
def get_blog_allsizes(
    page=1,
    page_size: Optional[int] = None,
    req_parameter: dict = Depends(req_functionality),
):
    return {
        "message": f"message from all blogs in {page} : {page_size}",
        "required": req_parameter,
    }


@router.get(
    "/id/{id}/commment/{comment_id}",
    tags=["comment"],
    summary="Retreives comments of a blog",
)
def get_blog_complex(
    id,
    commment_id,
    valid=True,
    username: Optional[str] = None,
    req_parameter: dict = Depends(req_functionality),
):
    """
    simulates retrieving a comment of a blog
    - **id** mandatory path parameter
    - **commment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter
    """
    return {
        "message": f"blog with id {id} having comment {commment_id} is valid {valid} by username {username} ",
        "required": req_parameter,
    }


class BlogCategoryType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@router.get("/type/{type}")
def get_blog_by_type(
    type: BlogCategoryType,
    req_parameter: dict = Depends(req_functionality),
):
    return {
        "message": f"blog of type {type}",
        "required": req_parameter,
    }


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog_by_id(
    id: int,
    response: Response,
    req_parameter: dict = Depends(req_functionality),
):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"id with {id} not found."}

    return {
        "message": f"this is a message from {id}",
        "required": req_parameter,
    }
