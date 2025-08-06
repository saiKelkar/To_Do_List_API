from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schema, database
from ..controllers import auth_controllers

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup", response_model=schema.UserResponse)
def signup(user: schema.UserCreate, db: Session = Depends(database.get_db)):
    return auth_controllers.signup(user, db)

@router.post("/login", response_model=schema.UserResponse)
def login(user: schema.UserLogin, db: Session = Depends(database.get_db)):
    return auth_controllers.login(user, db)

@router.post("/logout")
def logout(user: schema.UserResponse, db: Session = Depends(database.get_db)):
    return auth_controllers.logout(user, db)