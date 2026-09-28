# Kutilgan: 7 -> "Tub", 9 -> "Tub emas", 1 -> "Tub emas", 2 -> "Tub"
n = int(input("Son: "))
tub = True
for d in range(2, n):
    if n % d == 0:
        tub = False
if tub:
    print("Tub")
else:
    print("Tub emas")
