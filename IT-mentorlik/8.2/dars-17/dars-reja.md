# 17-dars. DOM: elementlarni topish, yaratish, o'zgartirish

**Guruh:** 8.2 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa

## Maqsad
- DOM (Document Object Model) nima ekanini tushunadi: HTML'ning JS'dagi "daraxt" ko'rinishi.
- Elementlarni topadi: `getElementById`, `querySelector`, `querySelectorAll`.
- Kontent va stilni o'zgartiradi: `textContent`, `innerHTML`, `style`, `classList.add/remove/toggle`, atributlar.
- Element yaratadi va qo'shadi: `createElement`, `append`, `prepend`, `remove`.
- Massivdagi ma'lumotlardan DOM'da ro'yxat chizadi ("render").
- BOM (`window`, `location`, `navigator`) haqida tasavvurga ega bo'ladi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Console'da `document.body.style.background = "hotpink"` → istalgan sayt pushti bo'ladi 😄. `document.querySelectorAll("img").forEach(i => i.src = "https://cataas.com/cat")` → hamma rasmlar mushuk 🐱 |
| 5–10 | **Takrorlash** | 16-dars testi |
| 10–28 | **Yangi mavzu** | DOM daraxti (chizma). Topish, o'zgartirish, classList, yaratish, o'chirish. BOM qisqacha |
| 28–55 | **Amaliyot** | `amaliy-topshiriq.md`: dinamik mahsulotlar ro'yxati |
| 55–72 | **Challenge** | `challenge.md`: "DOM hakeri" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +20/+10/+5
