# 36-dars mentor eslatmasi

- 8.10 uchun To-Do soddalashtirilgan: har bir tugmaga alohida listener (event delegation yo'q). Kengroq variant: `../../8.2/dars-19/kod/` (filtr, delegation, `textContent` bilan XSS himoyasi).
- `innerHTML` ga foydalanuvchi matnini qo'ymang — `textContent` ishlating. Bunga 1 jumla bilan to'xtaling: "Kimdir vazifa o'rniga `<img onerror=...>` yozsa..."
- Eng ko'p xato: `JSON.parse(null)` → `null` bo'ladi, shuning uchun `|| []`. `localStorage.setItem("vazifalar", vazifalar)` (stringify'siz) → `"[object Object]"`.
- Maktab kompyuterlarida brauzer yopilganda localStorage tozalanishi mumkin (mehmon rejimi). Uyda sinab ko'rishni so'rang.
