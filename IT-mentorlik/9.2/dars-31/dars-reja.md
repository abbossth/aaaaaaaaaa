# 31-dars. Constraints (PK, FK, UNIQUE, CHECK, NOT NULL) va ALTER TABLE

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 3-bob, "Jadvallar orasidagi bog'lanishlar va cheklovlar"

## Maqsad
- Constraint = bazaning "qo'riqchisi" ekanini tushunadi: noto'g'ri ma'lumot bazaga umuman kirmasin.
- PRIMARY KEY, FOREIGN KEY (`ON DELETE CASCADE / RESTRICT / SET NULL`), UNIQUE (bitta va bir nechta ustunli), CHECK, NOT NULL, DEFAULT bilan ishlaydi.
- `ALTER TABLE`: ustun qo'shish/o'chirish/nomini o'zgartirish, tur o'zgartirish, constraint qo'shish/olib tashlash.
- Xato xabarlarini o'qiydi (`violates check constraint ...`).

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | *"Bazada baho = 7, yoshi = −3, telefon = 'salom'. Kim aybdor? Dasturchi emas — BAZA ruxsat bergan!"* |
| 5–12 | **Takrorlash** | 30-dars: CRUD, `UPDATE`siz `WHERE` xavfi |
| 12–30 | **Yangi mavzu** | `taqdimot.md`: constraint turlari, FK harakatlari, ALTER TABLE |
| 30–55 | **Jonli + amaliyot** | `kod/constraints.sql` qatorma-qator, keyin `amaliy-topshiriq.md` |
| 55–72 | **Challenge** | `challenge.md`: "Bazani buzib ko'r" 🔨 |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge: har bir to'g'ri tushuntirilgan xato +3
