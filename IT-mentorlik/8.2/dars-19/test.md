# 19-dars tezkor test

1. "State → render" nimani anglatadi? — Ma'lumot massivda saqlanadi, ekran har safar undan qayta chiziladi
2. Sahifa yangilanganda ma'lumot saqlanishi uchun? — `localStorage` + `JSON.stringify/parse`
3. `JSON.parse(localStorage.getItem("todos")) || []` dagi `|| []` nima uchun? — Birinchi marta ma'lumot yo'q bo'lsa, bo'sh massiv
4. Nega vazifa matnini `innerHTML` emas, `textContent` bilan qo'yamiz? — XSS'dan himoya
5. Dinamik elementlar uchun eventlarni qanday qo'shamiz? — Event delegation (ota elementga)
