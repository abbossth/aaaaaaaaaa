"""Shaxsiy kundalik (8.2, 29-dars)."""
import json
from datetime import datetime
from pathlib import Path

FAYL = Path(__file__).parent / "kundalik.json"


def yuklash() -> list:
    try:
        with open(FAYL, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def saqlash(yozuvlar: list) -> None:
    with open(FAYL, "w", encoding="utf-8") as f:
        json.dump(yozuvlar, f, ensure_ascii=False, indent=2)


def main() -> None:
    yozuvlar = yuklash()
    print(f"📔 Kundalik: {len(yozuvlar)} ta yozuv")
    while True:
        tanlov = input("\n1.Yozish 2.O'qish 3.Qidirish 4.Kayfiyat statistikasi 0.Chiqish\n> ").strip()
        if tanlov == "1":
            matn = input("Bugun nima bo'ldi? ").strip()
            kayfiyat = input("Kayfiyat (1-5): ").strip()
            try:
                kayfiyat = int(kayfiyat)
                if not 1 <= kayfiyat <= 5:
                    raise ValueError
            except ValueError:
                print("❌ Kayfiyat 1 dan 5 gacha son bo'lsin")
                continue
            yozuvlar.append({"sana": datetime.now().strftime("%d.%m.%Y %H:%M"), "matn": matn, "kayfiyat": kayfiyat})
            saqlash(yozuvlar)
            print("✅ Saqlandi")
        elif tanlov == "2":
            for y in yozuvlar[-5:]:
                print(f"{y['sana']} {'⭐' * y['kayfiyat']}\n   {y['matn']}")
        elif tanlov == "3":
            soz = input("So'z: ").lower()
            for y in yozuvlar:
                if soz in y["matn"].lower():
                    print(f"{y['sana']}: {y['matn']}")
        elif tanlov == "4":
            if yozuvlar:
                ortacha = sum(y["kayfiyat"] for y in yozuvlar) / len(yozuvlar)
                print(f"O'rtacha kayfiyat: {ortacha:.1f} / 5")
        elif tanlov == "0":
            break


if __name__ == "__main__":
    main()
