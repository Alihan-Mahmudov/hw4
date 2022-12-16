from config import bot, ADMINS
from aiogram import types, Dispatcher
import random


async def echo(message: types.Message):
    if message.from_user.id in ADMINS:
        if message.text.startswith('game'):
            await bot.send_dice(message.chat.id, emoji=('🏀','🎲','⚽','🎯','🎳️','🎰') )

    elif message.text.isnumeric():
        await bot.send_message(chat_id=message.from_user.id, text=int(message.text) ** 2)
    else:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)



def register_hendler_extra(dp: Dispatcher):
        dp.register_message_handler(echo)
