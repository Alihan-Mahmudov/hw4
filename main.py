from aiogram.utils import executor
from hendlers import client, callback, extra, admin, fsm_anketa
from config import dp
import logging

client.regiser_hendlers_client(dp)
callback.register_hendler_callback(dp)
admin.register_admin_hendlers(dp)
fsm_anketa.register_handlers_fsm_anketa(dp)

extra.register_hendler_extra(dp)

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)