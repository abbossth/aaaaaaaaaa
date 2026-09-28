const boshlangich = [
  { ism: "Aziz", ball: 87 }, { ism: "Malika", ball: 95 }, { ism: "Bobur", ball: 72 },
  { ism: "Dilnoza", ball: 91 }, { ism: "Sardor", ball: 64 }, { ism: "Nigora", ball: 78 },
];
const qoshilganlar = JSON.parse(localStorage.getItem("qoshilganlar")) || [];
let qidiruv = "";

const baho = (b) => (b >= 86 ? 5 : b >= 71 ? 4 : b >= 56 ? 3 : 2);
const MEDAL = ["🥇", "🥈", "🥉"];

function render() {
  const hammasi = [...boshlangich, ...qoshilganlar].sort((a, b) => b.ball - a.ball);
  const ortacha = hammasi.reduce((s, o) => s + o.ball, 0) / hammasi.length;
  document.querySelector("#ortacha").textContent = `O'rtacha ball: ${ortacha.toFixed(1)}`;

  const royxat = document.querySelector("#royxat");
  royxat.innerHTML = "";
  hammasi.forEach((o, i) => {
    if (!o.ism.toLowerCase().includes(qidiruv)) return;
    const karta = document.createElement("div");
    karta.className = "karta";
    const h3 = document.createElement("h3");
    h3.textContent = `${MEDAL[i] ?? ""} ${o.ism}`;
    const p = document.createElement("p");
    p.textContent = `Ball: ${o.ball} · Baho: ${baho(o.ball)}`;
    karta.append(h3, p);
    royxat.append(karta);
  });
}

document.querySelector("#qidiruv").addEventListener("input", (e) => {
  qidiruv = e.target.value.trim().toLowerCase();
  render();
});

document.querySelector("#forma").addEventListener("submit", (e) => {
  e.preventDefault();
  const ism = document.querySelector("#ism").value.trim();
  const ball = Number(document.querySelector("#ball").value);
  const xato = document.querySelector("#xato");
  if (!ism) return (xato.textContent = "Ism kiriting");
  if (!Number.isFinite(ball) || ball < 0 || ball > 100) return (xato.textContent = "Ball 0..100 oralig'ida bo'lsin");
  xato.textContent = "";
  qoshilganlar.push({ ism, ball });
  localStorage.setItem("qoshilganlar", JSON.stringify(qoshilganlar));
  e.target.reset();
  render();
});

render();
