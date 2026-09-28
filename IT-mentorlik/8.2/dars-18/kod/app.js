// 1. Dark mode
document.querySelector("#rejim").addEventListener("click", (e) => {
  const qorongi = document.body.classList.toggle("qorongi");
  e.target.textContent = qorongi ? "☀️ Light mode" : "🌙 Dark mode";
});

// 2. Hisoblagich
let hisob = 0;
const hisobEl = document.querySelector("#hisob");
const yangila = () => (hisobEl.textContent = hisob);
document.querySelector("#plus").addEventListener("click", () => { hisob++; yangila(); });
document.querySelector("#minus").addEventListener("click", () => { if (hisob > 0) hisob--; yangila(); });
document.querySelector("#nol").addEventListener("click", () => { hisob = 0; yangila(); });

// 3. Filtr + qidiruv
const mahsulotlar = [
  { nom: "iPhone 15", kategoriya: "telefon" },
  { nom: "Redmi Note 13", kategoriya: "telefon" },
  { nom: "AirPods", kategoriya: "aksessuar" },
  { nom: "Chexol", kategoriya: "aksessuar" },
  { nom: "Samsung A15", kategoriya: "telefon" },
];
let tanlanganKategoriya = "hammasi";
let qidiruvMatni = "";

function render() {
  const natija = mahsulotlar
    .filter((m) => tanlanganKategoriya === "hammasi" || m.kategoriya === tanlanganKategoriya)
    .filter((m) => m.nom.toLowerCase().includes(qidiruvMatni));
  document.querySelector("#galereya").innerHTML =
    natija.map((m) => `<div class="karta">${m.nom}</div>`).join("") || "<p>Hech narsa topilmadi 🤷</p>";
}

document.querySelector("#qidiruv").addEventListener("input", (e) => {
  qidiruvMatni = e.target.value.trim().toLowerCase();
  render();
});

document.querySelectorAll(".filtr").forEach((tugma) => {
  tugma.addEventListener("click", () => {
    document.querySelector(".filtr.faol").classList.remove("faol");
    tugma.classList.add("faol");
    tanlanganKategoriya = tugma.dataset.kategoriya;
    render();
  });
});

// 4. Klaviatura: "+" va "-" tugmalari hisoblagichni boshqaradi
document.addEventListener("keydown", (e) => {
  if (e.target.tagName === "INPUT") return;
  if (e.key === "+") { hisob++; yangila(); }
  if (e.key === "-" && hisob > 0) { hisob--; yangila(); }
});

render();
