"""8.2 — birinchi Telegram bot (aiogram 3)."""
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message) -> None:
    ism = message.from_user.first_name
    await message.answer(
        f"Assalomu alaykum, {ism}! 👋\n"
        "Men 8.2 guruhining birinchi botiman.\n"
        "Buyruqlar ro'yxati: /help"
    )


@dp.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(
        "📋 Buyruqlar:\n"
        "/start — boshlash\n"
        "/help — yordam\n"
        "/about — bot haqida\n\n"
        "Istalgan matn yozsangiz, uni qaytaraman 🔁"
    )


@dp.message(Command("about"))
async def cmd_about(message: Message) -> None:
    await message.answer("🤖 Aiogram 3 bilan Python'da yozilgan. Muallif: 8.2 o'quvchisi")


@dp.message(F.text)
async def echo(message: Message) -> None:
    await message.answer(f"Siz yozdingiz: {message.text}")


@dp.message()
async def boshqa(message: Message) -> None:
    await message.answer("Hozircha faqat matnni tushunaman 🙂")


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
