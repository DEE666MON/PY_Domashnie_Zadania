# Название - module_16_2_Validaciua_dannih
# Запуск сервера - uvicorn main:app --reload
# Документация - http://127.0.0.1:8000/docs
from fastapi import FastAPI, Path
from typing import Annotated

# get post put delete

app = FastAPI()


@app.get("/")
async def welcome():
    return "Главная страница."


@app.get("/user/admin")
async def userAdmin():
    return "Вы вошли как администратор."


@app.get("/user/{user_id}")
async def userId(user_id: int = Path(ge=1, le=100, description="Enter User ID",
                                     example="50")):
    return f"Вы вошли как пользователь № {user_id}."


@app.get("/user/{username}/{age}'")
async def userNameAndAge(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
                         age: int = Path(ge=18, le=120, description="Enter age", example="24")):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}."
