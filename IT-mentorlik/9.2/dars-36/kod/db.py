"""36-dars: bazaga ulanish qatlami (asyncpg). Bot kodi SQL'ni to'g'ridan-to'g'ri yozmaydi — shu funksiyalarni chaqiradi."""
import asyncpg

pool: asyncpg.Pool | None = None


async def ulan(dsn: str) -> None:
    global pool
    pool = await asyncpg.create_pool(dsn, min_size=1, max_size=5)
    with open(__file__.replace("db.py", "schema.sql"), encoding="utf-8") as f:
        await pool.execute(f.read())


async def foydalanuvchi_saqla(telegram_id: int, ism: str, username: str | None) -> None:
    # UPSERT: bor bo'lsa — yangilaydi, yo'q bo'lsa — qo'shadi
    await pool.execute(
        """INSERT INTO foydalanuvchilar (telegram_id, ism, username) VALUES ($1, $2, $3)
           ON CONFLICT (telegram_id) DO UPDATE SET ism = EXCLUDED.ism, username = EXCLUDED.username""",
        telegram_id, ism, username,
    )


async def kitoblar() -> list[asyncpg.Record]:
    return await pool.fetch("SELECT id, nomi, muallif, soni FROM kitoblar ORDER BY nomi")


async def kitob_ol(telegram_id: int, kitob_id: int) -> str:
    """Kitobni ijaraga oladi. Natija: 'ok' | 'tugagan' | 'allaqachon'."""
    async with pool.acquire() as conn:
        async with conn.transaction():          # ikkala amal ham bajariladi yoki hech biri
            bor = await conn.fetchval(
                "SELECT 1 FROM ijaralar WHERE telegram_id=$1 AND kitob_id=$2 AND qaytarilgan IS NULL",
                telegram_id, kitob_id,
            )
            if bor:
                return "allaqachon"
            yangilandi = await conn.execute(
                "UPDATE kitoblar SET soni = soni - 1 WHERE id = $1 AND soni > 0", kitob_id
            )
            if yangilandi == "UPDATE 0":
                return "tugagan"
            await conn.execute(
                "INSERT INTO ijaralar (telegram_id, kitob_id) VALUES ($1, $2)", telegram_id, kitob_id
            )
            return "ok"


async def mening_kitoblarim(telegram_id: int) -> list[asyncpg.Record]:
    return await pool.fetch(
        """SELECT i.id, k.nomi, i.olingan
           FROM ijaralar i JOIN kitoblar k ON k.id = i.kitob_id
           WHERE i.telegram_id = $1 AND i.qaytarilgan IS NULL
           ORDER BY i.olingan""",
        telegram_id,
    )


async def qaytar(telegram_id: int, ijara_id: int) -> bool:
    async with pool.acquire() as conn:
        async with conn.transaction():
            kitob_id = await conn.fetchval(
                """UPDATE ijaralar SET qaytarilgan = now()
                   WHERE id = $1 AND telegram_id = $2 AND qaytarilgan IS NULL
                   RETURNING kitob_id""",
                ijara_id, telegram_id,
            )
            if kitob_id is None:
                return False
            await conn.execute("UPDATE kitoblar SET soni = soni + 1 WHERE id = $1", kitob_id)
            return True


async def statistika() -> asyncpg.Record:
    return await pool.fetchrow(
        """SELECT (SELECT COUNT(*) FROM foydalanuvchilar) AS foydalanuvchilar,
                  (SELECT COUNT(*) FROM ijaralar WHERE qaytarilgan IS NULL) AS qolda,
                  (SELECT k.nomi FROM ijaralar i JOIN kitoblar k ON k.id = i.kitob_id
                   GROUP BY k.nomi ORDER BY COUNT(*) DESC LIMIT 1) AS eng_mashhur"""
    )
