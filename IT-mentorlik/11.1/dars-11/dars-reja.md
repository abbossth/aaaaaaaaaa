# 11-dars. Sifat darvozalari: ESLint, Prettier, unit test (Vitest)

**Guruh:** 11.1 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** I bob, "Unit-test va hujjatlashtirish orqali sifatni nazorat qilish"

## Maqsad
- "Sifat darvozasi" (quality gate) tushunchasini biladi: kod main'ga kirishidan oldin avtomatik tekshiruvlardan o'tadi.
- **Prettier** (formatlash) va **ESLint** (xato va yomon amaliyotlarni topish) ni sozlaydi va ishlatadi.
- **Vitest** bilan unit test yozadi: `describe`, `it/test`, `expect`, `toBe`, `toEqual`, `toThrow`.
- AAA (Arrange–Act–Assert) tuzilmasini va chegaraviy holatlarni (edge cases) test qilishni tushunadi.
- `npm run lint`, `npm run format`, `npm test` skriptlarini sozlaydi. Bular 34-darsdagi CI'ga tayyorgarlik.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | 9-darsdagi refaktoringni eslash: *"Har safar qo'lda tekshirdingiz. Loyihada 500 ta funksiya bo'lsa-chi? Robot tekshirsin!"* Ekranda: `npm test` → 40 ta yashil ✓ 0.3 soniyada |
| 5–10 | **Takrorlash** | 10-dars testi |
| 10–25 | **Yangi mavzu** | Test piramidasi (unit → integratsion → E2E). Vitest sintaksisi. AAA. Edge case'lar. ESLint va Prettier farqi |
| 25–35 | **Jonli** | `kod/sifat-demo` ni noldan sozlash: `npm i -D vitest eslint prettier`, config, skriptlar |
| 35–62 | **Amaliyot** | `amaliy-topshiriq.md` |
| 62–75 | **Challenge** | `challenge.md`: "Mutant ovchisi" 🧟 |
| 75–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Sozlangan loyiha +10 · Testlar +5/+10/+20 · Mutant ovchisi +20/+10/+5
