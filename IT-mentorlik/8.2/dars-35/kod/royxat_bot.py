"""FSM namunasi: IT to'garagiga ro'yxatdan o'tish boti (aiogram 3)."""
import asyncio
import json
import os
from pathlib import Path

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from dotenv import load_dotenv

load_dotenv()
router = Router()
FAYL = Path(__file__).parent / "royxat.json"
YONALISHLAR = ["Web", "Python", "Telegram bot", "Dizayn"]


class Royxat(StatesGroup):
    ism = State()
    yosh = State()
    yonalish = State()
    telefon = State()
    tasdiq = State()


def saqlash(yozuv: dict) -> None:
    data = json.loads(FAYL.read_text(encoding="utf-8")) if FAYL.exists() else []
    data.append(yozuv)
    FAYL.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Salom! IT to'garagiga yozilish uchun /register\nBekor qilish: /cancel")


@router.message(Command("cancel"))
async def cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("❌ Bekor qilindi", reply_markup=ReplyKeyboardRemove())


@router.message(Command("register"))
async def boshla(message: Message, state: FSMContext):
    await state.set_state(Royxat.ism)
    await message.answer("1/4. Ism va familiyangiz?")


@router.message(Royxat.ism, F.text)
async def ism_ol(message: Message, state: FSMContext):
    ism = message.text.strip()
    if len(ism) < 3 or any(c.isdigit() for c in ism):
        return await message.answer("Iltimos, to'g'ri ism kiriting (kamida 3 harf, raqamsiz)")
    await state.update_data(ism=ism.title())
    await state.set_state(Royxat.yosh)
    await message.answer("2/4. Yoshingiz?")


@router.message(Royxat.yosh, F.text)
async def yosh_ol(message: Message, state: FSMContext):
    if not message.text.isdigit() or not 10 <= int(message.text) <= 18:
        return await message.answer("Yosh 10 dan 18 gacha son bo'lishi kerak")
    await state.update_data(yosh=int(message.text))
    kb = InlineKeyboardBuilder()
    for y in YONALISHLAR:
        kb.button(text=y, callback_data=f"yon:{y}")
    kb.adjust(2)
    await state.set_state(Royxat.yonalish)
    await message.answer("3/4. Yo'nalishni tanlang:", reply_markup=kb.as_markup())


@router.callback_query(Royxat.yonalish, F.data.startswith("yon:"))
async def yonalish_ol(callback: CallbackQuery, state: FSMContext):
    await state.update_data(yonalish=callback.data.split(":", 1)[1])
    await callback.message.edit_reply_markup()
    kb = ReplyKeyboardBuilder()
    kb.button(text="📱 Raqamni yuborish", request_contact=True)
    await state.set_state(Royxat.telefon)
    await callback.message.answer("4/4. Telefon raqamingizni yuboring:", reply_markup=kb.as_markup(resize_keyboard=True, one_time_keyboard=True))
    await callback.answer()


@router.message(Royxat.telefon, F.contact)
async def telefon_ol(message: Message, state: FSMContext):
    await state.update_data(telefon=message.contact.phone_number)
    d = await state.get_data()
    kb = InlineKeyboardBuilder()
    kb.button(text="✅ Tasdiqlash", callback_data="ha")
    kb.button(text="🔁 Qaytadan", callback_data="yoq")
    await state.set_state(Royxat.tasdiq)
    await message.answer("Ma'lumotlar qabul qilindi", reply_markup=ReplyKeyboardRemove())
    await message.answer(
        f"Tekshiring:\n👤 {d['ism']}\n🎂 {d['yosh']}\n💻 {d['yonalish']}\n📱 {d['telefon']}",
        reply_markup=kb.as_markup(),
    )


@router.message(Royxat.telefon)
async def telefon_notogri(message: Message):
    await message.answer("Iltimos, pastdagi 📱 tugmani bosing")


@router.callback_query(Royxat.tasdiq, F.data.in_({"ha", "yoq"}))
async def tasdiq(callback: CallbackQuery, state: FSMContext):
    if callback.data == "ha":
        saqlash({**(await state.get_data()), "user_id": callback.from_user.id})
        await callback.message.edit_text("🎉 Ro'yxatdan o'tdingiz! Tez orada bog'lanamiz.")
        await state.clear()
    else:
        await state.set_state(Royxat.ism)
        await callback.message.edit_text("Qaytadan boshlaymiz. Ismingiz?")
    await callback.answer()


async def main():
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(Bot(token=os.getenv("BOT_TOKEN")))


if __name__ == "__main__":
    asyncio.run(main())
