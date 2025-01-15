from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from ..backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from ..models.user import *
from ..models.task import *
from ..schemas import CreateTask, UpdateTask
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    all_t = db.scalars(select(Task)).all()
    if all_t is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Tasks was not found.'
        )
    return all_t


@router.get("/task_id")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task_by = db.scalar(select(Task).where(Task.id == task_id))
    if task_by is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found.'
        )
    return task_by


@router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], user_ID: int, create_task: CreateTask):
    db.execute(insert(Task).values(title=create_task.title, content=create_task.content, priority=create_task.priority,
                                   user_id=user_ID, slug=slugify(create_task.title+create_task.content)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, update_task: UpdateTask):
    update_t = db.scalar(select(Task).where(Task.id == task_id))
    if update_t is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found.'
        )
    db.execute(update(Task).where(Task.id == task_id).values(title=update_task.title, content=update_task.content,
                                                             priority=update_task.priority,
                                                             slug=slugify(update_task.title+update_task.content)))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task update is successful!'
    }


@router.delete("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    delete_t = db.scalar(select(Task).where(Task.id == task_id))
    if delete_t is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found.'
        )
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task delete is successful!'
    }
