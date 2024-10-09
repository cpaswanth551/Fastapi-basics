from typing import List, Optional
from fastapi import APIRouter, Cookie, Header, Response
from fastapi.responses import HTMLResponse


router = APIRouter(prefix="/product", tags=["product"])

products = ["watch", "camera", "phone"]


@router.get("/all")
def get_all_products():
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(
        key="test_cookie", value="this is a test cookie value"
    )  # cookie setting here ....
    return response


@router.get("/withheader")
def get_all_products(
    response: Response, custom_header: Optional[List[str]] = Header(None)
):
    if custom_header:
        response.headers["custom_response_header"] = " and ".join(custom_header)
    return {"data": products, "custom_header": custom_header}


@router.get("/withcookiees")
def get_all_products(
    response: Response,
    custom_header: Optional[List[str]] = Header(None),
    test_cookie: Optional[str] = Cookie(None),  # here cookie is retreived  ....
):
    if custom_header:
        response.headers["custom_response_header"] = " and ".join(custom_header)

    print(test_cookie)

    return {"data": products, "custom_header": custom_header, "my_cookie": test_cookie}


@router.get(
    "/{id}",
    responses={
        200: {
            "content": {"text/html": {"example": "<div>Product</div>"}},
            "description": "return the HTML for an Object.",
        },
        404: {
            "content": {"text/plain": {"example": "Product Not avialiable"}},
            "description": "A clear text error message.",
        },
    },
)
def get_product(id: int):
    product = products[id]
    out = f"""
    <head>
      <style>
      .product {{
        width: 500px;
        height: 30px;
        border: 2px inset green;
        background-color: lightblue;
        text-align: center;
      }}
      </style>
    </head>
    <div class="product">{product}</div>
    """

    return HTMLResponse(content=out, media_type="text/html")
