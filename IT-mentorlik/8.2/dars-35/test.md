# 35-dars tezkor test

1. FSM nima uchun kerak? — Bot har bir foydalanuvchi qaysi bosqichda ekanini eslab qolishi uchun
2. Holatlar qaysi klassdan meros oladi? — `StatesGroup`
3. Keyingi holatga o'tish? — `await state.set_state(Royxat.yosh)`
4. Yig'ilgan ma'lumotni saqlash? — `await state.update_data(kalit=qiymat)`
5. Hammasini olish? — `await state.get_data()`
6. Holatdan chiqish? — `await state.clear()`
7. Telefon raqamni tugma orqali so'rash? — `request_contact=True`
