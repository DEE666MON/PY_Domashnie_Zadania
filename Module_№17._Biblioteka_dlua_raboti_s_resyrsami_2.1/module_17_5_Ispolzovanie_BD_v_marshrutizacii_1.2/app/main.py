# Запуск сервера python -m uvicorn app.main:app
# Создание виртуального окружения python -m venv .venv
# Вход в виртуальное окружение .venv\Scripts\activate.bat или .venv\Scripts\activate
from fastapi import FastAPI
from .routers import task
from .routers import user

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user.router)
app.include_router(task.router)
