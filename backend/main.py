from fastapi import FastAPI
import uvicorn

from mangodm import connect_to_mongo, close_mongo_connection

from modules.Chapter.models import register_chapter_collections
from modules.Node.models import register_node_collections
from modules.Novel.models import register_novel_collections
from modules.Person.models import register_person_collections
from modules.Scene.models import register_scene_collections
from modules.User.models import register_user_collections


app = FastAPI(
    title="CultVet",
    description="API for create visual novels.",
    version="0.1",
    contact={
        "name": "Author: Alexander Rodionov",
        "email": "sa27shal@gmail.com"
    },
    openapi_url="/api/v0.1/openapi.json",
    redoc_url=None,
)


@app.on_event("startup")
async def startup_event():
    register_chapter_collections()
    register_node_collections()
    register_novel_collections()
    register_person_collections()
    register_scene_collections()
    register_user_collections()

    await connect_to_mongo("", "")  # TODO
    print("Connect to mongo.")


@app.on_event("shutdown")
async def shutdown_event():
    close_mongo_connection()
    print("Close mongo connection.")


@app.get("/api", description="Root endpoint", tags=['BASE'])
async def test():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
