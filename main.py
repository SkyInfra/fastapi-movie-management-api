from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException
from pydantic import BaseModel
import time
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import DictCursor

app = FastAPI()

load_dotenv()

while True:
    try:
        con = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            cursor_factory=DictCursor
        )

        cursor = con.cursor()
        print("Connected to database successfully")
        break

    except Exception as error:
        print("Failed to connect to database")
        print("Error:", error)
        time.sleep(2)
# -----------------------------
# Movie Management System
# -----------------------------


class Movie(BaseModel):
    title: str
    director: str
    genre: str
    release_year: int
    rating: int
    is_availible: bool


@app.get("/")
def home():
    return {"message": "Welcome to Movie Management System"}


# -----------------------------
# GET ALL MOVIES
# -----------------------------

@app.get("/movies/count", status_code=status.HTTP_200_OK)
def total_movies():

    cursor.execute("SELECT COUNT(*) AS total FROM movies")

    total = cursor.fetchone()

    return {"total_movies": total["total"]}

@app.get("/movies", status_code=status.HTTP_200_OK)
def get_movies():
    cursor.execute("select * from movies")
    movie = cursor.fetchall()
    return {"message": "All Movies", "data": movie}


# -----------------------------
# GET MOVIE BY ID
# -----------------------------
@app.get("/movies/{id}", status_code=status.HTTP_200_OK)
def get_movie_by_id(id: int):
    cursor.execute("SELECT * FROM movies WHERE movie_id = %s", (id,))

    movie = cursor.fetchone()

    if movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie Not Found"
        )

    return {"message": "Movie Found", "data": movie}


# -----------------------------
# GET MOVIES BY GENRE
# -----------------------------
@app.get("/movies/genre/{gen}", status_code=status.HTTP_200_OK)
def get_movies_by_genre(gen: str):

    cursor.execute("select * from movies where genre = %s", (gen,))
    movies = cursor.fetchall()
    if not movies:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movies Not Found"
        )

    return {"message": "Movies Found", "data": movies}


# -----------------------------
# GET AVAILABLE MOVIES
# -----------------------------
@app.get("/movies/is_availible/{available}", status_code=status.HTTP_200_OK)
def get_available_movies(available: bool):

    cursor.execute("select * from movies where is_availible = %s", (available,))
    movies = cursor.fetchall()

    if not movies:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movies not Found"
        )

    return {"message": "Available Movies", "data": movies}


# -----------------------------
# GET MOVIES BY MINIMUM RATING
# -----------------------------
@app.get("/movies/rating/{rate}", status_code=status.HTTP_200_OK)
def get_movies_by_rating(rate: int):

    cursor.execute("select * from movies where rating > %s", (rate,))
    movies = cursor.fetchall()

    if not movies:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movies Not Found above this rating",
        )
    return {"message": "Movies Found", "data": movies}



# -----------------------------
# CREATE MOVIE
# -----------------------------
@app.post("/movies", status_code=status.HTTP_200_OK)
def create_movie(movie: Movie):
    cursor.execute(
        """INSERT INTO movies
        (title, director, genre, release_year, rating, is_availible)
        VALUES (%s,%s,%s,%s,%s,%s)
        RETURNING *;
        """,
        (
            movie.title,
            movie.director,
            movie.genre,
            movie.release_year,
            movie.rating,
            movie.is_availible,
        ),
    )

    new_movie = cursor.fetchone()
    con.commit()

    return {"message": "Movie added successfully", "data": new_movie}


# -----------------------------
# UPDATE MOVIE
# -----------------------------
@app.put("/movies/{id}", status_code=status.HTTP_200_OK)
def update_movie(id: int, updated_movie: Movie):

    cursor.execute(
        """
        UPDATE movies
        SET
            title = %s,
            director = %s,
            genre = %s,
            release_year = %s,
            rating = %s,
            is_availible = %s
        WHERE movie_id = %s
        RETURNING *;
    """,
        (
            updated_movie.title,
            updated_movie.director,
            updated_movie.genre,
            updated_movie.release_year,
            updated_movie.rating,
            updated_movie.is_availible,
            id,
        ),
    )

    movie = cursor.fetchone()

    if movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie Not Found"
        )

    con.commit()

    return {"message": "Movie Updated Successfully", "data": movie}


# -----------------------------
# DELETE MOVIE
# -----------------------------
@app.delete("/movies/{id}", status_code=status.HTTP_200_OK)
def delete_movie(id: int):

    cursor.execute(
        """
        DELETE FROM movies
        WHERE movie_id = %s
        RETURNING *;
    """,
        (id,),
    )

    movie = cursor.fetchone()

    if movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie Not Found"
        )

    con.commit()

    return {"message": "Movie Deleted Successfully", "data": movie}
