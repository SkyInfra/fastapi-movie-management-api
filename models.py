from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base


class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    director = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    release_year = Column(Integer)
    rating = Column(Float)
    is_availible = Column(Boolean)