# 4. Tub son (for...else)
n = int(input("Son: "))
if n < 2:
    print("Tub emas")
else:
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            print("Tub emas")
            break
    else:
        print("Tub son")

# 5. Raqamlar
n = int(input("Musbat son: "))
yigindi, teskari = 0, 0
while n > 0:
    r = n % 10
    yigindi += r
    teskari = teskari * 10 + r
    n //= 10
print(yigindi, teskari)

# 6. Kalkulyator REPL
while True:
    qator = input(">>> ").strip()
    if qator == "exit":
        break
    try:
        a, op, b = qator.split()
        a, b = float(a), float(b)
    except ValueError:
        print("Format: son operator son (masalan: 5 + 3)")
        continue
    match op:
        case "+": print(a + b)
        case "-": print(a - b)
        case "*": print(a * b)
        case "/": print(a / b if b != 0 else "0 ga bo'lib bo'lmaydi")
        case "**": print(a ** b)
        case _: print("Noma'lum operator")

# 7. Kompyuter sonni topadi (binar qidiruv)
past, yuqori = 1, 100
for urinish in range(1, 8):
    taxmin = (past + yuqori) // 2
    javob = input(f"{taxmin}? (katta/kichik/topdi): ")
    if javob == "topdi":
        print(f"{urinish} urinishda topdim! 😎")
        break
    elif javob == "katta":
        past = taxmin + 1
    else:
        yuqori = taxmin - 1
