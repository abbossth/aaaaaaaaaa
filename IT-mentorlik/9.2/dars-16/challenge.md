# 16-dars challenge: "Xaker vs Himoyachi" 🛡⚔️

**Vaqt:** 17 daqiqa | **Format:** juftliklar almashadi

## 1-bosqich: Himoya (8 daqiqa)
Har bir juftlik `Oyinchi` klassini yozadi (RPG o'yin qahramoni):
- `hp` (0..100), `oltin` (manfiy bo'lmaydi), `daraja` (faqat o'qish, XP'dan hisoblanadi: har 100 XP = 1 daraja)
- Metodlar: `zarba_ol(n)`, `davolan(n)`, `oltin_top(n)`, `sotib_ol(narx)`, `xp_ol(n)`

## 2-bosqich: Hujum (9 daqiqa)
Kodlar almashtiriladi. "Xakerlar" **faqat public metodlar va property'lar orqali** (name mangling taqiqlanadi!) qahramonni "buzilgan" holatga keltirishga harakat qiladi:
- `hp` > 100 yoki < 0
- `oltin` manfiy
- `daraja` ni to'g'ridan-to'g'ri o'zgartirish
- manfiy zarba bilan davolanish 😏 (`zarba_ol(-50)`)

**Ball:** har bir muvaffaqiyatli hujum — xakerga +5 XP. Birorta ham hujum o'tmagan himoyachiga +20 XP va 🛡 "Bulletproof" badge.
