# 11-dars slaydlari: Sifat darvozalari

## 1-slayd
🚦 **Kod main'ga kirishdan oldin — tekshiruvdan o'tadi**

## 2-slayd — 3 ta darvoza
🎨 **Prettier:** formatlash (probel, qo'shtirnoq, qator uzunligi). Bahs yo'q!
🔍 **ESLint:** xatolar va yomon amaliyotlar (ishlatilmagan o'zgaruvchi, `==`)
🧪 **Testlar:** kod to'g'ri ishlayaptimi?

## 3-slayd — Test piramidasi
```
       /\      E2E (kam, sekin)
      /  \     Integratsion
     /____\    Unit (ko'p, tez) ← bugun
```

## 4-slayd — Vitest
```js
import { describe, it, expect } from "vitest";
import { calculateTotal } from "../src/cart.js";

describe("calculateTotal", () => {
  it("bo'sh savat uchun 0 qaytaradi", () => {
    expect(calculateTotal([])).toBe(0);
  });
});
```

## 5-slayd — AAA
```js
it("chegirmani qo'llaydi", () => {
  const items = [{ price: 600000, qty: 1 }];    // Arrange
  const total = calculateTotal(items);          // Act
  expect(total).toBe(570000);                   // Assert
});
```

## 6-slayd — Nimani test qilish kerak?
✅ Oddiy holat · ✅ Chegaraviy holat (0, bo'sh, maksimum, 499 999 va 500 000)
✅ Noto'g'ri kiritish (`toThrow`) · ❌ Kutubxonalarning o'zini test qilmang

## 7-slayd — Matcher'lar
`toBe` (===) · `toEqual` (obyekt/massiv) · `toThrow` · `toBeCloseTo` (kasr) · `toContain` · `toHaveLength`

## 8-slayd — package.json skriptlari
```json
"scripts": {
  "test": "vitest run",
  "lint": "eslint .",
  "format": "prettier --write ."
}
```
