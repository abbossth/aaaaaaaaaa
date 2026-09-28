"""8.2 — 34-dars: inline tugmali viktorina bot (challenge asosi)."""
import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv

load_dotenv()
dp = Dispatcher()

SAVOLLAR = [
    ("HTML nimaning qisqartmasi?", ["HyperText Markup Language", "High Tech Modern Language", "Home Tool Markup Language"], 0),
    ("Python'da ro'yxat qaysi qavsda yoziladi?", ["{ }", "[ ]", "( )"], 1),
    ("CSS'da matn rangini qaysi xossa o'zgartiradi?", ["background", "font", "color"], 2),
    ("JS'da o'zgarmas o'zgaruvchi?", ["const", "let", "var"], 0),
    ("Telegram bot tokenini qayerdan olamiz?", ["@BotFather", "@TokenBot", "Google"], 0),
]
natijalar: dict[int, dict] = {}  # user_id -> {"savol": 0, "ball": 0}


def savol_tugmalari(n: int):
    kb = InlineKeyboardBuilder()
    for i, variant in enumerate(SAVOLLAR[n][1]):
        kb.button(text=variant, callback_data=f"javob:{n}:{i}")
    kb.adjust(1)
    return kb.as_markup()


async def savol_yubor(message: Message, user_id: int):
    n = natijalar[user_id]["savol"]
    await message.answer(f"❓ {n + 1}/{len(SAVOLLAR)}. {SAVOLLAR[n][0]}", reply_markup=savol_tugmalari(n))


@dp.message(CommandStart())
async def start(message: Message):
    natijalar[message.from_user.id] = {"savol": 0, "ball": 0}
    await message.answer("🧠 IT viktorinaga xush kelibsiz! 5 ta savol.")
    await savol_yubor(message, message.from_user.id)


@dp.callback_query(F.data.startswith("javob:"))
async def javob(callback: CallbackQuery):
    _, n, tanlov = callback.data.split(":")
    n, tanlov = int(n), int(tanlov)
    holat = natijalar.get(callback.from_user.id)
    if holat is None or holat["savol"] != n:          # eski tugma qayta bosildi
        return await callback.answer("Bu savolga javob berilgan ⏭")

    togri = SAVOLLAR[n][2]
    if tanlov == togri:
        holat["ball"] += 1
        await callback.answer("✅ To'g'ri!")
    else:
        await callback.answer(f"❌ Noto'g'ri. Javob: {SAVOLLAR[n][1][togri]}", show_alert=True)

    await callback.message.edit_reply_markup(reply_markup=None)   # tugmalarni olib tashlash
    holat["savol"] += 1
    if holat["savol"] < len(SAVOLLAR):
        await savol_yubor(callback.message, callback.from_user.id)
    else:
        await callback.message.answer(f"🏁 Natija: {holat['ball']}/{len(SAVOLLAR)}\nQayta o'ynash: /start")


async def main():
    await dp.start_polling(Bot(os.getenv("BOT_TOKEN")))


if __name__ == "__main__":
    asyncio.run(main())
