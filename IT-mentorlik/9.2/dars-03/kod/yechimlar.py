# 2. Yosh kalkulyatori
yil = int(input("Tug'ilgan yilingiz: "))
print(f"Hozir: {2026 - yil} yosh, 2030-yilda: {2030 - yil} yosh")

# 3. Taksi narxi
km = float(input("Masofa (km): "))
narx = 7000 + km * 2500
print(f"To'lov: {narx:,.2f} so'm")

# 4. Valyuta
KURS = 12800
dollar = float(input("Dollar: "))
print(f"{dollar} $ = {dollar * KURS:,.0f} so'm")

# 5. Soniya konvertori
s = int(input("Soniyalar: "))
kun = s // 86400
soat = s % 86400 // 3600
daqiqa = s % 3600 // 60
soniya = s % 60
print(f"{kun} kun {soat} soat {daqiqa} daqiqa {soniya} soniya")

# 6. int("3.5") -> ValueError, chunki int() faqat butun son yozilgan matnni qabul qiladi.
# float("3.5") -> 3.5, keyin int(3.5) -> 3 (kasr qismi tashlab yuboriladi, yaxlitlanmaydi).
