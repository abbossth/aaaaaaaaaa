# 13-dars amaliy topshiriq

## 🟢 Oson (+5 XP)
`kod/emitter.js` ni ishga tushiring. Yangi obunachi qo'shing: `logToFile` (buyurtmani `orders.log` ga yozadi, `fs.appendFileSync`). Buning uchun `EventEmitter` kodini o'zgartirish kerak bo'ldimi? (Yo'q — OCP!)

## 🟡 O'rta (+10 XP): Vitest bilan testlar
`EventEmitter` uchun testlar yozing:
- `emit` barcha obunachilarni chaqiradi
- `off` dan keyin handler chaqirilmaydi
- `once` faqat bir marta ishlaydi
- `on` qaytargan funksiya obunani bekor qiladi
Maslahat: `vi.fn()` bilan "josus" funksiya yarating va `toHaveBeenCalledTimes(1)` bilan tekshiring.

## 🔴 Qiyin (+20 XP): Reaktiv Store (mini-Redux)
`createStore(initialState)`: `getState()`, `setState(partial)`, `subscribe(listener)` (unsubscribe qaytarsin). `setState` chaqirilganda barcha obunachilarga yangi holat uzatiladi. Uni brauzerda hisoblagich va savat bilan ishlating: ikki xil DOM qismi bir store'ga obuna bo'ladi va avtomatik yangilanadi.
