class Pul:
    def __init__(self, summa: int):
        if summa < 0:
            raise ValueError("Pul manfiy bo'lmaydi")
        self.summa = int(summa)

    @classmethod
    def from_dollar(cls, dollar: float, kurs: int = 12800) -> "Pul":
        return cls(round(dollar * kurs))

    def __add__(self, other: "Pul") -> "Pul":
        return Pul(self.summa + other.summa)

    def __sub__(self, other: "Pul") -> "Pul":
        if other.summa > self.summa:
            raise ValueError("Mablag' yetarli emas")
        return Pul(self.summa - other.summa)

    def __mul__(self, k: int) -> "Pul":
        return Pul(self.summa * k)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Pul) and self.summa == other.summa

    def __lt__(self, other: "Pul") -> bool:
        return self.summa < other.summa

    def __gt__(self, other: "Pul") -> bool:
        return self.summa > other.summa

    def __str__(self) -> str:
        return f"{self.summa:,} so'm".replace(",", " ")

    def __repr__(self) -> str:
        return f"Pul({self.summa})"

    def taqsimla(self, n: int) -> list["Pul"]:
        asosiy, qoldiq = divmod(self.summa, n)
        return [Pul(asosiy + (1 if i < qoldiq else 0)) for i in range(n)]


if __name__ == "__main__":
    a, b = Pul(15000), Pul(5500)
    print(a + b, a - b, a * 3, a > b, a == Pul(15000))
    print(sum([a, b, Pul(1000)], Pul(0)))
    print(Pul.from_dollar(10), Pul(100000).taqsimla(3))
