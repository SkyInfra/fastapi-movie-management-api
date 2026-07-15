from fastapi import Body, FastAPI
from fastapi import status 
from fastapi import HTTPException
from pydantic import BaseModel

app = FastAPI()


# -----------------------------
# Movie Management System
# -----------------------------

movie_store = []


class Movie(BaseModel):
    movie_id: str
    title: str
    director: str
    genre: str
    release_year: int
    rating: float
    available: bool


@app.get("/")
def home():
    return {
        "message": "Welcome to Movie Management System"
    }


# -----------------------------
# GET ALL MOVIES
# -----------------------------
@app.get("/movies",status_code = status.HTTP_200_OK)
def get_movies():
    return {
        "message": "All Movies",
        "data": movie_store
    }


# -----------------------------
# GET MOVIE BY ID
# -----------------------------
@app.get("/movies/{movie_id}", status_code= status.HTTP_200_OK)
def get_movie_by_id(movie_id: str):
    for movie in movie_store:
        if movie["movie_id"] == movie_id:
            return {
                "message": "Movie Found",
                "data": movie
            }

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Movies Not Found "
    )


# -----------------------------
# GET MOVIES BY GENRE
# -----------------------------
@app.get("/movies/genre/{genre}", status_code = status.HTTP_200_OK)
def get_movies_by_genre(genre: str):
    movies = []

    for movie in movie_store:
        if movie["genre"].lower() == genre.lower():
            movies.append(movie)

    if movies:
        return {
            "message": "Movies Found",
            "data": movies
        }
    raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND,
        detail = "Movies Not Found"
    )


# -----------------------------
# GET AVAILABLE MOVIES
# -----------------------------
@app.get("/movies/available/{available}", status_code= status.HTTP_200_OK)
def get_available_movies(available: bool):
    movies = []

    for movie in movie_store:
        if movie["available"] == available:
            movies.append(movie)

    return {
        "message": "Available Movies",
        "data": movies
    }


# -----------------------------
# GET MOVIES BY MINIMUM RATING
# -----------------------------
@app.get("/movies/rating/{rating}", status_code = status.HTTP_200_OK)
def get_movies_by_rating(rating: float):
    movies = []

    for movie in movie_store:
        if movie["rating"] >= rating:
            movies.append(movie)

    return {
        "message": "Movies Found",
        "data": movies
    }


# -----------------------------
# GET TOTAL MOVIES
# -----------------------------
@app.get("/movies/count" , status_code= status.HTTP_200_OK)
def total_movies():
    return {
        "total_movies": len(movie_store)
    }


# -----------------------------
# CREATE MOVIE
# -----------------------------
@app.post("/movies", status_code = status.HTTP_200_OK)
def create_movie(movie: Movie):
    movie_store.append(movie.model_dump())

    return {
        "message": "Movie added successfully",
        "data": movie
    }


# -----------------------------
# UPDATE MOVIE
# -----------------------------
@app.put("/movies/{movie_id}" ,status_code =  status.HTTP_200_OK)
def update_movie(movie_id: str, updated_movie: Movie):

    for movie in movie_store:
        if movie["movie_id"] == movie_id:
            movie.update(updated_movie.model_dump())

            return {
                "message": "Movie updated successfully",
                "data": movie
            }

    raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND,
        detail = "Movie Not Found"
    )

# -----------------------------
# DELETE MOVIE
# -----------------------------
@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: str):

    for movie in movie_store:
        if movie["movie_id"] == movie_id:
            movie_store.remove(movie)

            return {
                "message": "Movie deleted successfully",
                "data": movie
            }

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Movie not found"
    )
