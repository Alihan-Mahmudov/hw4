from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from config import bot, ADMINS
from aiogram import types, Dispatcher
from keyboards.client_kb import start_markup



async def start_hendler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="hi",
                           reply_markup=start_markup)
async def pin_hendler(message: types.Message):
    if message.from_user.id in ADMINS:
        await bot.pin_chat_message(chat_id=message.reply_to_message.from_user.id)

async def send_image(message: types.Message):
    photo = open('media/Bez-nazvaniya-34.webp', 'rb')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Сколько лет Роналду?"
    answers = [
        '44',
        '40',
        '37',
        '55',
        '69',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Ок",
        open_period=5,
        reply_markup=markup
    )

def regiser_hendlers_client(dp: Dispatcher):
    dp.register_message_handler(start_hendler, commands=['start', 'help'])
    dp.register_message_handler(send_image, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(pin_hendler, commands=['pin'])


