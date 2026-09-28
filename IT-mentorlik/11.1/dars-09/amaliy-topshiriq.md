# 9-dars amaliy topshiriq: Refaktoring

**Qoida:** refaktoring — kodning **xatti-harakatini o'zgartirmasdan** tuzilishini yaxshilash. Har bir refaktoringdan oldin va keyin bir xil kirish qiymatlari bilan natijani tekshiring!

## 🟢 Oson (+5 XP): `kod/refaktor-1.js`
Nomlarni tuzating, sehrli sonlarni konstantaga chiqaring, `if/else return true/false` ni soddalashtiring.

## 🟡 O'rta (+10 XP): `kod/refaktor-2.js`
Takrorlanishni umumiy `sendEmail(user, subject, body)` funksiyasiga chiqaring. Guard clause va `isValidEmail` funksiyasini qo'llang. Template literal ishlating.

## 🔴 Qiyin (+20 XP): `kod/refaktor-3.js`
`processOrder` ni kichik funksiyalarga ajrating: `validateOrder`, `calculateSubtotal`, `calculateDelivery`, `applyPromo`, `notifyUser`. Promo kodlar obyektda saqlansin (`const PROMOS = { MAKTAB10: 0.1, YANGI20: 0.2 }`), shunda yangi promo qo'shish uchun kodni o'zgartirish shart bo'lmaydi. Bu keyingi darsdagi SOLID'ning "O" harfi!

**Tekshirish:** refaktoringdan oldin va keyin bir xil buyurtma bilan `console.log(processOrder(...))` natijasi bir xil bo'lishi kerak.
