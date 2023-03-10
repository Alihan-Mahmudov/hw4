from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

Token = config('TOKEN')

bot = Bot(Token)
dp = Dispatcher(bot = bot,storage=storage)
ADMINS = [5170771003,]
DICES = ['🎲','🎯','🎳','🎰','⚽','🏀']