# 8-dars. Node.js va npm'ga kirish: modullar, package.json, skriptlar

**Guruh:** 11.1 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa

> Bu dars rasmiy dasturda yo'q, lekin kerak: guruh Python'ni bilmaydi. Keyingi mavzular (Clean Code, andozalar, REST API, Docker, CI) JS/Node misollarida o'tiladi.

## Maqsad
- Node.js nima ekanini tushunadi: JavaScript brauzerdan tashqarida, serverda ishlaydi.
- `node fayl.js`, REPL, `process.argv`, `fs` va `path` modullari bilan ishlaydi.
- ES modullar (`import/export`) va CommonJS (`require`) farqini biladi.
- `npm init`, `package.json`, `dependencies/devDependencies`, `npm scripts`, `node_modules` va `.gitignore` tushunchalarini qo'llaydi.
- Oddiy CLI dastur yozadi: **To-Do CLI** (JSON faylga saqlaydi).

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | *"Netflix, PayPal, LinkedIn, Uber back-endlarining bir qismi Node.js'da. Siz bilgan JavaScript bilan server yozish mumkin."* Jonli: 5 qatorlik HTTP server, brauzerda `localhost:3000` ochiladi |
| 5–10 | **Takrorlash** | 7-dars testi |
| 10–25 | **Yangi mavzu** | Node = V8 + tizim API'lari. Brauzer vs Node (`window` yo'q, `fs` bor). Modullar. npm ekotizimi. package.json tahlili. Semver (`^1.2.3`) |
| 25–55 | **Amaliyot** | `amaliy-topshiriq.md`: To-Do CLI |
| 55–72 | **Challenge** | `challenge.md`: "npm paket ovchisi" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Jonli kod: 5 qatorlik server
```js
// server.js
import http from "node:http";
http.createServer((req, res) => {
  res.end(`Salom! Siz ${req.url} sahifasini so'radingiz`);
}).listen(3000, () => console.log("http://localhost:3000"));
```
`package.json` da `"type": "module"` bo'lishi kerak (yoki fayl `.mjs`).

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +20/+10/+5
