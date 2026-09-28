# Review javoblari (mentor uchun)

1. **Parol kodda saqlangan** (`PAROL = "admin123"`) + "master parol" orqasidagi eshik (backdoor): istalgan foydalanuvchi sifatida kirish mumkin. **Xavfsizlik!**
2. **Parollar ochiq holda** JSON'da saqlanadi va taqqoslanadi. Hash kerak (keyinroq, `bcrypt`, 46-dars).
3. **`eval(ifoda)`**: foydalanuvchi istalgan Python kodini bajarishi mumkin (`__import__('os').system(...)`). **Jiddiy xavfsizlik!**
4. **Fayl yopilmaydi:** `open()` `with`siz ishlatilgan. `encoding` ham yo'q.
5. **Xato:** `u == None` bo'lsa, "Xato" chiqadi, lekin funksiya davom etadi va `u["parol"]` → `TypeError`. `return` yoki `else` kerak.
6. **Yomon nomlar:** `f`, `a`, `d`, `x`, `l`, `p`, `u`.
7. **`== None`** o'rniga `is None`.
8. **DRY buzilgan:** `chegirma1/2/3` → bitta `chegirma(narx, foiz)`. Muvaffaqiyatsiz login holatida `login()` `None` qaytaradi (aniq `False` qaytarish kerak).
