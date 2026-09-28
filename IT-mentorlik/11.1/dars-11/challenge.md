# 11-dars challenge: "Mutant ovchisi" 🧟

**Vaqt:** 13 daqiqa | **Format:** juftliklar

**Mutation testing** g'oyasi: agar kodga ataylab xato ("mutant") kiritilsa, testlar buni ushlashi kerak. Ushlamasa, testlar yetarli emas!

## 1-raund: Mutant yaratish (5 daqiqa)
Juftlik A `src/cart.js` ga **bitta** yashirin mutant kiritadi. Masalan:
- `>=` → `>`
- `0.05` → `0.5`
- `startsWith("998")` → `includes("998")`
- `throw` qatorini o'chirish

## 2-raund: Ovlash (8 daqiqa)
Juftlik B faqat `npm test` natijasiga qarab (kodni o'qimasdan!) mutant bor-yo'qligini aytadi.
- Test qizarsa → mutant ushlandi (+5 B'ga).
- Test yashil qolsa → mutant "tirik qoldi" (+5 A'ga). B mutantni o'ldiradigan **yangi test** yozsa, +10.

Keyin rollar almashadi.

**Xulosa:** 100% yashil testlar kod xatosiz degani emas. Yaxshi testlar chegaraviy holatlarni ham tekshiradi.
**XP:** 🥇 +20 · 🥈 +10 · 🥉 +5
