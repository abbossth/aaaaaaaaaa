// ================= S — Single Responsibility =================
// ❌ Yomon: bitta klass 3 xil ish qiladi
class UserServiceBad {
  register(user) {
    if (!user.email.includes("@")) throw new Error("Email xato"); // validatsiya
    console.log("DB: saqlandi", user);                           // saqlash
    console.log(`EMAIL -> ${user.email}: Xush kelibsiz!`);        // xabar yuborish
  }
}

// ✅ Yaxshi: har bir klass bitta vazifa
const validateUser = (user) => {
  if (!user.email.includes("@")) throw new Error("Email xato");
};
class UserRepository { save(user) { console.log("DB: saqlandi", user); } }
class Mailer { send(to, text) { console.log(`EMAIL -> ${to}: ${text}`); } }

class UserService {
  constructor(repo, mailer) { this.repo = repo; this.mailer = mailer; } // D ham shu yerda!
  register(user) {
    validateUser(user);
    this.repo.save(user);
    this.mailer.send(user.email, "Xush kelibsiz!");
  }
}

// ================= O — Open/Closed =================
const discountStrategies = {
  none: (price) => price,
  student: (price) => price * 0.8,
  blackFriday: (price) => price * 0.5,
  // yangi chegirma = yangi qator, eski kodga tegilmaydi
};
const finalPrice = (price, type) => (discountStrategies[type] ?? discountStrategies.none)(price);

// ================= L — Liskov =================
class Shape { area() { throw new Error("implement qiling"); } }
class Rectangle extends Shape { constructor(w, h) { super(); this.w = w; this.h = h; } area() { return this.w * this.h; } }
class Circle extends Shape { constructor(r) { super(); this.r = r; } area() { return Math.PI * this.r ** 2; } }
const totalArea = (shapes) => shapes.reduce((s, sh) => s + sh.area(), 0); // har qanday Shape ishlaydi

// ================= D — Dependency Inversion (test uchun) =================
class FakeRepo { saved = []; save(u) { this.saved.push(u); } }
class FakeMailer { sent = []; send(to, t) { this.sent.push({ to, t }); } }

const repo = new FakeRepo();
const mailer = new FakeMailer();
new UserService(repo, mailer).register({ email: "aziz@mail.uz" });
console.log(repo.saved.length === 1 && mailer.sent.length === 1 ? "✅ D ishlayapti" : "❌");
console.log(finalPrice(100000, "student"), totalArea([new Rectangle(2, 3), new Circle(1)]).toFixed(2));
