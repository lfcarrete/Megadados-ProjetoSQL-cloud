from email.policy import HTTP
from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Gender, Role


app = FastAPI()

db: List[User] = [
    User(
        id = UUID("0422058c-efa8-4a1d-8fae-4229fb6abfe5"),
        first_name = "Jamila",
        last_name = "Ahmed",
        gender = Gender.female,
        roles = [Role.student]
    ),
    User(
        id = UUID("a8db539d-2303-4cda-b174-c7edd84435fd"),
        first_name = "Alex",
        last_name = "Jones",
        gender = Gender.male,
        roles = [Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
    raise HTTPException (
        status_code = 404,
        detail = f"user with id: {user_id} does not exists"
    )