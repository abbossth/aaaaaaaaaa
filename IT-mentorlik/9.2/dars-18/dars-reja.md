# 18-dars. Abstraksiya: abc moduli, abstrakt klasslar — "To'lov tizimi" modeli

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 2-bob, "Abstraksiya"

## Maqsad
- Abstraksiya mohiyatini tushunadi: murakkab tafsilotlarni yashirib, faqat muhim interfeysni ko'rsatish.
- `abc.ABC` va `@abstractmethod` bilan abstrakt klass yaratadi. Undan obyekt yaratib bo'lmasligini biladi.
- Abstrakt klass — "shartnoma" ekanini tushunadi: har bir bola barcha abstrakt metodlarni yozishi shart.
- Real back-end misolida qo'llaydi: to'lov provayderlari (Click, Payme, Uzum), bildirishnoma kanallari.
- OOP'ning 4 ustunini bitta loyihada birlashtiradi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | *"Mashinani haydash uchun dvigatel qanday ishlashini bilishingiz shartmi? Yo'q — rul, gaz, tormoz yetarli. Bu abstraksiya."* Keyin: *"Do'kon Click, Payme, Uzum orqali to'lov qabul qiladi. Har biri butunlay boshqa API. Lekin do'kon kodi `provayder.tolov(summa)` deb yozadi, xolos."* |
| 5–10 | **Takrorlash** | 17-dars testi + Arena natijalari |
| 10–28 | **Yangi mavzu** | Abstraksiya. `ABC`, `@abstractmethod`. `TypeError: Can't instantiate abstract class`. Shartnoma g'oyasi. Duck typing (Python uslubi) |
| 28–58 | **Amaliyot** | `amaliy-topshiriq.md`: to'lov tizimi |
| 58–72 | **Challenge** | `challenge.md`: "Shartnomani buz" |
| 72–80 | **Yakun** | OOP 4 ustuni xulosasi, XP, uyga vazifa |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +20/+10/+5
