# Kutilgan: summa >= 100000 bo'lsa 10% chegirma, >= 500000 bo'lsa 20%.
# 50000 -> 50000, 200000 -> 180000, 600000 -> 480000
summa = float(input("Summa: "))
if summa >= 100000:
    chegirma = 0.1
elif summa >= 500000:
    chegirma = 0.2
print(f"To'lov: {summa - summa * chegirma:.0f}")
