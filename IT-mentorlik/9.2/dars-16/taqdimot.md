# 16-dars slaydlari: Inkapsulyatsiya 🔒

## 1-slayd
`aziz.balans = 999999999` 😈 → **Qanday himoya qilamiz?**

## 2-slayd — Bankomat analogiyasi 🏧
Pul seyfda (yashirin). Siz faqat **tugmalar** orqali ishlaysiz: PIN, yechish, balans.
Seyfni to'g'ridan-to'g'ri ochib bo'lmaydi.

## 3-slayd — Python kelishuvlari
| Yozilishi | Ma'nosi |
|---|---|
| `balans` | Public — hamma uchun |
| `_balans` | Protected — "ichki, tegmang" (kelishuv) |
| `__balans` | Private — nomi o'zgartiriladi (`_BankHisobi__balans`) |
Python'da "haqiqiy" private yo'q: *"We are all consenting adults here"*

## 4-slayd — @property
```python
class BankHisobi:
    def __init__(self, egasi):
        self.egasi = egasi
        self.__balans = 0

    @property
    def balans(self):          # getter — faqat o'qish
        return self.__balans

hisob.balans          # ✅ 0
hisob.balans = 100    # 💥 AttributeError
```

## 5-slayd — Validatsiyali setter
```python
class Talaba:
    @property
    def yosh(self):
        return self._yosh

    @yosh.setter
    def yosh(self, qiymat):
        if not 6 <= qiymat <= 20:
            raise ValueError("Yosh 6..20 oralig'ida bo'lishi kerak")
        self._yosh = qiymat
```

## 6-slayd — Nima uchun?
✅ Noto'g'ri holatning oldini olish · ✅ Ichki tuzilmani keyin o'zgartirish erkinligi
✅ Xavfsizlik va audit (kim, qachon o'zgartirdi)
