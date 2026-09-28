# 10-dars amaliy topshiriq

## 🟢 Oson (+5 XP)
`kod/solid.js` ni ishga tushiring (`node solid.js`). Har bir bo'limga o'z so'zingiz bilan 1 jumlalik izoh yozing: bu kod qaysi tamoyilni qanday bajaradi?

## 🟡 O'rta (+10 XP)
`kod/buzilgan.js` dagi `Order` klassini tahlil qiling:
1. SRP qayerda buzilgan? `Order` nechta "sabab" bilan o'zgarishi mumkin?
2. OCP qayerda buzilgan? "Uzum Nasiya" to'lovini qo'shish uchun nimani o'zgartirish kerak?
Javoblarni `TAHLIL.md` ga yozing.

## 🔴 Qiyin (+20 XP)
`Order` ni refaktoring qiling:
- `Order` faqat mahsulotlar va summani bilsin
- `PaymentProcessor` + `paymentProviders` obyekti (OCP): Click, Payme, Cash
- `OrderRepository`, `ReceiptPrinter`, `SmsNotifier`
- `OrderService` barcha bog'liqliklarni **konstruktor orqali** olsin (DIP)
- Yangi to'lov turini (Uzum Nasiya) **eski kodga tegmasdan** qo'shib ko'rsating
- Fake repo va fake notifier bilan tekshiring (`solid.js` oxiridagi kabi)
