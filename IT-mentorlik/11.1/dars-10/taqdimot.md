# 10-dars slaydlari: SOLID

## 1-slayd
🧱 **SOLID** — mustahkam kod uchun 5 tamoyil (Robert C. Martin)

## 2-slayd — S: Single Responsibility
**Bitta modul — bitta sabab o'zgarish uchun**
```js
// ❌ Hisobot ham hisoblaydi, ham formatlaydi, ham email yuboradi
class Report { calculate() {} toHTML() {} sendEmail() {} }
// ✅
class ReportCalculator {}  class ReportFormatter {}  class EmailSender {}
```

## 3-slayd — O: Open/Closed
**Kengaytirishga ochiq, o'zgartirishga yopiq**
```js
// ❌ yangi to'lov turi = if qo'shish
if (type === "click") ... else if (type === "payme") ...
// ✅ yangi to'lov = yangi obyekt, eski kod o'zgarmaydi
const providers = { click: new ClickPay(), payme: new PaymePay() };
providers[type].pay(amount);
```

## 4-slayd — L: Liskov Substitution
**Bola klass ota klass o'rnida muammosiz ishlashi kerak**
❌ `Penguin extends Bird` → `fly()` xato beradi 🐧
✅ `Bird` → `FlyingBird`, `SwimmingBird`

## 5-slayd — I: Interface Segregation
**Keraksiz metodlarga majburlamang**
❌ `Printer { print(); scan(); fax(); }` — oddiy printer "fax" qila olmaydi
✅ Kichik interfeyslar: `Printable`, `Scannable`

## 6-slayd — D: Dependency Inversion
**Aniq klassga emas, abstraksiyaga bog'laning**
```js
// ❌ class OrderService { db = new PostgresDB(); }
// ✅ class OrderService { constructor(db) { this.db = db; } }
new OrderService(new PostgresDB());   // production
new OrderService(new FakeDB());       // test
```

## 7-slayd — Qachon qo'llash kerak?
SOLID — qonun emas, **kompas**. Kichik skriptga 10 ta klass yozmang (YAGNI!).
Signal: "Bitta o'zgarish uchun 5 ta faylni tuzatyapman" → tamoyil buzilgan.
