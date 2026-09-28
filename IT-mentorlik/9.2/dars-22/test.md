# 22-dars tezkor test

1. FSM nima? — Chekli holatlar mashinasi: bot qaysi holatda ekanini va keyingi qadamni biladi
2. Holatlar guruhini qanday e'lon qilamiz? — `class X(StatesGroup): a = State()`
3. Holatga o'tish? — `await state.set_state(X.a)`
4. Holat ma'lumotini saqlash? — `await state.update_data(kalit=qiymat)`
5. Hammasini tozalash? — `await state.clear()`
6. Telefon raqamini tugma orqali so'rash? — `request_contact=True`
