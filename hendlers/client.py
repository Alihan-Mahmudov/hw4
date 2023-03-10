from aiogram import types,Dispatcher
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from config import bot, dp
from keyboards.client_kb import start_markup
from database import db_bot

@dp.message_handler(commands = ['start'])
async def comands(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=f' type /quiz to start quiz'
                                                              f' /meme to get photo'
                                                              f' /audio to get good song',
                           reply_markup=start_markup)
@dp.message_handler(commands = ['quiz'])
async def quiz_1(message:types.Message):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Next', callback_data='button1')
    markup.add(button1)
    question = 'Какое слово надо использовать после слова "Бургер'
    answers = [
        'Кинг',
        'Кортошка Фри',
        'Супер',
        'Пицца',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question = question,
        options = answers,
        is_anonymous = False,
        type = 'quiz',
        correct_option_id=0,
        open_period=15,
        reply_markup = markup
    )
@dp.message_handler(commands = ['meme'])
async def Burger_King(message: types.Message):
    photo = open('media/Bez-nazvaniya-34.webp','rb')
    await bot.send_photo(message.from_user.id,photo = photo)

@dp.message_handler(commands = ['audio'])
async def Burger_King_audio1(message: types.Message):
    photo = open('media/murder brg.mp3','rb')
    markup1 = InlineKeyboardMarkup()
    buttonaud = InlineKeyboardButton('Next', callback_data='buttonaud')
    markup1.add(buttonaud)
    await bot.send_audio(message.from_user.id,audio = photo,reply_markup=markup1)

async def get_random_user(message: types.Message):
    await db_bot.sql_command_random(message)

def register_handlers_client(dp:Dispatcher):
    dp.message_handler(comands,commands=['start'])
    dp.message_handler(quiz_1,commands=['quiz'])
    dp.message_handler(Burger_King,commands=['meme'])
    dp.message_handler(Burger_King_audio1,commands=['audio'])
    dp.register_message_handler(get_random_user, commands=['get'])


