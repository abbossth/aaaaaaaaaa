# Kutilgan natija (eng kuchli 3 ta):
# 1. Madina — 98
# 2. Jasur — 91
# 3. Aziz — 87
natijalar = {"Aziz": 87, "Madina": 98, "Bekzod": 75, "Jasur": 91, "Laylo": 80}
reyting = sorted(natijalar.items(), key=lambda x: x[1], reverse=True)  # XATO 1: ism bo'yicha, o'sish tartibida | mantiqiy
for i, (ism, ball) in enumerate(reyting[:3], start=1):                 # XATO 2: 0 dan sanaydi | mantiqiy
    print(f"{i}. {ism} — {ball}")
