import aiogram
from .buttons_bot import buttons_start, button_get_users, button_delete_user, button_is_admin

main_keyboard = aiogram.types.ReplyKeyboardMarkup(
    keyboard = [
        [buttons_start]
    ]
)

main_inline_keyboard = aiogram.types.InlineKeyboardMarkup(
    inline_keyboard = [
        [button_get_users]
    ]
)