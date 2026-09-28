const emoji = { tosh: "✊", qaychi: "✌️", "qog'oz": "✋" };
const yutadi = { tosh: "qaychi", qaychi: "qog'oz", "qog'oz": "tosh" };
const variantlar = Object.keys(emoji);

const oyinchi = (prompt("tosh, qaychi yoki qog'oz?") || "").trim().toLowerCase();

if (!variantlar.includes(oyinchi)) {
  alert("Noto'g'ri tanlov!");
} else {
  const komp = variantlar[Math.floor(Math.random() * variantlar.length)];
  let natija;
  if (oyinchi === komp) {
    natija = "Durang 🤝";
  } else if (yutadi[oyinchi] === komp) {
    natija = "Siz yutdingiz! 🎉";
  } else {
    natija = "Kompyuter yutdi 🤖";
  }
  alert(`Siz: ${oyinchi} ${emoji[oyinchi]} | Kompyuter: ${komp} ${emoji[komp]} → ${natija}`);
}
