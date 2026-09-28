# 13-dars. Observer andozasi: EventEmitter, React state

**Guruh:** 11.1 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** I bob, "Loyihalash andozalari: ... Observer"

## Maqsad
- Observer (publish/subscribe) andozasining mohiyatini tushunadi: "subject" o'zgarganda barcha "observer"larga xabar beriladi.
- O'z `EventEmitter` klassini yozadi: `on`, `off`, `emit`, `once`.
- Node.js'ning tayyor `EventEmitter` idan va brauzerdagi `addEventListener` dan foydalanadi. Ular aynan Observer ekanini ko'radi.
- React'dagi state va re-render mexanizmini Observer nuqtai nazaridan tushunadi.
- Xotira oqishini (memory leak) oldini olish uchun obunani bekor qilish (unsubscribe) muhimligini biladi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | *"YouTube kanalga obuna bo'ldingiz. Yangi video chiqqanda sizga bildirishnoma keladi. Siz har 5 daqiqada kanalni tekshirmaysiz, kanalning o'zi xabar beradi."* Bu — Observer |
| 5–10 | **Takrorlash** | 12-dars testi |
| 10–25 | **Yangi mavzu** | Subject + Observer. Pub/sub. Real misollar: DOM eventlar, Node EventEmitter, React state, WebSocket, Redux |
| 25–35 | **Jonli** | Noldan `EventEmitter` (`kod/emitter.js`) |
| 35–60 | **Amaliyot** | `amaliy-topshiriq.md` |
| 60–74 | **Challenge** | `challenge.md`: "Jonli chat simulyatsiyasi" |
| 74–80 | **Yakun** | 3 ta andozani taqqoslash (Factory/Singleton/Observer), XP, uyga vazifa |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +20/+10/+5
