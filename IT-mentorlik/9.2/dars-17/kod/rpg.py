import random


class Qahramon:
    def __init__(self, ism: str, hp: int, kuch: int):
        self.ism = ism
        self.max_hp = hp
        self.hp = hp
        self.kuch = kuch

    @property
    def tirikmi(self) -> bool:
        return self.hp > 0

    def hujum(self, dushman: "Qahramon") -> str:
        zarar = random.randint(self.kuch - 3, self.kuch + 3)
        dushman.zarba_ol(zarar)
        return f"{self.ism} zarba berdi: -{zarar}"

    def zarba_ol(self, zarar: int) -> None:
        self.hp = max(0, self.hp - zarar)

    def __str__(self) -> str:
        bar = "█" * (self.hp * 10 // self.max_hp)
        return f"{self.__class__.__name__} {self.ism:<8} [{bar:<10}] {self.hp}/{self.max_hp}"


class Jangchi(Qahramon):
    def __init__(self, ism: str):
        super().__init__(ism, hp=130, kuch=12)
        self.qalqon = 4

    def zarba_ol(self, zarar: int) -> None:          # override: qalqon zararni kamaytiradi
        super().zarba_ol(max(0, zarar - self.qalqon))


class Sehrgar(Qahramon):
    def __init__(self, ism: str):
        super().__init__(ism, hp=90, kuch=10)
        self.mana = 30

    def hujum(self, dushman: Qahramon) -> str:        # override: mana bo'lsa — olovli shar
        if self.mana >= 10:
            self.mana -= 10
            dushman.zarba_ol(25)
            return f"{self.ism} 🔥 olovli shar: -25 (mana: {self.mana})"
        return super().hujum(dushman)


class Kamonchi(Qahramon):
    def __init__(self, ism: str):
        super().__init__(ism, hp=100, kuch=11)

    def hujum(self, dushman: Qahramon) -> str:        # override: 30% kritik zarba
        if random.random() < 0.3:
            dushman.zarba_ol(self.kuch * 2)
            return f"{self.ism} 🎯 KRITIK: -{self.kuch * 2}"
        return super().hujum(dushman)


def jang(a: Qahramon, b: Qahramon) -> Qahramon:
    print(f"\n⚔️  {a.ism} vs {b.ism}")
    raund = 1
    while a.tirikmi and b.tirikmi:
        hujumchi, himoyachi = (a, b) if raund % 2 else (b, a)
        print(f"{raund:>2}. {hujumchi.hujum(himoyachi)}")
        raund += 1
    golib = a if a.tirikmi else b
    print(f"🏆 G'olib: {golib}")
    return golib


if __name__ == "__main__":
    jang(Jangchi("Temur"), Sehrgar("Merlin"))
