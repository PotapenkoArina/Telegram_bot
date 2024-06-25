from aiogram.types import CallbackQuery
from .dispatcher_bot import dispatcher
from .keyboard_bot import main_keyboard, main_inline_keyboard
from .buttons_bot import button_delete_user, button_is_admin
import sqlite3

@dispatcher.callback_query()
async def callback_handler(callback: CallbackQuery):
    if callback.data == 'users':
        
        data_base = sqlite3.connect(database = 'flask_cookie_test/project/data.db' )
        cursor = data_base.cursor()
        cursor.execute('SELECT * FROM user')
        data_users = cursor.fetchall()
        main_inline_keyboard.inline_keyboard[0] = [button_delete_user, button_is_admin]

        for user in data_users:
            await callback.message.answer(
                text= user[1],
                reply_markup = main_inline_keyboard
            )

