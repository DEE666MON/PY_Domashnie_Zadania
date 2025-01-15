# Название - module_16_5_Shablonizator_Jinja_2
# Запуск сервера - uvicorn main:app --reload
# Документация - http://127.0.0.1:8000/docs
from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated
from pydantic import BaseModel

# get post put delete

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
templates = Jinja2Templates(directory="templates")
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
def get_main(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("user.html", {"request": request, "users": users})


@app.get(path="/user/{user_id}")
def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("user.html", {"request": request, "user": users[user_id - 1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found.")


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
