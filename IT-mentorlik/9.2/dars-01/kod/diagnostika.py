# 2-vazifa
ism = input("Ismingiz: ")
yil = int(input("Tug'ilgan yilingiz: "))
print(f"Salom, {ism}! Siz 2026-yilda {2026 - yil} yoshga to'lasiz.")

# 3-vazifa: FizzBuzz
for i in range(1, 31):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
