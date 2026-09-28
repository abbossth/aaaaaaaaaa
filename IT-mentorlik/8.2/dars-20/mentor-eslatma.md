# 20-dars mentor eslatmasi

## Ko'p uchraydigan xatolar
| Xato | Yechim |
|---|---|
| `await` async bo'lmagan funksiyada → SyntaxError | `async function` |
| `res.json()` oldidan `await` unutilgan → `[object Promise]` | `await res.json()` |
| CORS xatosi | Bu API brauzerdan so'rovga ruxsat bermaydi. Boshqa API tanlash kerak (keyinroq server orqali hal qilinadi) |
| Maktab internetida API bloklangan | Mentor oldindan tekshiradi. Zaxira: API javobini JSON faylga saqlab, lokal `fetch("data.json")` |

## Maslahat
Open-Meteo `weather_code` WMO kodlarida. To'liq ro'yxat: open-meteo.com/en/docs (pastda "WMO Weather interpretation codes"). `kod/app.js` da asosiylari bor.
