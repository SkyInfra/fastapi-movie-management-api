from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

# Student Managment Api 
students = []
@app.get("/")
def managment_api():
    return {
        "message" : "Wellcome to student Management System" 
    }
class Student(BaseModel):
    name : str
    reg_No : str
    father_name : str
    age : int
    department : str
    semester : str
    cgpa : float

@app.get("/student")
def student_detail():
    return {
        "student_detail" : students
    }
@app.post("/student")
def create_student(std : Student):
    students.append(std.model_dump())
    return{
        "messege" : "student Added Successfully ",
        "student" : std
    }


    
@app.put("/student/{reg_no}")
def update_student(reg_no, update_std : Student):
    
    for std in students :
        if std["reg_No"] == reg_no :
            std.update(update_std.model_dump())
            return{
                "message" : "student detail Updated Successfully" ,
                "student" : std
            }
        
    return{
        "message" : "student not found" 
    }

@app.delete("/student/{reg_no}")
def delete_student(reg_no : str):
    for std in students:

        if std["reg_No"] == reg_no :
            std.remove(std)
            return{
                "messege" : "student deleted SuccessFully",
                 "student" : std
            }
    return {
        "message" : "student not found "
    }

# Library Mangement System 
book_store = []
@app.get("/")
def library():
    return{
        "message" : "Wellcome to Library Management System"
    }
class Book(BaseModel):
    book_id: str
    title: str
    author: str
    price: float
    available: bool

@app.get("/book")
def get_book():
    return {
        "message" : "All Book Detail",
        "Data" : book_store
    }
@app.post("/book")
def create_book(b : Book):
    book_store.append(b.model_dump())
    return {
        "message" : "Book Added to Library Successfully ",
        "detail" : b
    }
@app.put("/book/{id}")
def update_book(id ,book :Book):
    for b in book_store:
        if b["book_id"] == id:
            b.update(book.model_dump())
            return{
                "message" : "Book Detail updated Successfully",
                "updated-detai" : book.model_dump()
            }
        
    return {
        "message" : "Book not found "
    }

@app.delete("/book/{id}")
def delete_book(id :str):
    for book in book_store:
        if book["book_id"] == id :
            book_store.remove(book)
            return{
                "message" : "Book deleted SuccessFully ",
                "detai" : book
            }
    return{
        "message" : "Book Not founded "
    }
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
@app.get("/movies")
def get_movies():
    return {
        "message": "All Movies",
        "data": movie_store
    }


# -----------------------------
# GET MOVIE BY ID
# -----------------------------
@app.get("/movies/{movie_id}")
def get_movie_by_id(movie_id: str):
    for movie in movie_store:
        if movie["movie_id"] == movie_id:
            return {
                "message": "Movie Found",
                "data": movie
            }

    return {
        "message": "Movie not found"
    }


# -----------------------------
# GET MOVIES BY GENRE
# -----------------------------
@app.get("/movies/genre/{genre}")
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

    return {
        "message": "No movies found"
    }


# -----------------------------
# GET AVAILABLE MOVIES
# -----------------------------
@app.get("/movies/available/{available}")
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
@app.get("/movies/rating/{rating}")
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
@app.get("/movies/count")
def total_movies():
    return {
        "total_movies": len(movie_store)
    }


# -----------------------------
# CREATE MOVIE
# -----------------------------
@app.post("/movies", status_code=201)
def create_movie(movie: Movie):
    movie_store.append(movie.model_dump())

    return {
        "message": "Movie added successfully",
        "data": movie
    }


# -----------------------------
# UPDATE MOVIE
# -----------------------------
@app.put("/movies/{movie_id}")
def update_movie(movie_id: str, updated_movie: Movie):

    for movie in movie_store:
        if movie["movie_id"] == movie_id:
            movie.update(updated_movie.model_dump())

            return {
                "message": "Movie updated successfully",
                "data": movie
            }

    return {
        "message": "Movie not found"
    }


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

    return {
        "message": "Movie not found"
    }