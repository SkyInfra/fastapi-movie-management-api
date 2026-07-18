from pydantic import BaseModel , EmailStr

class MovieBase(BaseModel):
    title: str
    director: str
    genre: str
    release_year: int
    rating: float
    is_availible: bool


class MovieCreate(MovieBase):
    pass


class MovieResponse(MovieBase):
    movie_id: int

    class Config:
        from_attributes = True


class CreateUser(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    user_id: int
    email: EmailStr

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str