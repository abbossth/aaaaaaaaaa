m1 = input("1-mahsulot: "); n1 = int(input("Narxi: ")); s1 = int(input("Soni: "))
m2 = input("2-mahsulot: "); n2 = int(input("Narxi: ")); s2 = int(input("Soni: "))
m3 = input("3-mahsulot: "); n3 = int(input("Narxi: ")); s3 = int(input("Soni: "))

j1, j2, j3 = n1 * s1, n2 * s2, n3 * s3
jami = j1 + j2 + j3
qqs = jami * 0.12

chiziq = "=" * 30
print(chiziq)
print(f"{'IT MARKET DOKONI':^30}")
print(chiziq)
print(f"{'Mahsulot':<15}{'Soni':>5}{'Summa':>10}")
print("-" * 30)
print(f"{m1:<15}{s1:>5}{j1:>10,}")
print(f"{m2:<15}{s2:>5}{j2:>10,}")
print(f"{m3:<15}{s3:>5}{j3:>10,}")
print("-" * 30)
print(f"{'JAMI:':<20}{jami:>10,}")
print(f"{'QQS (12%):':<20}{qqs:>10,.0f}")
print(chiziq)
print(f"{'Xaridingiz uchun rahmat!':^30}")
print(chiziq)
