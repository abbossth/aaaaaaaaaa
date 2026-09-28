# 10-dars challenge: "SOLID sud" ⚖️

**Vaqt:** 14 daqiqa | **Format:** jamoalar

Mentor 6 ta "ish" (kod parchasi yoki holat) ko'rsatadi. Jamoalar "sudya" sifatida qaror chiqaradi: **qaysi tamoyil buzilgan** va **qanday tuzatish kerak**?

| № | Ish | Hukm |
|---|---|---|
| 1 | `class User { save() {} sendEmail() {} generatePDF() {} }` | S |
| 2 | Yangi mamlakat qo'shish uchun `calculateTax()` ichiga yana `if` qo'shiladi | O |
| 3 | `class ReadOnlyFile extends File { write() { throw Error() } }` | L |
| 4 | `interface Worker { work(); eat(); sleep(); }` → `Robot` ham `eat()` ni implement qilishga majbur | I |
| 5 | `class Weather { api = new OpenWeatherAPI("KEY") }`: test qilishda real API'ga so'rov ketadi | D |
| 6 | `function processAll() { /* 300 qator: validatsiya, hisoblash, saqlash, log */ }` | S |

**Ball:** to'g'ri tamoyil +2, to'g'ri yechim taklifi +3.
**XP:** 🥇 +20 · 🥈 +10 · 🥉 +5
