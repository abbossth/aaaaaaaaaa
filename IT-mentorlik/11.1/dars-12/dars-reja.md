# 12-dars. Loyihalash andozalari: Factory, Singleton

**Guruh:** 11.1 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** I bob, "Loyihalash andozalari: Factory, Singleton, Observer"

## Maqsad
- Design pattern (loyihalash andozasi) nima ekanini va "Gang of Four" (GoF) tasnifini (yaratuvchi, tuzilmaviy, xulq-atvor) biladi.
- **Factory** andozasi: obyekt yaratishni markazlashtiradi, mijoz kodini aniq klasslardan ajratadi.
- **Singleton** andozasi: tizimda bitta nusxa (logger, config, DB ulanishi). JS'da ES modul aslida tayyor singleton ekanini tushunadi.
- Singleton'ning kamchiliklarini biladi: global holat, test qilish qiyinligi.
- Andozalarni real vazifalarda qo'llaydi: bildirishnoma fabrikasi, logger.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | *"Yandex Go'da 'Ekonom', 'Komfort', 'Biznes' tugmasini bosasiz. Ilova qaysi mashina obyektini yaratishni qanday biladi? Va nega butun ilovada bitta 'Sozlamalar' bor?"* |
| 5–10 | **Takrorlash** | 11-dars testi |
| 10–20 | **Andozalar haqida** | Andoza — tayyor retsept. GoF (1994), 23 ta andoza, 3 guruh |
| 20–35 | **Factory** | ❌ `new` lar va `if`lar hamma joyda → ✅ fabrika. `kod/factory.js` |
| 35–45 | **Singleton** | Logger misoli. JS modul singleton. Kamchiliklari. `kod/singleton.js` |
| 45–68 | **Amaliyot** | `amaliy-topshiriq.md` |
| 68–78 | **Challenge** | `challenge.md`: "Andoza detektivi" |
| 78–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +20/+10/+5
