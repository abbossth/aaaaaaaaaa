# 12-dars challenge: "Andoza detektivi" 🔍

**Vaqt:** 10 daqiqa | **Format:** jamoalar

Real kutubxona va vaziyatlarda qaysi andoza ishlatilgan? (Factory, Singleton yoki "hech biri")

| № | Holat | Javob |
|---|---|---|
| 1 | `document.createElement("div")` | Factory |
| 2 | `React.createElement(type, props)` | Factory |
| 3 | Node.js'da `require("./db")` ikki marta chaqirilsa, bir xil obyekt qaytadi | Singleton (modul keshi) |
| 4 | `express()` — yangi ilova obyektini qaytaradi | Factory |
| 5 | Brauzerdagi `window` obyekti | Singleton |
| 6 | `Array.from("abc")` | Factory (statik fabrika metodi) |
| 7 | `mongoose.connect()` ilova bo'ylab bitta ulanishni qayta ishlatadi | Singleton |
| 8 | `new Date()` | Hech biri (oddiy konstruktor) |

**XP:** 🥇 +20 · 🥈 +10 · 🥉 +5
