# 13-dars slaydlari: Observer

## 1-slayd
🔔 **"Obuna bo'ling va qo'ng'iroqchani bosing!"**

## 2-slayd — Observer
```
     Subject (kanal)
    /      |       \
 👀 Obs1  👀 Obs2  👀 Obs3   ← obunachilar
```
Subject o'zgarsa → hammasiga `notify()`

## 3-slayd — Pub/Sub API
```js
emitter.on("order:created", handler);   // obuna
emitter.emit("order:created", order);   // e'lon
emitter.off("order:created", handler);  // obunani bekor qilish
```

## 4-slayd — Siz allaqachon ishlatgansiz!
```js
button.addEventListener("click", onClick);   // DOM
process.on("exit", cleanup);                 // Node
socket.on("message", show);                  // WebSocket
```

## 5-slayd — React = Observer
```jsx
const [count, setCount] = useState(0);
// setCount → React "obunachi" komponentlarni qayta chizadi
```

## 6-slayd — Afzalliklari
✅ Kuchsiz bog'lanish: subject obunachilarni bilmaydi
✅ Yangi obunachi qo'shish oson (OCP!)
⚠️ Obunani bekor qilmasangiz → memory leak
⚠️ Juda ko'p event → "qaysi event nimani chaqiryapti?" chalkashligi

## 7-slayd — 3 andoza
| Andoza | Guruh | Savol |
|---|---|---|
| Factory | Yaratuvchi | Obyektni **qanday yaratamiz**? |
| Singleton | Yaratuvchi | Nechta nusxa? **Bitta** |
| Observer | Xulq-atvor | O'zgarish haqida **qanday xabar beramiz**? |
