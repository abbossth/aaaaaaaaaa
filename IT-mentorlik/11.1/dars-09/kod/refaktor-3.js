// 🔴 Qiyin: bu funksiyani 4–5 ta kichik, aniq nomli funksiyaga ajrating
function processOrder(o) {
  // tekshirish
  if (!o.items || o.items.length == 0) { console.log("Bo'sh buyurtma"); return; }
  if (!o.user || !o.user.phone) { console.log("Telefon yo'q"); return; }
  // summa
  let s = 0;
  for (const it of o.items) { s += it.price * it.qty; }
  // yetkazib berish
  let d = 0;
  if (s < 100000) d = 15000;
  else if (s < 300000) d = 10000;
  // promo
  if (o.promo == "MAKTAB10") s = s * 0.9;
  if (o.promo == "YANGI20") s = s * 0.8;
  const total = s + d;
  // SMS
  console.log("SMS -> " + o.user.phone + ": Buyurtmangiz qabul qilindi. Jami: " + total + " so'm");
  return total;
}
