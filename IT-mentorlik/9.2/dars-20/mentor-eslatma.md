# 20-dars mentor eslatmasi

## Ko'p uchraydigan muammolar
| Muammo | Yechim |
|---|---|
| `TokenValidationError` | Token noto'g'ri yoki `.env` o'qilmagan (fayl nomi `.env.txt` bo'lib qolgan!) |
| Bot javob bermaydi | Bir xil token bilan 2 ta nusxa ishlayapti (`Conflict: terminated by other getUpdates`) |
| Maktab tarmog'ida `api.telegram.org` bloklangan | Mobil internet (hotspot) orqali ulash |
| `ModuleNotFoundError: aiogram` | venv faollashtirilmagan |
| aiogram 2 misollari internetdan olingan (`executor.start_polling`) | Bu eski versiya! Faqat aiogram 3 hujjatlaridan foydalaning |

## Maslahat
- Har bir o'quvchi **o'z** botini yaratsin (bitta token — bitta ishlaydigan nusxa).
- Botlar faqat kompyuter yoqiq va `python bot.py` ishlayotgan paytda javob beradi. Buni tushuntiring. 24/7 ishlash — deploy mavzusi (62-dars).
