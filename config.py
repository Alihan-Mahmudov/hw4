from aiogram import Bot, Dispatcher, types
from decouple import config


TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
ADMINS = [5170771003, ]