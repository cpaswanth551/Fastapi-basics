from asyncio import create_task
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from app.db import models, database
from app.exceptions import StoryException
from app.router import blog_get, blog_post, product, user, article
from fastapi.middleware.cors import CORSMiddleware
from app.auth import authentication

app = FastAPI()


app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT, content={"detail": exc.name}
    )


models.Base.metadata.create_all(database.engine)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
