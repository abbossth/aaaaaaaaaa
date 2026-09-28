"""Kontaktlar kitobi v3 — JSON faylga saqlaydi va xatolarga chidamli."""
import csv
import json
import shutil
from pathlib import Path

FAYL = Path("kontaktlar.json")
BACKUP = Path("kontaktlar.backup.json")


class NotogriTelefon(Exception):
    """Telefon raqami noto'g'ri formatda."""


def tel_tozalash(tel: str) -> str:
    raqamlar = "".join(c for c in tel if c.isdigit())
    if len(raqamlar) == 9:
        raqamlar = "998" + raqamlar
    if len(raqamlar) != 12 or not raqamlar.startswith("998"):
        raise NotogriTelefon(f"'{tel}' — noto'g'ri raqam")
    return raqamlar


def yuklash() -> dict:
    try:
        with open(FAYL, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("⚠️ Fayl buzilgan. Backup'dan tiklashga urinamiz...")
        try:
            with open(BACKUP, encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}


def saqlash(kontaktlar: dict) -> None:
    if FAYL.exists():
        shutil.copy(FAYL, BACKUP)
    with open(FAYL, "w", encoding="utf-8") as f:
        json.dump(kontaktlar, f, ensure_ascii=False, indent=2)


def qoshish(kontaktlar: dict) -> None:
    ism = input("Ism: ").strip().title()
    if not ism:
        print("❌ Ism bo'sh")
        return
    try:
        tel = tel_tozalash(input("Telefon: "))
    except NotogriTelefon as e:
        print(f"❌ {e}")
        return
    kontaktlar[ism] = {"tel": tel, "email": input("Email: ").strip().lower() or None}
    saqlash(kontaktlar)
    print("✅ Saqlandi")


def csv_eksport(kontaktlar: dict, fayl: str = "kontaktlar.csv") -> None:
    with open(fayl, "w", newline="", encoding="utf-8") as f:
        yozuvchi = csv.writer(f)
        yozuvchi.writerow(["ism", "tel", "email"])
        for ism, m in kontaktlar.items():
            yozuvchi.writerow([ism, m["tel"], m["email"] or ""])
    print(f"📤 {fayl} ga eksport qilindi")


def main() -> None:
    kontaktlar = yuklash()
    print(f"📒 {len(kontaktlar)} ta kontakt yuklandi")
    while True:
        tanlov = input("\n1.Qo'shish 2.Hammasi 3.O'chirish 4.CSV eksport 0.Chiqish\n> ").strip()
        match tanlov:
            case "1":
                qoshish(kontaktlar)
            case "2":
                for ism, m in sorted(kontaktlar.items()):
                    print(f"  {ism:<15} +{m['tel']}  {m['email'] or '-'}")
            case "3":
                if kontaktlar.pop(input("Ism: ").strip().title(), None):
                    saqlash(kontaktlar)
                    print("🗑 O'chirildi")
                else:
                    print("Topilmadi")
            case "4":
                csv_eksport(kontaktlar)
            case "0":
                break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Xayr!")
