from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse


router = APIRouter(prefix="/product", tags=["product"])

products = ["watch", "camera", "phone"]


@router.get("/all")
def get_all_products():
    data = " ".join(products)
    return Response(content=data, media_type="text/plain")


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
