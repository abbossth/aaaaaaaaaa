import random
from pokemon import Pokemon, Olov, Suv, Elektr, jang

# O'quvchilarning klasslarini shu yerga qo'shing
ishtirokchilar = [
    Olov("Charmander", 100, 12), Suv("Squirtle", 110, 10),
    Elektr("Pikachu", 90, 14), Olov("Vulpix", 95, 13),
    Suv("Psyduck", 120, 9), Elektr("Jolteon", 85, 15),
    Pokemon("Eevee", 115, 11), Pokemon("Snorlax", 140, 6),
]

for p in ishtirokchilar:
    assert p.hp + p.kuch * 5 <= 170, f"{p.ism} balans qoidasini buzdi!"

random.shuffle(ishtirokchilar)
bosqich = 1
while len(ishtirokchilar) > 1:
    print(f"\n===== {bosqich}-BOSQICH =====")
    keyingi = []
    for i in range(0, len(ishtirokchilar), 2):
        a, b = ishtirokchilar[i], ishtirokchilar[i + 1]
        golib = jang(a, b)
        golib._hp = golib._max_hp  # keyingi bosqichga to'liq HP bilan
        keyingi.append(golib)
    ishtirokchilar = keyingi
    bosqich += 1
print(f"\n👑 TURNIR CHEMPIONI: {ishtirokchilar[0].ism}!")
