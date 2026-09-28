# 36-dars amaliy topshiriq (jamoaviy loyiha)

## 1-qadam: namunani ishga tushirish (10 daqiqa)
```bash
createdb -U postgres kutubxona
cd kod && cp .env.example .env     # token va parolni yozing
pip install -r requirements.txt
python sinov.py                    # bazani botsiz sinash
python bot.py
```

## 2-qadam: jamoaviy bot (40 daqiqa)
Mavzu tanlang (yoki o'zingizniki):

| Bot | Jadvallar |
|---|---|
| 🍽 Oshxona buyurtma boti | foydalanuvchilar, taomlar, buyurtmalar, buyurtma_elementlari |
| 📝 Test/imtihon boti | foydalanuvchilar, savollar, variantlar, natijalar |
| 🏀 To'garakka yozilish boti | foydalanuvchilar, togaraklar, azolik (+ joy cheklovi) |
| 💸 Xarajatlar hisobchisi | foydalanuvchilar, kategoriyalar, xarajatlar (oylik hisobot) |

### 🟢 Minimum (+30 XP)
- `schema.sql` (kamida 3 jadval, PK/FK/CHECK), `db.py`, `bot.py`
- `/start` UPSERT bilan, kamida 2 ta asosiy funksiya
- Faqat parametrli so'rovlar (`$1`)

### 🟡 Yaxshi (+10 XP)
- Tranzaksiya ishlatilgan joy (masalan, joy/soni kamayishi)
- `/stat` — `GROUP BY` bilan statistika

### 🔴 A'lo (+20 XP)
- Admin buyruqlari (`ADMIN_ID` tekshiruvi bilan): yangi kitob/taom qo'shish (FSM)
- `sinov.py` da barcha `db.py` funksiyalari tekshirilgan
