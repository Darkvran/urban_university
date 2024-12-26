#Python ver. 3.13

from aiogram import Bot, Dispatcher
import asyncio
from aiogram.types import Message
from aiogram.filters import CommandStart

bot = Bot(token="7724426276:AAG6TQu6u9qG_jC11eynrNyRcgxNUWwlf8g")

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    print("Привет! Я бот помогающий твоему здоровью.")

@dp.message()
async def command_start_handler(message: Message) -> None:
    print("Введите команду /start, чтобы начать общение.")



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())