# 4. Takrorlarni o'chirish (tartib saqlanadi)
royxat = [1, 2, 2, 3, 1, 4]
natija = []
for x in royxat:
    if x not in natija:
        natija.append(x)
print(natija)

# 5. Ikkinchi eng katta
sonlar = [5, 3, 8, 1, 9, 2]
birinchi = ikkinchi = float("-inf")
for n in sonlar:
    if n > birinchi:
        birinchi, ikkinchi = n, birinchi
    elif birinchi > n > ikkinchi:
        ikkinchi = n
print(ikkinchi)

# 6. Matritsa
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Qatorlar:", [sum(q) for q in m])
print("Ustunlar:", [sum(q[j] for q in m) for j in range(3)])
print("Diagonal:", sum(m[i][i] for i in range(3)))
print("Transpon:", [[m[i][j] for i in range(3)] for j in range(3)])

# 7. Top-N
oquvchilar = [("Aziz", 87), ("Malika", 95), ("Bobur", 72), ("Dilnoza", 91), ("Sardor", 68)]
medallar = ["🥇", "🥈", "🥉"]
for medal, (ism, ball) in zip(medallar, sorted(oquvchilar, key=lambda x: x[1], reverse=True)):
    print(f"{medal} {ism}: {ball}")
