"""36-dars: "Kutubxona bot" — aiogram 3 + PostgreSQL (asyncpg).
.env:  BOT_TOKEN=...   DATABASE_URL=postgresql://postgres:parol@localhost:5432/kutubxona
"""
import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from dotenv import load_dotenv

import db

load_dotenv()
dp = Dispatcher()


def menyu():
    kb = ReplyKeyboardBuilder()
    kb.button(text="📚 Kitoblar")
    kb.button(text="🎒 Mening kitoblarim")
    kb.button(text="📊 Statistika")
    kb.adjust(2, 1)
    return kb.as_markup(resize_keyboard=True)


@dp.message(CommandStart())
async def start(message: Message):
    u = message.from_user
    await db.foydalanuvchi_saqla(u.id, u.full_name, u.username)
    await message.answer(f"📖 Maktab kutubxonasiga xush kelibsiz, {u.first_name}!", reply_markup=menyu())


@dp.message(F.text == "📚 Kitoblar")
async def kitoblar(message: Message):
    kb = InlineKeyboardBuilder()
    qatorlar = []
    for k in await db.kitoblar():
        belgi = "✅" if k["soni"] > 0 else "⛔"
        qatorlar.append(f"{belgi} <b>{k['nomi']}</b> — {k['muallif']} ({k['soni']} ta)")
        if k["soni"] > 0:
            kb.button(text=f"📥 {k['nomi']}", callback_data=f"ol:{k['id']}")
    kb.adjust(1)
    await message.answer("\n".join(qatorlar), reply_markup=kb.as_markup(), parse_mode="HTML")


@dp.callback_query(F.data.startswith("ol:"))
async def ol(callback: CallbackQuery):
    natija = await db.kitob_ol(callback.from_user.id, int(callback.data.split(":")[1]))
    xabarlar = {
        "ok": "✅ Kitob sizga berildi! 14 kun ichida qaytaring.",
        "tugagan": "😔 Afsuski, bu kitob tugagan.",
        "allaqachon": "📕 Bu kitob allaqachon sizda.",
    }
    await callback.answer(xabarlar[natija], show_alert=True)


@dp.message(F.text == "🎒 Mening kitoblarim")
async def mening(message: Message):
    ijaralar = await db.mening_kitoblarim(message.from_user.id)
    if not ijaralar:
        return await message.answer("Sizda hozircha kitob yo'q 📭")
    kb = InlineKeyboardBuilder()
    for i in ijaralar:
        kb.button(text=f"↩️ Qaytarish: {i['nomi']}", callback_data=f"qaytar:{i['id']}")
    kb.adjust(1)
    matn = "\n".join(f"📕 {i['nomi']} — {i['olingan']:%d.%m.%Y}" for i in ijaralar)
    await message.answer(matn, reply_markup=kb.as_markup())


@dp.callback_query(F.data.startswith("qaytar:"))
async def qaytar(callback: CallbackQuery):
    ok = await db.qaytar(callback.from_user.id, int(callback.data.split(":")[1]))
    await callback.answer("✅ Rahmat, qaytarildi!" if ok else "Bu ijara topilmadi", show_alert=True)
    if ok:
        await callback.message.delete()


@dp.message(F.text == "📊 Statistika")
@dp.message(Command("stat"))
async def stat(message: Message):
    s = await db.statistika()
    await message.answer(
        f"👥 Foydalanuvchilar: {s['foydalanuvchilar']}\n"
        f"📚 Hozir qo'lda: {s['qolda']} ta kitob\n"
        f"🔥 Eng mashhur: {s['eng_mashhur'] or '—'}"
    )


async def main():
    await db.ulan(os.getenv("DATABASE_URL"))
    await dp.start_polling(Bot(os.getenv("BOT_TOKEN")))


if __name__ == "__main__":
    asyncio.run(main())
