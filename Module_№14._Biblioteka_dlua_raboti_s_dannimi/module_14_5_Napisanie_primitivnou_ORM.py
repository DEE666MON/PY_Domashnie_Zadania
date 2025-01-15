from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import config
from crud_functions import *

api = config.TOKEN
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
buttonKB1 = KeyboardButton(text='Рассчитать')
buttonKB2 = KeyboardButton(text='Информация')
buttonKB3 = KeyboardButton(text='Купить')
buttonKB4 = KeyboardButton(text='Регистрация')
kb.add(buttonKB1, buttonKB2, buttonKB3, buttonKB4)
kb.resize_keyboard = True

ikb1 = InlineKeyboardMarkup()
ikb2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Таблеточка1', callback_data='product_buying'),
         InlineKeyboardButton(text='Таблеточка2', callback_data='product_buying'),
         InlineKeyboardButton(text='Таблеточка3', callback_data='product_buying'),
         InlineKeyboardButton(text='Таблеточка4', callback_data='product_buying')]
    ]
)
buttonIKB1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
buttonIKB2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
ikb1.add(buttonIKB1, buttonIKB2)

flagFormula = True


class UserState(StatesGroup):
    age = State()  # Возвраст
    growth = State()  # Рост
    weight = State()  # Вес


class RegistrationState(StatesGroup):
    username = State()  # Название
    email = State()  # Почта
    age = State()  # Возвраст
    balance = 1000  # Баланс/Счёт


@dp.message_handler(commands=['start'])
async def start(message):
    text = "Привет! Я бот помогающий твоему здоровью."
    print(text)
    await message.answer(text, reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    text = "Выберите опцию:"
    print(f"{message.text}\n{text}")
    await message.answer(text, reply_markup=ikb1)


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


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    print(message.text)
    allP = get_all_products()
    for i in range(4):
        text = f"Название: {allP[i][1]} | Описание: {allP[i][2]} | Цена: {allP[i][3]}"
        print(text)
        await message.answer(text)
        with open(f"img/{i + 1}.jpg", "rb") as img:
            await message.answer_photo(img)
    await message.answer("Выберите продукт для покупки:", reply_markup=ikb2)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    text = "Вы успешно приобрели продукт!"
    print(f"{call.message.text}\n{text}")
    await call.message.answer(text)
    await call.answer()


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    text = "Введите имя пользователя (только латинский алфавит):"
    print(f"{message.text}\n{text}")
    await message.answer(text)
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    text1 = "Пользователь существует, введите другое имя."
    text2 = "Введите свой email:"
    if is_included(message.text):
        print(f"{message.text}\n{text1}")
        await message.answer(text1)
    else:
        await state.update_data(username=message.text)
        print(f"{message.text}\n{text2}")
        await message.answer(text2)
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    text = "Введите свой возраст:"
    print(f"{message.text}\n{text}")
    await message.answer(text)
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_email(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(str(data['username']), str(data['email']), int(data['age']))
    text = "Регистрация прошла успешно."
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
    connection.close()
