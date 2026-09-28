# 23-dars. Bot + tashqi API, fayl/JSON saqlash — ob-havo va valyuta boti

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 2-bob, "Aiogram... API lar bilan ishlash va ma'lumotlar olish"

## Maqsad
- Botdan tashqi REST API'larga asinxron so'rov yuboradi (`aiohttp`, aiogram bilan birga o'rnatiladi).
- JSON javobni tahlil qilib, foydalanuvchiga chiroyli formatda chiqaradi.
- Tarmoq xatolarini (timeout, 4xx/5xx) ushlaydi. Bot hech qachon qulamaydi.
- Foydalanuvchi sozlamalarini (sevimli shahar) JSON faylda saqlaydi.
- Oddiy keshlash: kurslarni har so'rovda emas, har 30 daqiqada yangilaydi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Botga `/kurs` → darhol Markaziy bankning bugungi dollar kursi. *"Bot internetning istalgan ma'lumotini olib kela oladi."* |
| 5–10 | **Takrorlash** | 22-dars testi |
| 10–25 | **Yangi mavzu** | Nega `requests` emas, `aiohttp` (asinxron!). `async with session.get()`. Timeout. Xatolarni ushlash. Keshlash g'oyasi |
| 25–55 | **Amaliyot** | `amaliy-topshiriq.md` |
| 55–72 | **Challenge** | `challenge.md`: "API ovchisi" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +20/+10/+5
