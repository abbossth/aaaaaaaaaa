// 🟡 O'rta: takrorlanishni olib tashlang (DRY) va guard clause qo'llang
function sendWelcomeEmail(user) {
  if (user) {
    if (user.email) {
      if (user.email.includes("@")) {
        console.log("To: " + user.email);
        console.log("Subject: Xush kelibsiz!");
        console.log("Salom, " + user.name + "! Ro'yxatdan o'tganingiz uchun rahmat.");
      }
    }
  }
}

function sendResetEmail(user) {
  if (user) {
    if (user.email) {
      if (user.email.includes("@")) {
        console.log("To: " + user.email);
        console.log("Subject: Parolni tiklash");
        console.log("Salom, " + user.name + "! Parolni tiklash havolasi: ...");
      }
    }
  }
}
