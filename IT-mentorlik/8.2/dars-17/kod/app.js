const mahsulotlar = [
  { nom: "Telefon", narx: 2900000, chegirma: false, emoji: "📱" },
  { nom: "Noutbuk", narx: 6800000, chegirma: true, emoji: "💻" },
  { nom: "Quloqchin", narx: 650000, chegirma: false, emoji: "🎧" },
  { nom: "Soat", narx: 450000, chegirma: true, emoji: "⌚" },
];

const galereya = document.querySelector("#galereya");
const soni = document.querySelector("#soni");

function formatNarx(n) {
  return n.toLocaleString("ru-RU") + " so'm";
}

function render(royxat) {
  galereya.innerHTML = "";
  for (const m of royxat) {
    const karta = document.createElement("div");
    karta.className = "karta";
    if (m.chegirma) karta.classList.add("chegirma");

    const h3 = document.createElement("h3");
    h3.textContent = `${m.emoji} ${m.nom}`;

    const narx = document.createElement("p");
    narx.className = "narx";
    narx.textContent = formatNarx(m.narx);

    karta.append(h3, narx);
    galereya.append(karta);
  }
  soni.textContent = `Jami: ${royxat.length} ta mahsulot`;
}

render(mahsulotlar);
document.querySelector("#sarlavha").textContent += " 🛍";
