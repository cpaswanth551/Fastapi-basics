from fastapi import APIRouter, Depends, Request

from app.custom_log import log


router = APIRouter(
    prefix="/dependencies", tags=["dependencies"], dependencies=[Depends(log)]
)


# multi level dependency


def convert_params(request: Request, separator: str):
    query = []
    for key, value in request.query_params.items():
        query.append(f"{key} {separator} {value}")
    return query


def convert_headers(
    request: Request, separator: str = "--", query=Depends(convert_params)
):
    out_headers = []
    for key, value in request.headers.items():
        out_headers.append(f"{key} {separator} {value}")
    return {"headers": out_headers, "query": query}


@router.get("")
def get_items(test: str, separator: str = "--", headers=Depends(convert_headers)):
    return {"items": ["a", "b", "c"], "headers": headers}


@router.post("/new")
def create_items(header=Depends(convert_headers)):
    return {"item": [1, 2, 3, 4], "headers": header}


# class based dependency


class Account:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


@router.post("/user")
def create_user(
    name: str, email: str, password: str, account: Account = Depends(Account)
):
    return {"name": account.name, "email": account.email}
