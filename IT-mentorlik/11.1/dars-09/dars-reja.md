# 9-dars. Clean Code: nomlash, kichik funksiyalar, code smells, DRY/KISS/YAGNI

**Guruh:** 11.1 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** I bob, "Clean Code va SOLID tamoyillari"

## Maqsad
- Toza kod tamoyillarini biladi: aniq nomlar, kichik funksiyalar (bitta vazifa), izohlar o'rniga o'zini tushuntiruvchi kod, "sehrli sonlar" yo'qligi.
- DRY, KISS, YAGNI tamoyillarini misollar bilan tushuntiradi.
- Code smell'larni taniydi: uzun funksiya, takrorlanish, chuqur ichma-ichlik, ko'p parametr, noaniq nomlar.
- Refaktoring usullarini qo'llaydi: funksiya ajratish, nomni o'zgartirish, guard clause, konstanta chiqarish.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Ekranda `kod/iflos.js`: 40 qatorlik "spagetti" funksiya. *"Bu kod ishlaydi. Lekin 5 daqiqada uning nima qilishini tushuna oladiganlar qo'l ko'tarsin."* Keyin xuddi shu mantiqning toza versiyasi (`kod/toza.js`). *"Kod bir marta yoziladi, lekin 10 marta o'qiladi."* |
| 5–10 | **Takrorlash** | 8-dars testi |
| 10–28 | **Yangi mavzu** | Nomlash qoidalari. Funksiyalar: kichik, bitta vazifa, ≤ 3 parametr. Guard clause. Sehrli sonlar. Izohlar: "nima" emas, "nega". DRY/KISS/YAGNI. Code smells katalogi |
| 28–58 | **Amaliyot** | `amaliy-topshiriq.md`: refaktoring |
| 58–74 | **Challenge** | `challenge.md`: "Code Smell bingo" |
| 74–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Refaktoring +5/+10/+20 · Bingo +20/+10/+5
