// 34-dars: DOM — elementlarni topish va o'zgartirish

// 1) Elementni topish
const sarlavha = document.getElementById("sarlavha");
const matn = document.querySelector(".matn");       // CSS selektor bilan
console.log(sarlavha, matn);

// 2) Matnni o'zgartirish
sarlavha.textContent = "Salom, 8.10! 👋";
matn.innerHTML = "Bu matnni <b>JavaScript</b> o'zgartirdi ✨";

// 3) Stil o'zgartirish
sarlavha.style.color = "#4f46e5";
sarlavha.style.fontSize = "40px";

// 4) Profil kartochkasi — obyektdan (33-dars!)
const men = { ism: "Aziz Karimov", kasb: "Kelajakdagi Full-stack dasturchi 💻", reyting: 4 };
document.getElementById("ism").textContent = men.ism;
document.getElementById("kasb").textContent = men.kasb;
document.getElementById("yulduzlar").textContent = "⭐".repeat(men.reyting);

// 5) Atributni o'zgartirish
document.getElementById("rasm").src = "https://cataas.com/cat?width=240";

// 6) Massivdan ro'yxat yaratish (createElement + append)
const oyinlar = ["Minecraft", "Roblox", "FIFA", "Brawl Stars"];
const royxat = document.getElementById("royxat");
for (const oyin of oyinlar) {
  const li = document.createElement("li");
  li.textContent = "🎮 " + oyin;
  royxat.append(li);
}

// 7) Klass qo'shish/olib tashlash
royxat.firstElementChild.classList.add("yangi");

// 8) Tugma bosilganda (eventlar — keyingi darsda batafsil!)
function sehr() {
  const ranglar = ["#fde68a", "#bfdbfe", "#fecaca", "#bbf7d0", "#e9d5ff"];
  const tasodifiy = ranglar[Math.floor(Math.random() * ranglar.length)];
  document.body.style.background = tasodifiy;
  sarlavha.textContent = "Rang: " + tasodifiy;
}
