from fastapi import FastAPI

import models
from database import engine
from routers import movie, user, auth


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(movie.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def home():
    return {"message": "Welcome to Movie Management System"}