# Oraliq nazorat #1 — amaliy qism (60 ball, 50 daqiqa)

`kod/refaktor-nazorat/` loyihasini oling (mentor zip yoki GitHub template orqali beradi).

## Vazifa
`src/booking.js` — kinoteatr chiptalarini bron qilish funksiyasi. U **ishlaydi**, lekin kod juda yomon.

### 1. Git (15 ball)
- `refactor/booking` branch yarating
- Kamida **3 ta** mantiqiy (atomic) commit, Conventional Commits formatida
- Oxirida o'z reposingizga push qilib, **PR** oching. Tavsifida: Nima? Nega? Qanday tekshirildi?

### 2. Refaktoring (25 ball)
- Aniq nomlar, kichik funksiyalar, sehrli sonlar → konstantalar
- Guard clause'lar (chuqur ichma-ichlik yo'q)
- Narx qoidalari (OCP): yangi chipta turi qo'shish uchun `if` qo'shish shart bo'lmasin (obyekt/strategiya)
- **Xatti-harakat o'zgarmasligi kerak!**

### 3. Unit testlar (20 ball)
- `tests/booking.test.js` da kamida **6 ta** test (Vitest): oddiy holatlar, chegaraviy holatlar, xato holatlari
- **Maslahat:** refaktoringdan **oldin** testlarni yozing: ular refaktoring xatti-harakatni buzmaganini isbotlaydi!

## Baholash mezonlari
| Mezon | Ball |
|---|---|
| Branch + 3 atomic commit + Conventional Commits | 8 |
| PR tavsifi sifatli | 7 |
| Nomlar va kichik funksiyalar | 10 |
| Guard clause, konstantalar | 7 |
| OCP (narx strategiyalari) | 8 |
| Testlar soni va sifati (chegaraviy holatlar) | 15 |
| Testlar yashil va xatti-harakat saqlangan | 5 |
