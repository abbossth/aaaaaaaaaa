// 36-dars, 1-qism: forma validatsiyasi

const forma = document.getElementById("forma");

// Bitta maydonni tekshiruvchi yordamchi funksiya
function tekshir(id, shart, xatoMatni) {
  const input = document.getElementById(id);
  const xabar = document.getElementById(id + "-xabar");
  if (shart(input.value.trim())) {
    input.classList.remove("xato");
    input.classList.add("togri");
    xabar.textContent = "";
    return true;
  }
  input.classList.remove("togri");
  input.classList.add("xato");
  xabar.textContent = xatoMatni;
  return false;
}

forma.addEventListener("submit", (event) => {
  event.preventDefault();          // sahifa yangilanmasin!

  const ok1 = tekshir("ism", (v) => v.length >= 2, "Ism kamida 2 harf bo'lsin");
  const ok2 = tekshir("yosh", (v) => v >= 10 && v <= 18, "Yosh 10 dan 18 gacha bo'lsin");
  const ok3 = tekshir("telefon", (v) => v.startsWith("+998") && v.length === 13, "Format: +998901234567");
  const ok4 = tekshir("parol", (v) => v.length >= 6, "Parol kamida 6 belgi");

  if (ok1 && ok2 && ok3 && ok4) {
    const ism = document.getElementById("ism").value.trim();
    document.getElementById("natija").textContent = `✅ Tabriklaymiz, ${ism}! Siz ro'yxatdan o'tdingiz.`;
    forma.reset();
  }
});
