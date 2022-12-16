
from config import bot, ADMINS
from aiogram import types, Dispatcher

async def pin_hendler(message: types.Message):
    if message.from_user.id in ADMINS:
        await bot.pin_chat_message(message.chat.id, message.message_id)

def register_admin_hendlers(dp: Dispatcher):
    dp.register_message_handler(pin_hendler, commands="pin")