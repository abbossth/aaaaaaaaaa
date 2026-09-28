"""'Maktab oshxonasi' boti — reply va inline tugmalar namunasi."""
import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from dotenv import load_dotenv

load_dotenv()
dp = Dispatcher()

MENYU = {
    "osh": ("🍛 Osh", 15000),
    "lagmon": ("🍜 Lag'mon", 14000),
    "somsa": ("🥟 Somsa", 5000),
    "choy": ("🍵 Choy", 2000),
}
savatlar: dict[int, dict[str, int]] = {}  # user_id -> {taom_kodi: soni}


def asosiy_menyu():
    kb = ReplyKeyboardBuilder()
    for matn in ("🍽 Menyu", "🛒 Savat", "📞 Aloqa", "ℹ️ Biz haqimizda"):
        kb.button(text=matn)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def menyu_tugmalari():
    kb = InlineKeyboardBuilder()
    for kod, (nom, narx) in MENYU.items():
        kb.button(text=f"{nom} — {narx:,} so'm", callback_data=f"qosh:{kod}")
    kb.button(text="🛒 Savatni ko'rish", callback_data="savat")
    kb.adjust(1)
    return kb.as_markup()


def savat_matni(user_id: int) -> str:
    savat = savatlar.get(user_id, {})
    if not savat:
        return "🛒 Savat bo'sh"
    qatorlar, jami = [], 0
    for kod, soni in savat.items():
        nom, narx = MENYU[kod]
        qatorlar.append(f"{nom} × {soni} = {narx * soni:,}")
        jami += narx * soni
    return "🛒 Savat:\n" + "\n".join(qatorlar) + f"\n\n💰 Jami: {jami:,} so'm"


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Maktab oshxonasiga xush kelibsiz! 🍽", reply_markup=asosiy_menyu())


@dp.message(F.text == "🍽 Menyu")
async def menyu(message: Message):
    await message.answer("Bugungi menyu:", reply_markup=menyu_tugmalari())


@dp.message(F.text == "🛒 Savat")
async def savat(message: Message):
    await message.answer(savat_matni(message.from_user.id))


@dp.message(F.text == "📞 Aloqa")
async def aloqa(message: Message):
    await message.answer("📞 +998 90 123 45 67\n⏰ 08:00 – 15:00")


@dp.callback_query(F.data.startswith("qosh:"))
async def qosh(callback: CallbackQuery):
    kod = callback.data.split(":")[1]
    savat = savatlar.setdefault(callback.from_user.id, {})
    savat[kod] = savat.get(kod, 0) + 1
    await callback.answer(f"{MENYU[kod][0]} savatga qo'shildi ✅")


@dp.callback_query(F.data == "savat")
async def savat_inline(callback: CallbackQuery):
    kb = InlineKeyboardBuilder()
    kb.button(text="⬅️ Menyuga qaytish", callback_data="menyuga")
    kb.button(text="🗑 Tozalash", callback_data="tozala")
    await callback.message.edit_text(savat_matni(callback.from_user.id), reply_markup=kb.as_markup())
    await callback.answer()


@dp.callback_query(F.data == "menyuga")
async def menyuga(callback: CallbackQuery):
    await callback.message.edit_text("Bugungi menyu:", reply_markup=menyu_tugmalari())
    await callback.answer()


@dp.callback_query(F.data == "tozala")
async def tozala(callback: CallbackQuery):
    savatlar.pop(callback.from_user.id, None)
    await callback.message.edit_text("🗑 Savat tozalandi", reply_markup=menyu_tugmalari())
    await callback.answer()


async def main():
    await dp.start_polling(Bot(token=os.getenv("BOT_TOKEN")))


if __name__ == "__main__":
    asyncio.run(main())
