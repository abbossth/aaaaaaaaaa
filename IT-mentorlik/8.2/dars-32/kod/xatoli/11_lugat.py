# Kutilgan natija: olma: 3 ta, anor: 2 ta, nok: 1 ta
mevalar = ["olma", "anor", "olma", "nok", "anor", "olma"]
sanoq = {}
for m in mevalar:
    sanoq[m] += 1
for meva, soni in sanoq:
    print(f"{meva}: {soni} ta", end=", ")
