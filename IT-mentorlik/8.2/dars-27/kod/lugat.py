"""Inglizcha-o'zbekcha lug'at (8.2, 27-dars namunasi)."""
import random

lugat = {
    "apple": "olma", "book": "kitob", "computer": "kompyuter",
    "friend": "do'st", "school": "maktab", "water": "suv",
}

while True:
    print("\n📖 1.Tarjima 2.Qo'shish 3.Hammasi 4.Test 0.Chiqish")
    tanlov = input("> ").strip()

    if tanlov == "1":
        soz = input("Inglizcha so'z: ").strip().lower()
        print(f"➡️ {lugat.get(soz, 'Topilmadi 😕')}")
    elif tanlov == "2":
        en = input("Inglizcha: ").strip().lower()
        uz = input("O'zbekcha: ").strip().lower()
        if en and uz:
            lugat[en] = uz
            print("✅ Qo'shildi")
    elif tanlov == "3":
        for en, uz in sorted(lugat.items()):
            print(f"{en:<12} — {uz}")
        print(f"Jami: {len(lugat)} ta so'z")
    elif tanlov == "4":
        sozlar = random.sample(list(lugat), k=min(5, len(lugat)))
        ball = 0
        for en in sozlar:
            if input(f"{en} = ? ").strip().lower() == lugat[en]:
                ball += 1
                print("✅")
            else:
                print(f"❌ To'g'ri javob: {lugat[en]}")
        print(f"Natija: {ball}/{len(sozlar)}")
    elif tanlov == "0":
        break
