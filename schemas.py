from pydantic import BaseModel


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