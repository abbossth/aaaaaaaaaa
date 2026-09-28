# Oraliq nazorat #1 — amaliy qism

Barcha vazifalar bitta `nazorat1_familiya.py` faylida. Kod ishga tushishi va qulamasligi kerak.

## 🟢 1-vazifa (15 ball): Funksiyalar
`matn_tahlili(matn: str) -> dict` funksiyasini yozing. U quyidagilarni qaytarsin:
```python
{"sozlar": 5, "harflar": 23, "eng_uzun": "dasturlash", "unlilar": 8}
```
- Harflar — faqat harflar soni (`isalpha`)
- Unlilar — a, e, i, o, u (katta-kichik farqsiz)
- Bo'sh matn uchun: `{"sozlar": 0, "harflar": 0, "eng_uzun": "", "unlilar": 0}`

## 🟡 2-vazifa (20 ball): Fayl + xatolar
`baholar.txt` faylida har bir qatorda `ism,baho1,baho2,baho3` bor (fayl namunasi: `kod/baholar.txt`). Ba'zi qatorlar buzilgan.
`hisobot(fayl_nomi)` funksiyasi:
- har bir o'quvchining o'rtacha bahosini hisoblasin
- buzilgan qatorlarni (son emas, bo'sh, baho 2..5 dan tashqarida) o'tkazib yuborsin va nechtasi o'tkazilganini sanasin
- natijani `hisobot.json` ga yozsin: `{"oquvchilar": {"Aziz": 4.67, ...}, "otkazilgan": 2}`
- fayl topilmasa — tushunarli xabar chiqarsin, qulamasin

## 🔴 3-vazifa (25 ball): OOP
Kutubxona tizimi:
- `Kitob`: `nom`, `muallif`, `mavjud` (read-only property, bool). `__str__`.
- `Azo` (a'zo): `ism`, olgan kitoblari ro'yxati; bir vaqtda ko'pi bilan 3 ta kitob.
- `Kutubxona`: `kitob_qosh(kitob)`, `ber(kitob_nomi, azo)`, `qaytar(kitob_nomi, azo)`, `mavjud_kitoblar()`.
- Qoidalar buzilsa (kitob yo'q, band, limit oshgan, a'zoda bu kitob yo'q), o'z xato klassingizni `raise` qiling: `KutubxonaXatosi(Exception)`.
- Faylning oxirida 5–6 qatorlik namoyish (`if __name__ == "__main__":`), jumladan kamida bitta ushlangan xato.

### Baholash mezonlari (3-vazifa)
| Mezon | Ball |
|---|---|
| Klasslar to'g'ri tuzilgan | 8 |
| Inkapsulyatsiya (property) | 5 |
| O'z xato klassi va `raise`/`try` | 6 |
| Namoyish ishlaydi | 6 |
