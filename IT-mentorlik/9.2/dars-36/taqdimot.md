# 36-dars slaydlari: Bot + PostgreSQL 🤖🐘

## 1-slayd
💥 2 foydalanuvchi bir vaqtda → `royxat.json` buzildi. **Bazaga o'tamiz!**

## 2-slayd — Arxitektura
```
bot.py (handlerlar)  →  db.py (funksiyalar)  →  PostgreSQL
   "nima qilish"           "qanday saqlash"        "qayerda"
```

## 3-slayd — asyncpg asoslari
```python
pool = await asyncpg.create_pool(DATABASE_URL)
rows = await pool.fetch("SELECT * FROM kitoblar")           # ko'p qator
row  = await pool.fetchrow("SELECT ... WHERE id = $1", 5)    # bitta qator
son  = await pool.fetchval("SELECT COUNT(*) FROM kitoblar")  # bitta qiymat
await pool.execute("INSERT INTO ... VALUES ($1, $2)", a, b)  # natijasiz
```
`row["nomi"]` — lug'atdek o'qiladi

## 4-slayd — ☠️ SQL injection
```python
# ❌ HECH QACHON!
await pool.fetch(f"SELECT * FROM kitoblar WHERE nomi = '{message.text}'")
# foydalanuvchi yozadi:  '; DROP TABLE kitoblar; --
```
```python
# ✅ Parametrli so'rov — baza matnni hech qachon buyruq deb tushunmaydi
await pool.fetch("SELECT * FROM kitoblar WHERE nomi = $1", message.text)
```

## 5-slayd — UPSERT
```sql
INSERT INTO foydalanuvchilar (telegram_id, ism) VALUES ($1, $2)
ON CONFLICT (telegram_id) DO UPDATE SET ism = EXCLUDED.ism;
```
`/start` ni 100 marta bossa ham — 1 ta yozuv

## 6-slayd — Tranzaksiya: "hammasi yoki hech narsa"
```python
async with conn.transaction():
    await conn.execute("UPDATE kitoblar SET soni = soni - 1 WHERE id = $1 AND soni > 0", k)
    await conn.execute("INSERT INTO ijaralar ...")
# o'rtada xato bo'lsa — ikkalasi ham bekor qilinadi (ROLLBACK)
```

## 7-slayd — RETURNING
```sql
UPDATE ijaralar SET qaytarilgan = now() WHERE id = $1 RETURNING kitob_id;
```
O'zgartirish + natijani olish — **bitta** so'rovda
