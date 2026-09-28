# Kutilgan natija:
# Barsik: Miyov!
# Rex: Vov! (zoti: ovcharka)
class Hayvon:
    def __init__(self, ism):
        self.ism = ism

    def gapir(self):
        return f"{self.ism}: ..."

class Mushuk(Hayvon):
    def gapir(self):
        return f"{self.ism}: Miyov!"

class It(Hayvon):
    def __init__(self, ism, zot):
        self.zot = zot

    def gapir(self):
        return f"{self.ism}: Vov! (zoti: {self.zot})"

for h in [Mushuk("Barsik"), It("ovcharka", "Rex")]:
    print(h.gapir())
