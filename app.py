import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import route, store, user, authentication
from db import models
from db.database import engine


app = FastAPI(
    title="Twain Bike API",
    description="This API was developed for Twain Bike Website",
    version="0.0.1",
)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(store.router)
app.include_router(route.router)


if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, reload=True)


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

models.Base.metadata.create_all(engine)