# 21-dars mentor eslatmasi

## Ko'p uchraydigan xatolar
| Xato | Yechim |
|---|---|
| Inline tugma bosilganda "soat" belgisi aylanib turadi | `await callback.answer()` unutilgan |
| `callback_data` 64 baytdan uzun → xato | Qisqa kodlar: `"q:2:1"` |
| `F.text == "Menyu"` ishlamaydi, tugmada `"🍽 Menyu"` | Emoji ham matnning bir qismi! |
| `edit_text` → "message is not modified" | Yangi matn eskisi bilan bir xil. Bu xatoni e'tiborsiz qoldirish mumkin |
| Savat ma'lumotlari bot o'chganda yo'qoladi | Normal: hozircha xotirada. 23-darsda JSON, 36-darsda PostgreSQL |

## Maslahat
`savatlar` lug'ati global. Bu hozircha yetarli. 22-darsdagi FSM holatni to'g'ri boshqarish usulini ko'rsatadi.
