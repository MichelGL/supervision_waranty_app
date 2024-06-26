from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

from fastapi_users import fastapi_users, FastAPIUsers
from pydantic import BaseModel, Field

from fastapi import FastAPI, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationException
from fastapi.responses import JSONResponse

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

app = FastAPI(
    title="Construction Supervision and Warranty Service App"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"

# users = [
#     {"id": 1, "role": "admin", "name": "Michel"},
#     {"id": 2, "role": "employee", "name": "Victor"},
#     {"id": 3, "role": "contractor", "name": "Ivan"},
# ]
#
# class Task(BaseModel):
#     id: int
#
#
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     return [user for user in users if user.get("id") == user_id]
#
# @app.post("/users/{user_id}")
# def change_user_name(user_id: int, new_name: str):
#     current_user = list(filter(lambda user: user.get("id") == user_id, users))[0]
#     current_user["name"] = new_name
#     return {"status": 200, "data": current_user}
