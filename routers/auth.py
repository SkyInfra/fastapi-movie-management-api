print("AUTH ROUTER LOADED")
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from oauth2 import create_access_token
import models
import schemas
from database import get_db
from utils import verify

router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)


@router.post("/")
def login(user: schemas.UserLogin,
          db: Session = Depends(get_db)):

    db_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Credentials"
        )

    if not verify(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials"
        )

    access_token = create_access_token(
    data={"user_id": db_user.user_id}
)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }