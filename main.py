from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, get_db

app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)


# -----------------------------
# Home
# -----------------------------
@app.get("/")
def home():
    return {"message": "Welcome to Movie Management System"}


# -----------------------------
# GET TOTAL MOVIES
# -----------------------------
@app.get("/movies/count", status_code=status.HTTP_200_OK)
def total_movies(db: Session = Depends(get_db)):

    total = db.query(models.Movie).count()

    return {"total_movies": total}


# -----------------------------
# GET ALL MOVIES
# -----------------------------
@app.get("/movies", status_code=status.HTTP_200_OK)
def get_movies(db: Session = Depends(get_db)):

    movies = db.query(models.Movie).all()

    if not movies:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movies Not Found"
        )

    return {"message": "All Movies", "data": movies}


# -----------------------------
# GET MOVIE BY ID
# -----------------------------
@app.get("/movies/{id}", status_code=status.HTTP_200_OK)
def get_movie_by_id(id: int, db: Session = Depends(get_db)):

    movie = db.query(models.Movie).filter(models.Movie.movie_id == id).first()

    if movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie Not Found"
        )

    return {"message": "Movie Found", "data": movie}


# -----------------------------
# GET MOVIES BY GENRE
# -----------------------------
@app.get("/movies/genre/{gen}", status_code=status.HTTP_200_OK)
def get_movies_by_genre(gen: str, db: Session = Depends(get_db)):

    movies = db.query(models.Movie).filter(models.Movie.genre == gen).all()

    if not movies:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movies Not Found"
        )

    return {"message": "Movies Found", "data": movies}


# -----------------------------
# GET AVAILABLE MOVIES
# -----------------------------
@app.get("/movies/is_availible/{available}", status_code=status.HTTP_200_OK)
def get_available_movies(available: bool, db: Session = Depends(get_db)):

    movies = db.query(models.Movie).filter(models.Movie.is_availible == available).all()

    if not movies:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movies Not Found"
        )

    return {"message": "Available Movies", "data": movies}


# -----------------------------
# GET MOVIES BY MINIMUM RATING
# -----------------------------
@app.get("/movies/rating/{rate}", status_code=status.HTTP_200_OK)
def get_movies_by_rating(rate: float, db: Session = Depends(get_db)):

    movies = db.query(models.Movie).filter(models.Movie.rating >= rate).all()

    if not movies:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movies Not Found"
        )

    return {"message": "Movies Found", "data": movies}


# -----------------------------
# CREATE MOVIE
# -----------------------------
@app.post("/movies", status_code=status.HTTP_201_CREATED)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):

    new_movie = models.Movie(**movie.model_dump())

    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    return {"message": "Movie Added Successfully", "data": new_movie}


# -----------------------------
# UPDATE MOVIE
# -----------------------------
@app.put("/movies/{id}", status_code=status.HTTP_200_OK)
def update_movie(
    id: int,
    updated_movie: schemas.MovieCreate,
    db: Session = Depends(get_db),
):

    movie_query = db.query(models.Movie).filter(models.Movie.movie_id == id)

    movie = movie_query.first()

    if movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie Not Found"
        )

    movie_query.update(updated_movie.model_dump(), synchronize_session=False)

    db.commit()

    return {"message": "Movie Updated Successfully", "data": movie_query.first()}


# -----------------------------
# DELETE MOVIE
# -----------------------------
@app.delete("/movies/{id}", status_code=status.HTTP_200_OK)
def delete_movie(id: int, db: Session = Depends(get_db)):

    movie_query = db.query(models.Movie).filter(models.Movie.movie_id == id)

    movie = movie_query.first()

    if movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie Not Found"
        )

    movie_query.delete(synchronize_session=False)
    db.commit()

    return {"message": "Movie Deleted Successfully"}
