# 2-dars. SDLC: talab → dizayn → kod → test → deploy → monitoring

**Guruh:** 11.1 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** I bob, "Dasturiy ta'minot hayotiy sikli (SDLC)"

## Maqsad
- SDLC bosqichlarini va har bir bosqich natijasini (artefaktini) biladi: talablar hujjati, maket, kod, testlar, release, loglar.
- Waterfall va Agile (iterativ) modellarini farqlaydi.
- SDLC'ni o'z jamoasi startapiga qo'llab reja tuza oladi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Rasm: "Mijoz nima so'radi → PM nima tushundi → dasturchi nima yozdi → mijozga nima kerak edi" (mashhur "daraxtga osilgan arg'imchoq" memi). *"Bu muammo 50 yildan beri bor. SDLC aynan uni hal qilish uchun o'ylab topilgan."* |
| 5–10 | **Takrorlash** | 1-dars testi + jamoalardan 1 jumlalik "muammolar" (uyga vazifa) |
| 10–25 | **Yangi mavzu** | 6 bosqich va ularning artefaktlari. Waterfall va Agile. Real misol: "Maktab oshxonasi uchun buyurtma ilovasi" SDLC bo'ylab |
| 25–55 | **Challenge** | `challenge.md`: "Qog'oz samolyot fabrikasi" — Waterfall va Agile'ni jismonan his qilish |
| 55–72 | **Amaliyot** | `amaliy-topshiriq.md`: jamoa startapi uchun SDLC xaritasi |
| 72–80 | **Yakun** | Retro: "O'yinda Waterfall yoki Agile yaxshiroq ishladimi? Nega?" Uyga vazifa |

## SDLC bosqichlari va artefaktlar
| Bosqich | Savol | Artefakt |
|---|---|---|
| 1. Talab (Requirements) | Nima qurilyapti va kim uchun? | User story'lar, talablar hujjati |
| 2. Dizayn (Design) | Qanday ko'rinadi va qanday tuzilgan? | Figma maket, arxitektura sxemasi, DB sxemasi |
| 3. Kod (Implementation) | Qurish | Git repo, PR'lar |
| 4. Test | Ishlayaptimi? | Unit/integratsion testlar, bug report'lar |
| 5. Deploy | Foydalanuvchiga yetkazish | Release, CI/CD pipeline |
| 6. Monitoring / Maintenance | Ishlashda davom etyaptimi? | Loglar, metrikalar, alertlar |

## Baholash (XP)
- O'yinda ishtirok +10 · Eng ko'p sifatli samolyot yasagan jamoa +20 · SDLC xaritasi +10/+20
