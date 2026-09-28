class BankHisobi:
    """Oddiy bank hisobi (8.2, 30-dars)."""

    def __init__(self, egasi: str, balans: int = 0):
        self.egasi = egasi
        self.balans = balans
        self.tarix: list[str] = []

    def qoyish(self, summa: int) -> None:
        if summa <= 0:
            print("❌ Summa musbat bo'lishi kerak")
            return
        self.balans += summa
        self.tarix.append(f"+{summa:,}")

    def yechish(self, summa: int) -> None:
        if summa > self.balans:
            print(f"❌ Mablag' yetarli emas (balans: {self.balans:,})")
            return
        self.balans -= summa
        self.tarix.append(f"-{summa:,}")

    def otkazma(self, boshqa: "BankHisobi", summa: int) -> None:
        if summa > self.balans:
            print("❌ O'tkazma uchun mablag' yetarli emas")
            return
        self.yechish(summa)
        boshqa.qoyish(summa)
        print(f"✅ {self.egasi} → {boshqa.egasi}: {summa:,} so'm")

    def __str__(self) -> str:
        return f"💳 {self.egasi}: {self.balans:,} so'm"


if __name__ == "__main__":
    aziz = BankHisobi("Aziz", 100_000)
    malika = BankHisobi("Malika")
    aziz.otkazma(malika, 30_000)
    malika.yechish(50_000)
    print(aziz, malika, sep="\n")
    print("Aziz tarixi:", aziz.tarix)
