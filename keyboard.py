from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
)

# REPLY_KEYBOARDS
main_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="/team_members")
        ],
        [
            KeyboardButton(text="/documentation"),
           KeyboardButton(text="/presentation"),
        ],
        [
            KeyboardButton(text="/help")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Choose one option",
)
