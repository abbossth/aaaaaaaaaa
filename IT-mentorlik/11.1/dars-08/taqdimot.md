# 8-dars slaydlari: Node.js

## 1-slayd
🟩 **JavaScript — endi serverda ham!**

## 2-slayd — Node.js nima?
Chrome'ning V8 dvigateli + fayl, tarmoq va jarayonlar bilan ishlash API'lari
2009 · Ryan Dahl · Netflix, PayPal, LinkedIn, Uber

## 3-slayd — Brauzer va Node
| Brauzer | Node.js |
|---|---|
| `window`, `document`, DOM | yo'q |
| `fs` (fayllar) — yo'q | `fs`, `path`, `http`, `process` |
| Foydalanuvchi kompyuterida | Serverda |

## 4-slayd — Modullar
```js
// math.js
export const qosh = (a, b) => a + b;
// app.js
import { qosh } from "./math.js";
```
Eski usul (CommonJS): `module.exports` / `require()`

## 5-slayd — npm = dunyodagi eng katta paketlar ombori
`npm init -y` → package.json
`npm install chalk` → dependencies
`npm install -D vitest` → devDependencies
`npm run dev` → scripts

## 6-slayd — package.json
```json
{
  "name": "todo-cli",
  "type": "module",
  "scripts": { "start": "node index.js", "test": "vitest" },
  "dependencies": { "chalk": "^5.3.0" },
  "devDependencies": { "vitest": "^2.0.0" }
}
```
`^5.3.0` → 5.x.x ichidagi eng yangi (MAJOR o'zgarmaydi)

## 7-slayd — ⚠️ node_modules
Yuzlab MB! → `.gitignore` ga. Boshqa kompyuterda: `npm install` (yoki `npm ci`)
