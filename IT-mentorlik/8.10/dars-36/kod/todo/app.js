// 36-dars, 2-qism: localStorage bilan saqlanadigan To-Do

const forma = document.getElementById("forma");
const input = document.getElementById("matn");
const royxat = document.getElementById("royxat");

// 1) Sahifa ochilganda — saqlangan vazifalarni o'qiymiz (bo'lmasa bo'sh massiv)
let vazifalar = JSON.parse(localStorage.getItem("vazifalar")) || [];

// 2) Saqlash: massiv → matn (JSON) → localStorage
function saqla() {
  localStorage.setItem("vazifalar", JSON.stringify(vazifalar));
}

// 3) Chizish: massiv → sahifa
function chiz() {
  royxat.innerHTML = "";
  vazifalar.forEach((v, index) => {
    const li = document.createElement("li");
    if (v.bajarildi) li.classList.add("bajarildi");

    const span = document.createElement("span");
    span.textContent = v.matn;
    span.addEventListener("click", () => {       // bosilsa — bajarildi/bajarilmadi
      v.bajarildi = !v.bajarildi;
      saqla();
      chiz();
    });

    const ochir = document.createElement("button");
    ochir.textContent = "🗑";
    ochir.addEventListener("click", () => {
      vazifalar.splice(index, 1);                // massivdan o'chirish
      saqla();
      chiz();
    });

    li.append(span, ochir);
    royxat.append(li);
  });

  const qolgan = vazifalar.filter((v) => !v.bajarildi).length;
  document.getElementById("hisob").textContent = `${qolgan} ta vazifa qoldi`;
}

// 4) Qo'shish (validatsiya bilan)
forma.addEventListener("submit", (event) => {
  event.preventDefault();
  const matn = input.value.trim();
  const xato = document.getElementById("xato");

  if (matn.length < 2) {
    xato.textContent = "Kamida 2 ta belgi yozing ✋";
    return;
  }
  xato.textContent = "";
  vazifalar.push({ matn: matn, bajarildi: false });
  saqla();
  chiz();
  input.value = "";
});

chiz();
