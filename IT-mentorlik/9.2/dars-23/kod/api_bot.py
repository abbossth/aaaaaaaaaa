"""Tashqi API bilan ishlaydigan bot: valyuta kursi va ob-havo (aiogram 3 + aiohttp)."""
import asyncio
import json
import os
import time
from pathlib import Path

import aiohttp
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv

load_dotenv()
router = Router()

SHAHARLAR = {
    "Toshkent": (41.31, 69.28), "Samarqand": (39.65, 66.96), "Buxoro": (39.77, 64.42),
    "Andijon": (40.78, 72.34), "Namangan": (41.00, 71.67), "Nukus": (42.46, 59.60),
}
SOZLAMALAR = Path(__file__).parent / "sozlamalar.json"
_kesh: dict = {"vaqt": 0.0, "kurslar": None}


async def get_json(url: str, params: dict | None = None):
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(url, params=params) as resp:
            resp.raise_for_status()
            return await resp.json(content_type=None)


async def kurslar() -> dict[str, float]:
    if _kesh["kurslar"] is None or time.time() - _kesh["vaqt"] > 1800:
        data = await get_json("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
        _kesh["kurslar"] = {v["Ccy"]: float(v["Rate"]) for v in data}
        _kesh["vaqt"] = time.time()
    return _kesh["kurslar"]


def sozlama_ol(user_id: int) -> dict:
    data = json.loads(SOZLAMALAR.read_text(encoding="utf-8")) if SOZLAMALAR.exists() else {}
    return data.get(str(user_id), {})


def sozlama_saqla(user_id: int, **kv) -> None:
    data = json.loads(SOZLAMALAR.read_text(encoding="utf-8")) if SOZLAMALAR.exists() else {}
    data.setdefault(str(user_id), {}).update(kv)
    SOZLAMALAR.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("💱 /kurs — valyuta kurslari\n💱 /kurs 100 USD — konvertatsiya\n🌤 /havo — ob-havo\n📍 /shahar — shaharni tanlash")


@router.message(Command("kurs"))
async def kurs(message: Message, command: CommandObject):
    try:
        k = await kurslar()
    except (aiohttp.ClientError, TimeoutError, KeyError, ValueError):
        return await message.answer("😔 Markaziy bank serveri javob bermadi. Keyinroq urinib ko'ring.")

    if command.args:  # /kurs 100 USD
        try:
            miqdor, valyuta = command.args.split()
            summa = float(miqdor) * k[valyuta.upper()]
            return await message.answer(f"{miqdor} {valyuta.upper()} = {summa:,.0f} so'm")
        except (ValueError, KeyError):
            return await message.answer("Format: /kurs 100 USD")

    qatorlar = [f"{e} {v}: {k[v]:,.2f} so'm" for e, v in (("🇺🇸", "USD"), ("🇪🇺", "EUR"), ("🇷🇺", "RUB"), ("🇰🇿", "KZT")) if v in k]
    await message.answer("💱 Markaziy bank kurslari:\n" + "\n".join(qatorlar))


@router.message(Command("shahar"))
async def shahar_tanlash(message: Message):
    kb = InlineKeyboardBuilder()
    for nom in SHAHARLAR:
        kb.button(text=nom, callback_data=f"shahar:{nom}")
    kb.adjust(3)
    await message.answer("Shaharingizni tanlang:", reply_markup=kb.as_markup())


@router.callback_query(F.data.startswith("shahar:"))
async def shahar_saqla(callback: CallbackQuery):
    nom = callback.data.split(":", 1)[1]
    sozlama_saqla(callback.from_user.id, shahar=nom)
    await callback.message.edit_text(f"✅ Shahar saqlandi: {nom}. Endi /havo")
    await callback.answer()


@router.message(Command("havo"))
async def havo(message: Message):
    nom = sozlama_ol(message.from_user.id).get("shahar", "Toshkent")
    lat, lon = SHAHARLAR[nom]
    try:
        d = await get_json(
            "https://api.open-meteo.com/v1/forecast",
            {"latitude": lat, "longitude": lon, "current": "temperature_2m,wind_speed_10m", "timezone": "auto"},
        )
    except (aiohttp.ClientError, TimeoutError):
        return await message.answer("😔 Ob-havo serveri javob bermadi")
    c = d["current"]
    await message.answer(f"🌤 {nom}: {c['temperature_2m']}°C, 💨 {c['wind_speed_10m']} km/soat")


async def main():
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(Bot(token=os.getenv("BOT_TOKEN")))


if __name__ == "__main__":
    asyncio.run(main())
