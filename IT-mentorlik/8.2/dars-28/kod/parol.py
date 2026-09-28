"""Parol generatori va kuch tekshiruvchisi (8.2, 28-dars)."""
import random
import string

BELGILAR = "!@#$%^&*?"


def parol_yarat(uzunlik: int = 12, raqam: bool = True, belgi: bool = True) -> str:
    """Tasodifiy parol yaratadi."""
    alifbo = string.ascii_letters
    if raqam:
        alifbo += string.digits
    if belgi:
        alifbo += BELGILAR
    return "".join(random.choice(alifbo) for _ in range(uzunlik))


def parol_kuchi(parol: str) -> tuple[int, str]:
    """Parol kuchini 0..5 ball va tavsif bilan qaytaradi."""
    ball = sum([
        len(parol) >= 8,
        len(parol) >= 12,
        any(c.isdigit() for c in parol),
        any(c.isupper() for c in parol) and any(c.islower() for c in parol),
        any(c in BELGILAR for c in parol),
    ])
    tavsif = ["Juda kuchsiz 😱", "Kuchsiz 😟", "O'rta 😐", "Yaxshi 🙂", "Kuchli 💪", "Juda kuchli 🛡"][ball]
    return ball, tavsif


if __name__ == "__main__":
    for _ in range(3):
        p = parol_yarat(16)
        print(p, parol_kuchi(p))
    print("123456", parol_kuchi("123456"))
