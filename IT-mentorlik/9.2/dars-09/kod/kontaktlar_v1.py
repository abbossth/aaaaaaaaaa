kontaktlar = {}

while True:
    print("\n📒 KONTAKTLAR KITOBI v1")
    print("1. Qo'shish  2. Hammasi  3. Qidirish  4. Tahrirlash  5. O'chirish  6. Guruh  7. Statistika  0. Chiqish")
    tanlov = input("> ").strip()

    match tanlov:
        case "1":
            ism = input("Ism: ").strip().title()
            if ism in kontaktlar and input("Mavjud. Yangilaysizmi? (ha/yo'q): ") != "ha":
                continue
            tel = "".join(c for c in input("Telefon: ") if c.isdigit())
            if len(tel) == 9:
                tel = "998" + tel
            if len(tel) != 12 or not tel.startswith("998"):
                print("❌ Telefon noto'g'ri")
                continue
            kontaktlar[ism] = {
                "tel": tel,
                "email": input("Email (bo'sh qoldirish mumkin): ").strip().lower() or None,
                "guruh": input("Guruh (do'st/oila/sinfdosh): ").strip().lower() or "boshqa",
            }
            print(f"✅ {ism} qo'shildi")
        case "2":
            if not kontaktlar:
                print("Bo'sh")
            for i, (ism, m) in enumerate(sorted(kontaktlar.items()), 1):
                print(f"{i}. {ism:<15} +{m['tel']}  {m['email'] or '-':<20} [{m['guruh']}]")
        case "3":
            q = input("Qidiruv: ").lower()
            topildi = {i: m for i, m in kontaktlar.items() if q in i.lower()}
            print(topildi or "Topilmadi")
        case "4":
            ism = input("Kimni tahrirlaymiz: ").title()
            if ism not in kontaktlar:
                print("Topilmadi")
                continue
            for maydon in ("tel", "email", "guruh"):
                yangi = input(f"{maydon} [{kontaktlar[ism][maydon]}]: ").strip()
                if yangi:
                    kontaktlar[ism][maydon] = yangi
        case "5":
            ism = input("Kimni o'chiramiz: ").title()
            print("🗑 O'chirildi" if kontaktlar.pop(ism, None) else "Topilmadi")
        case "6":
            g = input("Guruh: ").lower()
            print([i for i, m in kontaktlar.items() if m["guruh"] == g])
        case "7":
            guruhlar = {m["guruh"] for m in kontaktlar.values()}
            print({g: sum(1 for m in kontaktlar.values() if m["guruh"] == g) for g in guruhlar})
            print("Email yo'q:", sum(1 for m in kontaktlar.values() if not m["email"]))
        case "0":
            print("Xayr! 👋")
            break
        case _:
            print("Noma'lum buyruq")
