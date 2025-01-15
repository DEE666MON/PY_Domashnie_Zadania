from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    text = "Привет! Я бот помогающий твоему здоровью."
    print(text)
    await message.answer(text)


@dp.message_handler()
async def all_massages(message):
    text = "Введите команду /start, чтобы начать общение."
    print(text)
    await message.answer(text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
