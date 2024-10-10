from fastapi import APIRouter, BackgroundTasks, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.schemas import ProductBase
from app.custom_log import log


router = APIRouter(prefix="/templates", tags=["templates"])


templates = Jinja2Templates(directory="templates")


@router.post("/product/{id}", response_class=HTMLResponse)
def get_product(id: str, product: ProductBase, request: Request, bt: BackgroundTasks):
    bt.add_task(log_template_call(f"template read for product with id {id}"))
    return templates.TemplateResponse(
        "product.html",
        {
            "request": request,
            "id": id,
            "title": product.title,
            "description": product.description,
            "price": product.price,
        },
    )


def log_template_call(message: str):
    log("MyAPI", message)
