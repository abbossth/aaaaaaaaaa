# 11-dars amaliy topshiriq

## 🟢 Oson (+10 XP): Sozlash
1. `kod/sifat-demo` ni nusxalang, `npm install`, keyin `npm test`: hammasi yashil ✅ bo'lishi kerak.
2. `src/cart.js` da `>=` ni `>` ga o'zgartiring va `npm test` qiling. Qaysi test qizardi? Nega? Qaytaring.
3. `npm run lint` va `npm run format` ni ishga tushiring.

## 🟡 O'rta (+10 XP): O'z testlaringiz
To-Do CLI'ingizdagi (8-dars) mantiqni `src/todo.js` ga ajrating (fayl bilan ishlashsiz, "sof" funksiyalar): `addTodo(todos, text)`, `completeTodo(todos, index)`, `removeTodo(todos, index)`. Har biriga kamida 3 ta test yozing (oddiy, chegaraviy, xato holati).

## 🔴 Qiyin (+20 XP)
- `npx vitest run --coverage` bilan test qamrovini (coverage) ko'ring (`@vitest/coverage-v8` kerak). 90%+ ga yeting.
- Jamoa reposiga ESLint + Prettier + Vitest ni qo'shing va `CONTRIBUTING.md` ga "PR ochishdan oldin `npm run lint && npm test`" qoidasini yozing.
