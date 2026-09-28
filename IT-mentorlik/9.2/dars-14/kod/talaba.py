class Talaba:
    maktab = "42-maktab"   # class atributi
    soni = 0               # nechta talaba yaratilgani

    def __init__(self, ism: str, sinf: str, yosh: int):
        self.ism = ism
        self.sinf = sinf
        self.yosh = yosh
        self.baholar: list[int] = []
        Talaba.soni += 1

    def baho_qosh(self, baho: int) -> None:
        if 2 <= baho <= 5:
            self.baholar.append(baho)

    def ortacha(self) -> float:
        return sum(self.baholar) / len(self.baholar) if self.baholar else 0.0

    def tanishtir(self) -> str:
        return f"Men {self.ism}, {self.sinf} sinf, {self.yosh} yosh. O'rtacha: {self.ortacha():.2f}"


aziz = Talaba("Aziz", "9.2", 15)
malika = Talaba("Malika", "9.3", 14)

for b in (5, 4, 5):
    aziz.baho_qosh(b)
malika.baho_qosh(5)

print(aziz.tanishtir())
print(malika.tanishtir())
print("Jami talabalar:", Talaba.soni)
print("Maktab:", aziz.maktab, malika.maktab)
print(aziz.__dict__)
