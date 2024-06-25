import aiogram
from .dispatcher_bot import dispatcher
from aiogram.types import Message
from .loader import loader_file

@dispatcher.message()
async def message_handler(message: Message):
    if message.text == "START" or message.text == '/startbot':
        await message.answer(text= "Choose the question in menu: ")
        await message.answer_photo(photo= loader_file(file_name= 'orig.png'), caption= 'MOTI')
