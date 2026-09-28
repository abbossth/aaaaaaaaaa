# 23-dars tezkor test

1. Nega botda `requests` emas, `aiohttp` ishlatamiz? — requests sinxron: kutish vaqtida bot boshqa foydalanuvchilarga javob bera olmaydi
2. So'rovga vaqt chegarasi qo'yish? — `aiohttp.ClientTimeout(total=10)`
3. 4xx/5xx javobda xato chiqarish? — `resp.raise_for_status()`
4. `/kurs 100 USD` dagi "100 USD" qayerda? — `command.args`
5. Keshlash nima uchun kerak? — Bir xil ma'lumot uchun serverga qayta-qayta so'rov yubormaslik (tezlik, limitlar)
