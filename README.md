# 🎬 FastAPI Movie Management API

A beginner-friendly RESTful Movie Management API built with **FastAPI**. This project demonstrates the fundamentals of backend development, including CRUD operations, request validation, HTTP status codes, and exception handling.

## 🚀 Features

- Create a new movie
- Get all movies
- Get a movie by ID
- Filter movies by genre
- Filter available movies
- Filter movies by minimum rating
- Count total movies
- Update movie details
- Delete a movie
- Request validation using Pydantic
- Proper HTTP status codes
- HTTP exception handling

## 🛠️ Technologies Used

- Python 3
- FastAPI
- Pydantic
- Uvicorn
- Postman

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/movies` | Get all movies |
| GET | `/movies/{movie_id}` | Get movie by ID |
| GET | `/movies/genre/{genre}` | Get movies by genre |
| GET | `/movies/available/{available}` | Get available/unavailable movies |
| GET | `/movies/rating/{rating}` | Get movies with minimum rating |
| GET | `/movies/count` | Get total number of movies |
| POST | `/movies` | Add a new movie |
| PUT | `/movies/{movie_id}` | Update movie details |
| DELETE | `/movies/{movie_id}` | Delete a movie |

## ▶️ Run the Project

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-movie-management-api.git
```

Navigate to the project:

```bash
cd fastapi-movie-management-api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

Run the server:

```bash
uvicorn main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/docs
```

to access the interactive Swagger UI.

## 📖 What I Learned

Through this project, I learned:

- Building REST APIs with FastAPI
- CRUD operations
- Pydantic request validation
- HTTP Status Codes
- HTTP Exceptions
- Path Parameters
- Testing APIs using Postman

## 👨‍💻 Author

**Muhammad Haseeb Akhtar**

Software Engineering Student | Backend & Cloud Computing Enthusiast
