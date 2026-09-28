"""db.py ni botsiz sinash: python sinov.py (DATABASE_URL .env da)."""
import asyncio
import os

from dotenv import load_dotenv

import db


async def main():
    load_dotenv()
    await db.ulan(os.getenv("DATABASE_URL"))
    await db.foydalanuvchi_saqla(1, "Test O'quvchi", "test")
    kitob = (await db.kitoblar())[0]
    print("Olish:", await db.kitob_ol(1, kitob["id"]))
    print("Yana olish:", await db.kitob_ol(1, kitob["id"]))
    mening = await db.mening_kitoblarim(1)
    print("Menda:", [m["nomi"] for m in mening])
    print("Qaytarish:", await db.qaytar(1, mening[0]["id"]))
    print("Statistika:", dict(await db.statistika()))


asyncio.run(main())
