from abc import ABC, abstractmethod
import uuid


class TolovProvayderi(ABC):
    """Barcha to'lov provayderlari uchun shartnoma."""

    nom: str = "abstrakt"
    komissiya: float = 0.0

    @abstractmethod
    def _api_sorov(self, summa: int) -> bool:
        """Provayderning haqiqiy API'siga so'rov (har biri o'zicha)."""

    def tolov(self, summa: int) -> str:
        """Umumiy mantiq — barcha provayderlar uchun bir xil (Template Method)."""
        if summa <= 0:
            raise ValueError("Summa musbat bo'lishi kerak")
        jami = round(summa * (1 + self.komissiya))
        if not self._api_sorov(jami):
            raise RuntimeError(f"{self.nom}: to'lov rad etildi")
        tid = f"{self.nom[:3].upper()}-{uuid.uuid4().hex[:8]}"
        print(f"✅ {self.nom}: {jami:,} so'm to'landi (komissiya {self.komissiya:.0%}). ID: {tid}")
        return tid


class Click(TolovProvayderi):
    nom, komissiya = "Click", 0.01

    def _api_sorov(self, summa: int) -> bool:
        print(f"   → Click API: POST /v2/merchant/invoice amount={summa}")
        return True


class Payme(TolovProvayderi):
    nom, komissiya = "Payme", 0.015

    def _api_sorov(self, summa: int) -> bool:
        print(f"   → Payme JSON-RPC: receipts.create amount={summa * 100} (tiyinda)")
        return True


class Naqd(TolovProvayderi):
    nom = "Naqd"

    def _api_sorov(self, summa: int) -> bool:
        return True


class Dokon:
    def __init__(self, provayder: TolovProvayderi):
        self.provayder = provayder   # do'kon qaysi provayder ekanini bilmaydi — faqat shartnomani

    def buyurtma(self, summa: int) -> str:
        return self.provayder.tolov(summa)


if __name__ == "__main__":
    for p in (Click(), Payme(), Naqd()):
        Dokon(p).buyurtma(150_000)
    try:
        TolovProvayderi()
    except TypeError as e:
        print("❌", e)
