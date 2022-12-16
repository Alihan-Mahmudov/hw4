from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from config import bot, dp
from aiogram import types, Dispatcher


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_1)

    question = "Где проходит чемпионат мира по футболу в 2022г?"
    answers = [
        "Венгрия",
        "Испания",
        "США",
        "Катар",
        "Франция",
        "Иран",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Воллейбол не смотрим да",
        open_period=5,
        reply_markup=markup
    )

async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_3")
    markup.add(button_call_1)

    question = 'Угадай число'
    answers = [
        "1",
        "54",
        "76",
        "37",
        "6534",
        "43",
        "76",
        "14",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=5,
        explanation="ахахахахаххааххаах",
        open_period=5,
        reply_markup=markup
    )

async def quiz_4(call: types.CallbackQuery):
    # markup = InlineKeyboardMarkup()
    # button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    # markup.add(button_call_2)

    question = 'Сколиько мне лет?'
    answers = [
        "1",
        "54",
        "76",
        "13"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="ахахахахаххааххаах",
        open_period=5
    )


def register_hendler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(quiz_3, text="button_call_2")
    dp.register_callback_query_handler(quiz_4)