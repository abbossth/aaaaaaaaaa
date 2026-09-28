# 9-dars slaydlari: Clean Code

## 1-slayd
📖 *"Kodni kompyuter uchun emas, odamlar uchun yozing."* — Martin Fowler (mazmunan)

## 2-slayd — Nomlash
❌ `d`, `data`, `temp`, `x1`, `handle()`, `doStuff()`
✅ `daysUntilDeadline`, `activeUsers`, `calculateTotalPrice()`, `isEmailValid`
Boolean: `is/has/can` · Funksiya: fe'l · O'zgaruvchi: ot

## 3-slayd — Kichik funksiyalar
- Bitta funksiya = bitta vazifa
- 20 qatordan kam (ideal)
- ≤ 3 parametr (ko'p bo'lsa → obyekt)
- Ichma-ichlik 2 darajadan oshmasin

## 4-slayd — Guard clause
```js
// ❌
function pay(user) {
  if (user) {
    if (user.balance > 0) {
      if (!user.blocked) { /* ... */ }
    }
  }
}
// ✅
function pay(user) {
  if (!user) return;
  if (user.balance <= 0) return;
  if (user.blocked) return;
  /* ... */
}
```

## 5-slayd — Sehrli sonlar
❌ `if (age > 17 && total > 500000) price *= 0.95;`
✅ `const ADULT_AGE = 18; const DISCOUNT_THRESHOLD = 500_000; const DISCOUNT_RATE = 0.05;`

## 6-slayd — DRY · KISS · YAGNI
**DRY:** Don't Repeat Yourself (takrorlanmang)
**KISS:** Keep It Simple, Stupid (sodda qiling)
**YAGNI:** You Aren't Gonna Need It (kerak bo'lmaydigan narsani yozmang)

## 7-slayd — Code smells 👃
Uzun funksiya · Takrorlanish · Chuqur ichma-ichlik · Ko'p parametr · Noaniq nom · Sehrli son · O'lik kod · Izoh bilan "bezatilgan" yomon kod
