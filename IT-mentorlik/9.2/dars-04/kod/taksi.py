TARIFLAR = {"ekonom": (7000, 2000), "komfort": (10000, 2800), "biznes": (20000, 4500)}

km = float(input("Masofa (km): "))
soat = int(input("Soat (0-23): "))
tarif = input("Tarif (ekonom/komfort/biznes): ").strip().lower()
yomgir = input("Yomg'ir (ha/yo'q): ").strip().lower() == "ha"

if tarif not in TARIFLAR:
    print("Xato: bunday tarif yo'q")
elif not 0 <= soat <= 23:
    print("Xato: soat 0 dan 23 gacha bo'lishi kerak")
elif km <= 0:
    print("Xato: masofa musbat bo'lishi kerak")
else:
    boshlangich, km_narx = TARIFLAR[tarif]
    narx = boshlangich + km * km_narx
    if soat >= 22 or soat < 6:
        narx *= 1.2
    if yomgir:
        narx *= 1.3
    if km > 50:
        narx *= 0.9
    narx = max(narx, boshlangich)
    print(f"Narx: {narx:,.0f} so'm")
