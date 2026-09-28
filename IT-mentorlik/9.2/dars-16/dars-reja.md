# 16-dars. Inkapsulyatsiya: private/protected, getter/setter, @property

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 2-bob, "Inkapsulyatsiya"

## Maqsad
- Inkapsulyatsiya mohiyatini tushunadi: obyekt ichki holatini himoya qilish va unga faqat "rasmiy eshiklar" (metodlar) orqali kirish.
- Python'dagi kelishuvlarni biladi: `public`, `_protected`, `__private` (name mangling).
- `@property` va `@x.setter` bilan validatsiyali getter/setter yozadi.
- Faqat o'qiladigan (read-only) xossalar yaratadi.
- Nima uchun `hisob.balans = -1000000` imkonsiz bo'lishi kerakligini tushunadi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | 14-darsdagi `BankHisobi`: `aziz.balans = 999999999` 😈. *"Bitta qator bilan millioner bo'ldim! Real bankda bu mumkinmi? Nega yo'q?"* |
| 5–10 | **Takrorlash** | 15-dars testi |
| 10–28 | **Yangi mavzu** | Bankomat analogiyasi (pul seyfda, faqat PIN va tugmalar orqali). `_` va `__`. `@property`. Validatsiyali setter. Read-only property |
| 28–55 | **Amaliyot** | `amaliy-topshiriq.md` |
| 55–72 | **Challenge** | `challenge.md`: "Xaker vs Himoyachi" |
| 72–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge: himoyachi +20, har bir muvaffaqiyatli "hujum" +5
