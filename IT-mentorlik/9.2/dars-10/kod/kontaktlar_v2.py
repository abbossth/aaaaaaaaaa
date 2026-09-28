"""Kontaktlar kitobi v2 — funksiyalarga bo'lingan versiya."""

GURUHLAR = ("do'st", "oila", "sinfdosh", "boshqa")


def tel_tozalash(tel: str) -> str | None:
    """Telefonni 998XXXXXXXXX formatiga keltiradi, noto'g'ri bo'lsa None qaytaradi."""
    raqamlar = "".join(c for c in tel if c.isdigit())
    if len(raqamlar) == 9:
        raqamlar = "998" + raqamlar
    if len(raqamlar) == 12 and raqamlar.startswith("998"):
        return raqamlar
    return None


def tel_format(tel: str) -> str:
    """998901234567 -> +998 90 123-45-67"""
    return f"+{tel[:3]} {tel[3:5]} {tel[5:8]}-{tel[8:10]}-{tel[10:]}"


def kontakt_qoshish(kontaktlar: dict) -> None:
    ism = input("Ism: ").strip().title()
    if not ism:
        print("❌ Ism bo'sh bo'lmasin")
        return
    tel = tel_tozalash(input("Telefon: "))
    if tel is None:
        print("❌ Telefon noto'g'ri")
        return
    guruh = input(f"Guruh {GURUHLAR}: ").strip().lower()
    kontaktlar[ism] = {
        "tel": tel,
        "email": input("Email: ").strip().lower() or None,
        "guruh": guruh if guruh in GURUHLAR else "boshqa",
    }
    print(f"✅ {ism} saqlandi")


def kontakt_qatori(ism: str, m: dict) -> str:
    return f"{ism:<15} {tel_format(m['tel'])}  {m['email'] or '-':<22} [{m['guruh']}]"


def hammasini_korsat(kontaktlar: dict) -> None:
    if not kontaktlar:
        print("📭 Bo'sh")
        return
    for i, ism in enumerate(sorted(kontaktlar), 1):
        print(f"{i:>2}. {kontakt_qatori(ism, kontaktlar[ism])}")


def qidirish(kontaktlar: dict, soz: str = "", **filtrlar) -> dict:
    """Ism bo'yicha qisman qidiradi. Filtrlar: guruh="do'st", email_bor=True"""
    natija = {}
    for ism, m in kontaktlar.items():
        if soz.lower() not in ism.lower():
            continue
        if "guruh" in filtrlar and m["guruh"] != filtrlar["guruh"]:
            continue
        if filtrlar.get("email_bor") and not m["email"]:
            continue
        natija[ism] = m
    return natija


def ochirish(kontaktlar: dict, ism: str) -> bool:
    return kontaktlar.pop(ism.title(), None) is not None


def menyu() -> str:
    print("\n📒 1.Qo'shish 2.Hammasi 3.Qidirish 4.O'chirish 0.Chiqish")
    return input("> ").strip()


def main() -> None:
    kontaktlar: dict = {}
    while True:
        match menyu():
            case "1":
                kontakt_qoshish(kontaktlar)
            case "2":
                hammasini_korsat(kontaktlar)
            case "3":
                hammasini_korsat(qidirish(kontaktlar, input("Qidiruv: ")))
            case "4":
                print("🗑 O'chirildi" if ochirish(kontaktlar, input("Ism: ")) else "Topilmadi")
            case "0":
                break
            case _:
                print("Noma'lum buyruq")


if __name__ == "__main__":
    main()
