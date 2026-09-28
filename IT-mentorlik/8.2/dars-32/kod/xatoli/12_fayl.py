# Kutilgan natija: "Faylda 3 ta qator bor" (fayl bo'lmasa: "Fayl topilmadi")
with open("eslatma.txt", "w", encoding="utf-8") as f:
    f.write("Birinchi\nIkkinchi\nUchinchi")

try:
    with open("eslatma.txt", encoding="utf-8") as f:
        qatorlar = f.read()
    print(f"Faylda {len(qatorlar)} ta qator bor")
except FileNotFoundError
    print("Fayl topilmadi")
