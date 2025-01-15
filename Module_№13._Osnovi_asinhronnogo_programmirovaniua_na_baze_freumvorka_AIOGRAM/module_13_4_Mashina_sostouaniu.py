from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()  # Возвраст
    growth = State()  # Рост
    weight = State()  # Вес


@dp.message_handler(commands=['start'])
async def start(message):
    text = "Привет! Я бот помогающий твоему здоровью."
    print(text)
    await message.answer(text)


@dp.message_handler(text='Calories')
async def set_age(message):
    text = "Введите свой возраст:"
    print(text)
    await message.answer(text)
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    text = "Введите свой рост:"
    print(f"{message.text}\n{text}")
    await message.answer(text)
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    text = "Введите свой вес:"
    print(f"{message.text}\n{text}")
    await message.answer(text)
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    text = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5

    # 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5 - упрощённая формула Миффлина-Сан Жеора
    # для мужчин: (10 x вес (кг) + 6.25 x рост(см) – 5 x возраст(г) + 5) x A;
    # для женщин: (10 x вес (кг) + 6.25 x рост(см) – 5 x возраст(г) - 161) x A;
    # Минимальная активность: A = 1.2
    # Слабая активность: A = 1.375
    # Средняя активность: A = 1.55
    # Высокая активность: A = 1.725
    # Экстра-активность: A = 1.9 (под эту категорию обычно подпадают люди, занимающиеся, например, тяжелой атлетикой, или другими силовыми видами спорта с ежедневными тренировками, а также те, кто выполняет тяжелую физическую работу).

    print(f"{message.text}\n{text}")
    await message.answer(text)
    await state.finish()


@dp.message_handler()
async def all_massages(message):
    text = "Введите команду /start, чтобы начать общение."
    print(text)
    await message.answer(text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
