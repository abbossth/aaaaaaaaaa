"""Loyiha: [nomi] — asosiy menyu (tech lead)."""
from storage import yuklash, saqlash
import logic


def menyu() -> str:
    print("\n=== [LOYIHA NOMI] ===")
    print("1. ...  2. ...  3. ...  0. Chiqish")
    return input("> ").strip()


def main() -> None:
    data = yuklash()
    while True:
        match menyu():
            case "1":
                logic.qoshish(data)
                saqlash(data)
            case "2":
                logic.korsatish(data)
            case "0":
                print("Xayr! 👋")
                break
            case _:
                print("Noma'lum buyruq")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nXayr! 👋")
