print("USER ROUTER LOADED")
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db
from utils import hash

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserResponse
)
def create_user(
    user: schemas.CreateUser,
    db: Session = Depends(get_db)
):

    hashed_password = hash(user.password)

    new_user = models.User(
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user