from fastapi import FastAPI
import uvicorn

from mangodm import connect_to_mongo, close_connection


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
    await connect_to_mongo()
    print("Connect to mongo.")


@app.on_event("shutdown")
async def shutdown_event():
    await close_connection()
    print("Close mongo connection.")


@app.get("/api", description="Root endpoint", tags=['BASE'])
async def test():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
