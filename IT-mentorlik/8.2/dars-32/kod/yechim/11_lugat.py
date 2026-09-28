# Kutilgan natija: olma: 3 ta, anor: 2 ta, nok: 1 ta
mevalar = ["olma", "anor", "olma", "nok", "anor", "olma"]
sanoq = {}
for m in mevalar:
    sanoq[m] = sanoq.get(m, 0) + 1          # XATO 1: KeyError (kalit hali yo'q) | runtime
for meva, soni in sanoq.items():            # XATO 2: .items() yo'q | runtime (ValueError)
    print(f"{meva}: {soni} ta", end=", ")
