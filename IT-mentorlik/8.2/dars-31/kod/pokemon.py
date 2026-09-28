import random


class Pokemon:
    tur = "⚪"

    def __init__(self, ism, hp, kuch):
        self.ism = ism
        self._hp = hp
        self._max_hp = hp
        self.kuch = kuch

    @property
    def hp(self):
        return self._hp

    @property
    def tirikmi(self):
        return self._hp > 0

    def zarar_ol(self, miqdor):
        self._hp = max(0, self._hp - int(miqdor))

    def hujum(self, raqib):
        raqib.zarar_ol(self.kuch)
        return f"{self.ism} oddiy hujum qildi!"

    def __str__(self):
        return f"{self.ism} {self.tur} [HP: {self._hp}]"


class Olov(Pokemon):
    tur = "🔥"

    def hujum(self, raqib):
        raqib.zarar_ol(self.kuch * 1.5)
        return f"{self.ism} olov purkadi! 🔥"


class Suv(Pokemon):
    tur = "💧"

    def hujum(self, raqib):
        raqib.zarar_ol(self.kuch * 1.2)
        return f"{self.ism} suv to'lqini yubordi! 💧"


class Elektr(Pokemon):
    tur = "⚡"

    def hujum(self, raqib):
        if random.random() < 0.3:
            raqib.zarar_ol(self.kuch * 2)
            return f"{self.ism} CHAQMOQ urdi! ⚡⚡ (kritik)"
        raqib.zarar_ol(self.kuch)
        return f"{self.ism} tok urdi! ⚡"


def jang(a, b):
    print(f"\n⚔️  {a} VS {b}")
    navbat = [a, b]
    raund = 1
    while a.tirikmi and b.tirikmi:
        hujumchi, himoyachi = navbat[0], navbat[1]
        print(f"{raund}-raund: {hujumchi.hujum(himoyachi)} → {himoyachi}")
        navbat.reverse()
        raund += 1
    golib = a if a.tirikmi else b
    print(f"🏆 G'olib: {golib.ism}!")
    return golib


if __name__ == "__main__":
    jang(Olov("Charmander", 100, 12), Elektr("Pikachu", 90, 14))
