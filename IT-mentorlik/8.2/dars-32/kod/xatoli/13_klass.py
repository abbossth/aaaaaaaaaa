# Kutilgan natija: Ali: 3 ta baho, o'rtacha 4.33
class Talaba:
    def __init__(self, ism):
        self.ism = ism
        baholar = []

    def baho_qosh(baho):
        self.baholar.append(baho)

    def ortacha(self):
        return sum(self.baholar) / len(self.baholar)

t = Talaba("Ali")
for b in [5, 4, 4]:
    t.baho_qosh(b)
print(f"{t.ism}: {len(t.baholar)} ta baho, o'rtacha {t.ortacha():.2f}")
