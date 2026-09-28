# 4. Uchburchak
a, b, c = (float(input(f"{i}-tomon: ")) for i in range(1, 4))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Teng tomonli")
    elif a == b or b == c or a == c:
        print("Teng yonli")
    else:
        print("Turli tomonli")
else:
    print("Bunday uchburchak mavjud emas")

# 5. Parol kuchi
parol = input("Parol: ")
ball = 0
if len(parol) >= 8: ball += 1
if any(c.isdigit() for c in parol): ball += 1
if any(c.isupper() for c in parol): ball += 1
if any(c.islower() for c in parol): ball += 1
if ball <= 1:
    print("Kuchsiz")
elif ball <= 3:
    print("O'rta")
else:
    print("Kuchli")

# 6. Bosqichli tarif
sarf = float(input("Sarf (kVt·soat): "))
if sarf <= 200:
    tolov = sarf * 600
elif sarf <= 1000:
    tolov = 200 * 600 + (sarf - 200) * 1000
else:
    tolov = 200 * 600 + 800 * 1000 + (sarf - 1000) * 1500
print(f"To'lov: {tolov:,.0f} so'm")
