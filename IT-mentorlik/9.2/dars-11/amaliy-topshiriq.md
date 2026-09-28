# 11-dars amaliy topshiriq: "Kontaktlar kitobi" v3 💾

## 🟢 Oson (+5 XP)
1. `son_sora(xabar)` funksiyasi: son kiritilmaguncha qayta so'rasin (`try/except ValueError`).
2. **Xavfsiz kalkulyator:** ikki son va amal. `ValueError` va `ZeroDivisionError` alohida ushlansin.
3. **Kundalik:** foydalanuvchi yozgan har bir gap `kundalik.txt` fayliga **qo'shilsin** (`a` rejimi), oldida sana-vaqt bilan (`datetime.now()`).

## 🟡 O'rta (+10 XP)
v2'ni v3'ga aylantiring:
- Dastur ishga tushganda `kontaktlar.json` dan yuklansin (fayl yo'q yoki buzilgan bo'lsa ham qulamasin).
- Har bir o'zgarishdan keyin (qo'shish, o'chirish, tahrirlash) avtomatik saqlansin.
- JSON fayl o'zbekcha harflarni to'g'ri saqlasin va chiroyli formatlansin.

## 🔴 Qiyin (+20 XP)
- **Eksport/import:** kontaktlarni CSV fayliga eksport qilish (`csv` moduli) va CSV'dan import qilish.
- **Custom exception:** `NotogriTelefon(Exception)`. `tel_tozalash` noto'g'ri raqamda `None` qaytarmasin, `raise` qilsin, chaqiruvchi esa uni ushlasin.
- **Backup:** har safar saqlashdan oldin eski faylni `kontaktlar.backup.json` ga nusxalang.

Namuna: `kod/kontaktlar_v3.py`
