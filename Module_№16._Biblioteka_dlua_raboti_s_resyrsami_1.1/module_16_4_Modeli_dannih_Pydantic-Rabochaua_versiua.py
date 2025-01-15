# Название - module_16_4_Modeli_dannih_Pydantic
# Запуск сервера - uvicorn main:app --reload
# Документация - http://127.0.0.1:8000/docs
from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

# get post put delete

app = FastAPI()
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
def get_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
def post_users(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: int = Path(ge=18, le=120, description="Enter age", example="24")) -> User:
    current_user = User(id=len(users) + 1, username=username, age=age)
    users.append(current_user)
    return current_user


@app.put("/user/{user_id}/{username}/{age}")
def put_users(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="50")],
              username: str = Path(min_length=5, max_length=20, description="Enter username",
                                   example="UrbanUser"),
              age: int = Path(ge=18, le=120, description="Enter age", example="24")) -> User:
    try:
        for U in users:
            if user_id == U.id:
                U.username = username
                U.age = age
                return U
        raise IndexError
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found.")


@app.delete("/user/{user_id}")
def delete_users(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="50")]):
    try:
        none_count = 0
        for U in users:
            if users[U.id - 1].id == 0:
                none_count += 1
            if user_id == U.id:
                temp = users[U.id - 1]
                users[U.id - 1] = User(id=0, username="None", age=0)
                return temp
        if none_count == len(users):
            users.clear()
        raise IndexError
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found.")
