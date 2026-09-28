# 10-dars amaliy topshiriq: "Kontaktlar kitobi" v2 📒

## 🟢 Oson (+5 XP): Funksiyalar mashqi
1. `is_even(n)`, `faktorial(n)`, `is_prime(n)`, `teskari(s)` funksiyalarini yozing (docstring bilan).
2. `bmi(vazn, boy)` — BMI va toifani (`"Ozg'in"`, `"Normal"`, `"Ortiqcha"`) qaytarsin (2 ta qiymat).

## 🟡 O'rta (+10 XP): Refaktoring
9-darsdagi `kontaktlar_v1.py` ni funksiyalarga bo'ling:
```python
def tel_tozalash(tel: str) -> str | None: ...
def kontakt_qoshish(kontaktlar: dict) -> None: ...
def hammasini_korsat(kontaktlar: dict) -> None: ...
def qidirish(kontaktlar: dict, soz: str) -> dict: ...
def ochirish(kontaktlar: dict, ism: str) -> bool: ...
def menyu() -> str: ...
def main() -> None: ...

if __name__ == "__main__":
    main()
```
Har bir funksiya **bitta** ishni qilsin. `main()` faqat menyu va chaqiruvlardan iborat bo'lsin.

## 🔴 Qiyin (+20 XP)
- Saralash: ism bo'yicha yoki qo'shilgan vaqt bo'yicha (`lambda`).
- `qidirish` funksiyasi `**filtrlar` qabul qilsin: `qidirish(kontaktlar, guruh="do'st", email_bor=True)`.
- Funksiyalarni alohida modulga chiqaring: `kontakt_utils.py` → `from kontakt_utils import tel_tozalash`.

Namuna: `kod/kontaktlar_v2.py`
