from uuid import UUID

from fastapi import FastAPI

from blogger.database import Database
from blogger.model import Post

app = FastAPI()
database = Database()


@app.post("/posts", response_model=UUID)
async def create_posts(post: Post):
    return database.create(post)


@app.get("/posts", response_model=Post)
async def read_posts(uuid: UUID):
    return database.read(uuid)


@app.put("/posts")
async def update_posts(uuid: UUID, post: Post):
    database.update(post)


@app.delete("/posts")
async def delete_posts(uuid: UUID):
    database.delete(uuid)
