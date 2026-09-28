"""Asosiy funksiyalar (3-a'zo)."""


def qoshish(data: dict) -> None:
    nom = input("Nomi: ").strip()
    if not nom:
        print("❌ Bo'sh bo'lmasin")
        return
    data["elementlar"].append({"nom": nom})
    print("✅ Qo'shildi")


def korsatish(data: dict) -> None:
    if not data["elementlar"]:
        print("📭 Bo'sh")
    for i, el in enumerate(data["elementlar"], 1):
        print(f"{i}. {el['nom']}")
