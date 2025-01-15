from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import config

api = config.TOKEN
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
buttonKB1 = KeyboardButton(text='Рассчитать')
buttonKB2 = KeyboardButton(text='Информация')
kb.add(buttonKB1, buttonKB2)
kb.resize_keyboard = True

ikb = InlineKeyboardMarkup()
buttonIKB1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
buttonIKB2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
ikb.add(buttonIKB1, buttonIKB2)

flagFormula = True

class UserState(StatesGroup):
    age = State()  # Возвраст
    growth = State()  # Рост
    weight = State()  # Вес


@dp.message_handler(commands=['start'])
async def start(message):
    text = "Привет! Я бот помогающий твоему здоровью."
    print(text)
    await message.answer(text, reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    text = "Выберите опцию:"
    print(f"{message.text}\n{text}")
    await message.answer(text, reply_markup=ikb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    global flagFormula
    if flagFormula:
        text = "10 x вес (кг) + 6.25 x рост(см) – 5 x возраст(г) - 161 для жен."
    else:
        text = "10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5 для муж."
    flagFormula = not flagFormula
    print(f"{call.message.text}\n{text}")
    await call.message.answer(text)
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    text = "Введите свой возраст:"
    print(f"{call.message.text}\n{text}")
    await call.message.answer(text)
    await UserState.age.set()
    await call.answer()


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
    global flagFormula
    await state.update_data(weight=message.text)
    data = await state.get_data()
    if not flagFormula:
        text = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161
    else:
        text = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    print(f"{message.text}\n{text}")
    await message.answer(text)
    await state.finish()


@dp.message_handler()
async def all_massages(message):
    text = "Введите команду /start, чтобы начать общение."
    print(f"{message.text}\n{text}")
    await message.answer(text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
