# 14-dars amaliy topshiriq: `utils.js` — funksiyalar kutubxonasi

## 🟢 Oson (+5 XP)
Quyidagi funksiyalarni **arrow** usulida yozing va Console'da tekshiring:
1. `sum(a, b)`, `max(a, b)`
2. `isEven(n)` — true/false
3. `greet(name, lang = "uz")` — `"Salom, Aziz!"` yoki `"Hello, Aziz!"`

## 🟡 O'rta (+10 XP)
4. `isPrime(n)` — tub sonmi?
5. `isPalindrome(s)` — `"Kiyik"` → true (katta-kichik harfga e'tiborsiz)
6. `formatPrice(1250000)` → `"1 250 000 so'm"` (`toLocaleString` ni internetdan o'rganing)
7. `randomInt(min, max)` — oraliqdagi tasodifiy butun son

## 🔴 Qiyin (+20 XP)
8. `bmi(weightKg, heightCm)` — obyekt qaytarsin: `{ value: 22.5, category: "Normal" }`
9. Barcha funksiyalarni `utils.js` faylida `export` qiling va `app.js` da `import` qilib ishlating (`<script type="module" src="app.js">`).
10. `countdown(n)` — `setInterval` bilan sahifada teskari sanoq (10, 9, ... 0 🚀).

Namuna: `kod/utils.js`
