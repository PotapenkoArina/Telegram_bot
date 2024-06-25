from .dispatcher_bot import dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from .keyboard_bot import main_inline_keyboard

@dispatcher.message(CommandStart())
async def start_bot(message: Message):
    await message.answer(text= "Hello, User!", reply_markup = main_inline_keyboard)