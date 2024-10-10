from fastapi import APIRouter, Depends, Request


router = APIRouter(prefix="/dependencies", tags=["dependencies"])


def convert_header(request: Request, seperater: str = "---"):
    out_headers = []
    for key, value in request.headers.items():
        out_headers.append(f"{key} {seperater} {value}")
    return out_headers


@router.get("")
def get_items(header=Depends(convert_header)):
    return {"item": [1, 2, 3, 4], "headers": header}


@router.post("/new")
def create_items(header=Depends(convert_header)):
    return {"item": [1, 2, 3, 4], "headers": header}
