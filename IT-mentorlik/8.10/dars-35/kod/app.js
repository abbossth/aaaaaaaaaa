// 35-dars: eventlar — click, input, keydown

// ===== 1. Hisoblagich =====
let son = 0;
const sonEl = document.getElementById("son");

function yangila() {
  sonEl.textContent = son;
  sonEl.classList.toggle("manfiy", son < 0);    // shart to'g'ri bo'lsa klass qo'shiladi
  sonEl.classList.toggle("katta", son >= 10);
}

document.getElementById("plus").addEventListener("click", () => {
  son++;
  yangila();
});
document.getElementById("minus").addEventListener("click", () => {
  son--;
  yangila();
});
document.getElementById("nol").addEventListener("click", () => {
  son = 0;
  yangila();
});

// ===== 2. Dark mode =====
const rejimBtn = document.getElementById("rejim");
rejimBtn.addEventListener("click", () => {
  document.body.classList.toggle("qorongi");
  rejimBtn.textContent = document.body.classList.contains("qorongi") ? "☀️" : "🌙";
});

// ===== 3. Jonli matn (input eventi) =====
const kirish = document.getElementById("kirish");
kirish.addEventListener("input", () => {
  const ism = kirish.value.trim();
  document.getElementById("salom").textContent = ism || "mehmon";
  document.getElementById("belgi").textContent = `${kirish.value.length}/20`;
});

// ===== 4. Klaviatura (keydown) =====
const kvadrat = document.getElementById("kvadrat");
let x = 0;
let y = 0;

document.addEventListener("keydown", (event) => {
  if (event.target === kirish) return;          // input'da yozayotganda o'yin ishlamasin
  document.getElementById("tugma").textContent = event.key;

  if (event.key === "ArrowRight") x += 20;
  if (event.key === "ArrowLeft") x -= 20;
  if (event.key === "ArrowDown") y += 20;
  if (event.key === "ArrowUp") y -= 20;
  if (event.key === "+") { son++; yangila(); }  // klaviaturadan ham hisoblagich
  if (event.key === "-") { son--; yangila(); }

  kvadrat.style.left = x + "px";
  kvadrat.style.top = y + "px";
});
