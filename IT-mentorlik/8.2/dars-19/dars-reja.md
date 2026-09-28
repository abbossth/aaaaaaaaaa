# 19-dars. Forma validatsiyasi + localStorage — To-Do ilova

**Guruh:** 8.2 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa

## Maqsad
- 16–18-darslardagi bilimlarni (massiv, obyekt, DOM, eventlar) bitta ilovada birlashtiradi.
- "State → render" g'oyasini tushunadi: ma'lumot massivda, ekran esa undan chiziladi.
- Forma ma'lumotlarini tekshiradi (validatsiya): bo'sh, juda qisqa, takroriy.
- `localStorage` bilan ma'lumotni saqlaydi, sahifa yangilanganda qayta yuklaydi.
- To'liq CRUD'li To-Do ilova yaratadi: qo'shish, belgilash, tahrirlash, o'chirish, filtrlash.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Tayyor To-Do'ni ko'rsatish: vazifa qo'shiladi → sahifa yangilanadi (`F5`) → vazifalar joyida! *"Bugun shuni noldan yasaymiz. Bu sizning portfoliongizdagi birinchi haqiqiy ilova."* |
| 5–10 | **Takrorlash** | 18-dars testi |
| 10–20 | **Arxitektura** | Doskada: `state (todos massivi)` → `render()` → DOM. Har bir harakat: state'ni o'zgartir → `save()` → `render()` |
| 20–55 | **Jonli + amaliyot** | Mentor bilan qadamma-qadam (`amaliy-topshiriq.md`), o'quvchilar parallel yozadi |
| 55–72 | **Challenge** | `challenge.md`: "Feature poygasi" |
| 72–80 | **Yakun** | Deploy (Netlify), XP, uyga vazifa |

## Baholash (XP)
- Asosiy CRUD +10 · localStorage +10 · Validatsiya +5 · Challenge feature'lari +5 har biri
