"""Hakaton bot shabloni (aiogram 3)."""
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import start

load_dotenv()


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    dp = Dispatcher()
    dp.include_router(start.router)
    # dp.include_router(boshqa.router)  # yangi handler fayllarini shu yerga qo'shing
    await dp.start_polling(Bot(token=os.getenv("BOT_TOKEN")))


if __name__ == "__main__":
    asyncio.run(main())
