from datetime import datetime


class BankHisobi:
    MIN_YECHISH = 1_000

    def __init__(self, egasi: str, pin: str):
        self.egasi = egasi
        self.__pin = pin
        self.__balans = 0
        self.__tarix: list[str] = []

    # --- faqat o'qiladigan xossalar ---
    @property
    def balans(self) -> int:
        return self.__balans

    @property
    def tarix(self) -> tuple[str, ...]:
        return tuple(self.__tarix)   # nusxa — tashqaridan o'zgartirib bo'lmaydi

    # --- "rasmiy eshiklar" ---
    def qoyish(self, summa: int) -> None:
        if summa <= 0:
            raise ValueError("Summa musbat bo'lishi kerak")
        self.__balans += summa
        self.__yoz(f"+{summa}")

    def yechish(self, summa: int, pin: str) -> None:
        if pin != self.__pin:
            self.__yoz("❌ noto'g'ri PIN")
            raise PermissionError("PIN noto'g'ri")
        if summa < self.MIN_YECHISH:
            raise ValueError(f"Minimal summa {self.MIN_YECHISH}")
        if summa > self.__balans:
            raise ValueError("Mablag' yetarli emas")
        self.__balans -= summa
        self.__yoz(f"-{summa}")

    def __yoz(self, amal: str) -> None:
        self.__tarix.append(f"{datetime.now():%H:%M:%S} {amal}")


if __name__ == "__main__":
    h = BankHisobi("Aziz", "1234")
    h.qoyish(50_000)
    h.yechish(20_000, "1234")
    print(h.balans, h.tarix)
    try:
        h.balans = 999_999_999
    except AttributeError as e:
        print("Himoya ishladi:", e)
    print(h._BankHisobi__balans)  # "name mangling" — mumkin, lekin QILMANG!
