from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2
)

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")
mem_button = KeyboardButton("/mem")

share_location = KeyboardButton("/location", request_location=True)
share_contact = KeyboardButton("/phon", request_contact=True)

start_markup.add(mem_button, quiz_button,
                 share_location, share_contact)

cancel_button = KeyboardButton('CANCEL')
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(cancel_button)

d_backend = KeyboardButton("Backand")
d_android = KeyboardButton("Android")
d_uxui = KeyboardButton("UXUI")
d_drugoe = KeyboardButton("Другое")

gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(d_backend, d_android, d_uxui, d_drugoe, cancel_button)


submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('ДА'), KeyboardButton('НЕТ'))