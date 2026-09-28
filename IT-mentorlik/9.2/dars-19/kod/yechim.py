"""Oraliq nazorat #1 — namuna yechim (FAQAT MENTOR UCHUN)."""
import json


# 1-vazifa
def matn_tahlili(matn: str) -> dict:
    sozlar = matn.split()
    return {
        "sozlar": len(sozlar),
        "harflar": sum(c.isalpha() for c in matn),
        "eng_uzun": max(sozlar, key=len) if sozlar else "",
        "unlilar": sum(c in "aeiou" for c in matn.lower()),
    }


# 2-vazifa
def hisobot(fayl_nomi: str) -> None:
    natija, otkazilgan = {}, 0
    try:
        with open(fayl_nomi, encoding="utf-8") as f:
            for qator in f:
                qismlar = qator.strip().split(",")
                try:
                    ism, *baholar = qismlar
                    baholar = [int(b) for b in baholar]
                    if not ism or len(baholar) != 3 or not all(2 <= b <= 5 for b in baholar):
                        raise ValueError
                except ValueError:
                    otkazilgan += 1
                    continue
                natija[ism] = round(sum(baholar) / 3, 2)
    except FileNotFoundError:
        print(f"❌ {fayl_nomi} topilmadi")
        return
    with open("hisobot.json", "w", encoding="utf-8") as f:
        json.dump({"oquvchilar": natija, "otkazilgan": otkazilgan}, f, ensure_ascii=False, indent=2)


# 3-vazifa
class KutubxonaXatosi(Exception):
    pass


class Kitob:
    def __init__(self, nom: str, muallif: str):
        self.nom, self.muallif = nom, muallif
        self._kimda = None

    @property
    def mavjud(self) -> bool:
        return self._kimda is None

    def __str__(self) -> str:
        return f"{self.nom} — {self.muallif} ({'mavjud' if self.mavjud else 'band'})"


class Azo:
    LIMIT = 3

    def __init__(self, ism: str):
        self.ism = ism
        self.kitoblar: list[Kitob] = []


class Kutubxona:
    def __init__(self):
        self._kitoblar: dict[str, Kitob] = {}

    def kitob_qosh(self, kitob: Kitob) -> None:
        self._kitoblar[kitob.nom] = kitob

    def _top(self, nom: str) -> Kitob:
        if nom not in self._kitoblar:
            raise KutubxonaXatosi(f"'{nom}' kitobi yo'q")
        return self._kitoblar[nom]

    def ber(self, nom: str, azo: Azo) -> None:
        kitob = self._top(nom)
        if not kitob.mavjud:
            raise KutubxonaXatosi(f"'{nom}' band")
        if len(azo.kitoblar) >= Azo.LIMIT:
            raise KutubxonaXatosi(f"{azo.ism} limitga yetgan")
        kitob._kimda = azo
        azo.kitoblar.append(kitob)

    def qaytar(self, nom: str, azo: Azo) -> None:
        kitob = self._top(nom)
        if kitob not in azo.kitoblar:
            raise KutubxonaXatosi(f"{azo.ism}da '{nom}' yo'q")
        azo.kitoblar.remove(kitob)
        kitob._kimda = None

    def mavjud_kitoblar(self) -> list[Kitob]:
        return [k for k in self._kitoblar.values() if k.mavjud]


if __name__ == "__main__":
    print(matn_tahlili("Men dasturlash o'rganyapman"))
    hisobot("baholar.txt")
    k = Kutubxona()
    for n, m in [("O'tkan kunlar", "Qodiriy"), ("Sariq devni minib", "Xudoyberdi To'xtaboyev")]:
        k.kitob_qosh(Kitob(n, m))
    aziz, malika = Azo("Aziz"), Azo("Malika")
    k.ber("O'tkan kunlar", aziz)
    try:
        k.ber("O'tkan kunlar", malika)
    except KutubxonaXatosi as e:
        print("❌", e)
    print(*k.mavjud_kitoblar(), sep="\n")
