# Kutilgan natija: Ali: 3 ta baho, o'rtacha 4.33
class Talaba:
    def __init__(self, ism):
        self.ism = ism
        self.baholar = []            # XATO 1: self. yo'q | runtime (AttributeError)

    def baho_qosh(self, baho):       # XATO 2: self parametri yo'q | runtime (TypeError)
        self.baholar.append(baho)

    def ortacha(self):
        return sum(self.baholar) / len(self.baholar)

t = Talaba("Ali")
for b in [5, 4, 4]:
    t.baho_qosh(b)
print(f"{t.ism}: {len(t.baholar)} ta baho, o'rtacha {t.ortacha():.2f}")
