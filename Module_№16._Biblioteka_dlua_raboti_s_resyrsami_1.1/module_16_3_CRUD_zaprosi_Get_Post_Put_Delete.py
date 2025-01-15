# Название - module_16_3_CRUD_zaprosi_Get_Post_Put_Delete
# Запуск сервера - uvicorn main:app --reload
# Документация - http://127.0.0.1:8000/docs
from fastapi import FastAPI, Path
from typing import Annotated

# get post put delete

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users():
    return users


@app.post("/user/{username}/{age}")
async def post_users(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: int = Path(ge=18, le=120, description="Enter age", example="24")):
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f"Имя: {username}, возраст: {age}"
    return f"User {current_index} is registered."


@app.put("/user/{user_id}/{username}/{age}")
async def put_users(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="50")],
                    username: str = Path(min_length=5, max_length=20, description="Enter username",
                                         example="UrbanUser"),
                    age: int = Path(ge=18, le=120, description="Enter age", example="24")):
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated."


@app.delete("/user/{user_id}")
async def delete_users(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="50")]):
    users.pop(str(user_id))
    return f"User {user_id} has been deleted."
