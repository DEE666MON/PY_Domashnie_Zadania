# Название - module_16_1_Osnovi_FastApi_i_marshrytizaciua
# Запуск сервера - uvicorn main:app --reload
# Документация - http://127.0.0.1:8000/docs
from fastapi import FastAPI

# get post put delete

app = FastAPI()


@app.get("/")
async def welcome():
    return "Главная страница."


@app.get("/user/admin")
async def userAdmin():
    return "Вы вошли как администратор."


@app.get("/user/{user_id}")
async def userId(user_id: int):
    return f"Вы вошли как пользователь № {user_id}."


@app.get("/user")
async def userNameAndAge(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}."
