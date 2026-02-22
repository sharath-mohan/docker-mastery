from schema.schema import UserCreate, UserUpdate
from fastapi import FastAPI
from db.db import DB_URL, SessionDep
from models.models import User, Base
from db.db import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": DB_URL}


@app.get("/users")
def read_users(db: SessionDep):
    users = db.query(User).all()
    return users


@app.post("/users")
def create_user(user: UserCreate, db: SessionDep):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate, db: SessionDep):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return {"error": "User not found"}
    db_user.name = user.name
    db_user.email = user.email
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: SessionDep):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return {"error": "User not found"}
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}
