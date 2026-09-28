# 20-dars slaydlari: fetch va API

## 1-slayd
🌐 **Boshqa serverlardan ma'lumot olamiz**

## 2-slayd — API nima?
Dasturlar o'rtasidagi "menyu": nima so'rash mumkin va javob qanday keladi.
Ob-havo, valyuta kursi, xarita, film ma'lumotlari, AI...

## 3-slayd — Asinxronlik 🍽
Sinxron: ofitsiant buyurtmangizni olib, **ovqat pishguncha oshxona oldida kutib turadi** (boshqalarga xizmat qilmaydi) 😩
Asinxron: buyurtmani oshxonaga beradi, **boshqalarga xizmat qiladi**, ovqat tayyor bo'lganda olib keladi ✅
`fetch` = oshxonaga buyurtma

## 4-slayd — async/await
```js
async function obHavo() {
  const res = await fetch("https://api.open-meteo.com/v1/forecast?latitude=41.3&longitude=69.28&current=temperature_2m");
  const data = await res.json();
  console.log(data.current.temperature_2m);
}
```

## 5-slayd — Xatolarni ushlash
```js
try {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`Server xatosi: ${res.status}`);
  const data = await res.json();
} catch (err) {
  xatoEl.textContent = "Ma'lumot olinmadi 😢";
}
```

## 6-slayd — 3 holat
⏳ Yuklanmoqda... → ✅ Ma'lumot → ❌ Xato
Yaxshi ilova uchalasini ham ko'rsatadi!
