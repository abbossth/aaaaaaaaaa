# 34-dars tezkor test

1. Reply tugma bosilganda botga nima keladi? — Oddiy matnli xabar
2. Inline tugma bosilganda? — Callback query (`callback_data`)
3. Inline tugmani qaysi dekorator ushlaydi? — `@dp.callback_query(...)`
4. `callback.answer()` yozilmasa? — Tugmada soat belgisi ⏳ uzoq aylanib turadi
5. `kb.adjust(2, 1)` nimani anglatadi? — 1-qatorda 2 ta, 2-qatorda 1 ta tugma
6. Xabarni yangi yubormasdan o'zgartirish? — `callback.message.edit_text(...)`
