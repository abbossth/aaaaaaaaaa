# 2. Palindrom
soz = input("So'z: ").lower()
print("Palindrom" if soz == soz[::-1] else "Palindrom emas")

# 5. Email validator
email = input("Email: ").strip().lower()
if email.count("@") == 1 and " " not in email and "." in email.split("@")[1]:
    print(f"To'g'ri: {email}")
else:
    print("Noto'g'ri email")

# 6. Slug
sarlavha = input("Sarlavha: ").lower()
slug = ""
for c in sarlavha:
    if c.isascii() and c.isalnum():
        slug += c
    elif c in " -_":
        slug += "-"
while "--" in slug:
    slug = slug.replace("--", "-")
print(slug.strip("-"))

# 7. Sezar shifri
matn = input("Matn: ")
k = int(input("Siljish: "))
natija = ""
for c in matn:
    if "a" <= c <= "z":
        natija += chr((ord(c) - ord("a") + k) % 26 + ord("a"))
    elif "A" <= c <= "Z":
        natija += chr((ord(c) - ord("A") + k) % 26 + ord("A"))
    else:
        natija += c
print(natija)
# Deshifrlash: xuddi shu kod, faqat k o'rniga -k
