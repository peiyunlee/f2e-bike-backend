import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import store,user,route
from db import models
from db.database import engine

app = FastAPI(
    title="Taiwan Bike API",
    description="This API was developed for Taiwan Bike Website",
    version="0.0.1",
    terms_of_service="http://localhost:3000",
)

app.include_router(route.router)
app.include_router(store.router)
app.include_router(user.router)

if __name__ == "__main__":
    uvicorn.run("app:app", port=3000, reload=True)

origins = [
    'http://localhost:3000',
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

models.Base.metadata.create_all(engine)
