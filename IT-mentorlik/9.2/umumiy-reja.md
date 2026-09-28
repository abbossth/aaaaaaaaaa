# 9.2 — Advanced Back-end va DevOps: umumiy reja

**Guruh:** 9.2 (HTML, CSS, JS, Bootstrap, Git/GitHub, terminal va Python o'tilgan, lekin chuqur o'zlashtirilmagan)
**Yo'nalish:** Advanced Back-end va DevOps (Python back-end), 9-sinf standarti asosida
**Hajm:** 70 dars × 80 daqiqa, haftasiga 3 marta, 30-sentabrdan
**Asosiy manba:** "Advanced Back-end va DevOps" o'quv qo'llanmasi va uslubiy ko'rsatmasi (RTRM, 2026)

## Guruhga xos yondashuv
- Python bir marta o'tilgan, lekin yuzaki. Shuning uchun Python asoslari **"tezkor + chuqur"** usulida o'tiladi: har bir mavzuda qisqa takrorlash va darhol real mini-dastur yasaladi.
- Rasmiy dasturdagi 5 bob to'liq qamrab olingan: Python → OOP + Telegram bot + Linux → PostgreSQL → FastAPI → DevOps.
- Rasmiy dasturning 102 darsi 70 darsga siqilgan. Bo'shagan joylarga **AI, challenge va startap** darslari qo'shilgan.
- **9.3 guruhi xuddi shu rejadan o'tadi.** Ikkala guruh o'rtasida **guruhlararo liga** (hakatonlar va Demo Day) o'tkaziladi.
- **Yil davomidagi yakuniy loyiha:** jamoaviy **back-end startap**: FastAPI + PostgreSQL + Telegram bot, Docker'da, CI/CD bilan serverda ishlaydi.

## Yil davomida o'quvchi yaratadigan loyihalar portfeli
1. CLI ilova: "Kontaktlar kitobi" (Python, fayllar, JSON)
2. OOP o'yin / tizim modeli
3. Aiogram Telegram bot + PostgreSQL
4. FastAPI REST API: JWT autentifikatsiya, Swagger
5. Docker Compose + Nginx + GitHub Actions bilan deploy qilingan startap

## Dars turlari bo'yicha taqsimot

| 📘 Mavzu | 🤖 AI | 🏆 Challenge | 🚀 Loyiha | 🎤 Nazorat/Demo | Jami |
|---|---|---|---|---|---|
| 46 | 5 | 6 | 7 | 6 | 70 |

## 70 darslik reja

> Hafta ustunidagi sana — o'sha haftaning boshlanish sanasi (30-sentabrdan hisoblangan, 3 dars = 1 hafta). **Ta'tillar hisobga olinmagan** — kuzgi va qishki ta'til haftalarini o'tkazib yuboring, raqamlar o'zgarmaydi.

### I bob. Python asoslari (tezkor + chuqur)

| № | Hafta | Mavzu | Tur | O'quvchi natijasi |
|---|---|---|---|---|
| [1](dars-01/dars-reja.md) | 1 (30.09) | Tanishuv, diagnostika, Back-end/DevOps kasblari va maoshlar, yo'l xaritasi, XP liga | 📘 Mavzu | Diagnostika, XP profil, GitHub akkaunt |
| [2](dars-02/dars-reja.md) | 1 (30.09) | Dasturlash tillari, kompilyator/interpretator. Python o'rnatish, VS Code, venv, pip | 📘 Mavzu | Sozlangan ish muhiti |
| [3](dars-03/dars-reja.md) | 1 (30.09) | O'zgaruvchilar, ma'lumot turlari, input, f-string | 📘 Mavzu | "Shaxsiy kartochka" dasturi |
| [4](dars-04/dars-reja.md) | 2 (07.10) | Operatorlar, if/elif/else, ichma-ich shartlar | 📘 Mavzu | "Taksi narxi kalkulyatori" |
| [5](dars-05/dars-reja.md) | 2 (07.10) | Sikllar: for, while, range, break/continue; match/case | 📘 Mavzu | "Son topish" o'yini + menyu |
| [6](dars-06/dars-reja.md) | 2 (07.10) | Python Bug Hunt #1 + Codewars reytingi | 🏆 Challenge | Tuzatilgan dasturlar, Codewars profili |
| [7](dars-07/dars-reja.md) | 3 (14.10) | Satrlar (string) va ularning metodlari | 📘 Mavzu | Parol kuchini tekshiruvchi dastur |
| [8](dars-08/dars-reja.md) | 3 (14.10) | List va tuple | 📘 Mavzu | "Xarid savati" dasturi |
| [9](dars-09/dars-reja.md) | 3 (14.10) | Set va dictionary | 📘 Mavzu | "Kontaktlar kitobi" v1 |
| [10](dars-10/dars-reja.md) | 4 (21.10) | DRY prinsipi, funksiyalar, *args/**kwargs, lambda | 📘 Mavzu | "Kontaktlar kitobi" v2 (funksiyalar) |
| [11](dars-11/dars-reja.md) | 4 (21.10) | try/except/finally, raise, fayllar (with open), JSON | 📘 Mavzu | "Kontaktlar kitobi" v3 (faylga saqlaydi) |
| [12](dars-12/dars-reja.md) | 4 (21.10) | AI pair programming: AI bilan kod yozish, AI'dan code review olish | 🤖 AI | AI tekshirgan va yaxshilangan CLI ilova |
| [13](dars-13/dars-reja.md) | 5 (28.10) | Mini loyiha: jamoaviy CLI ilova (o'yin, test tizimi, kutubxona) | 🚀 Loyiha | GitHub'dagi jamoaviy CLI ilova |

### II bob. OOP, Telegram bot, Linux

| № | Hafta | Mavzu | Tur | O'quvchi natijasi |
|---|---|---|---|---|
| [14](dars-14/dars-reja.md) | 5 (28.10) | OOP'ga kirish: klass, obyekt, __init__, atributlar | 📘 Mavzu | "Talaba" va "Guruh" klasslari |
| [15](dars-15/dars-reja.md) | 5 (28.10) | Metodlar: instance, class, static, maxsus (__str__, __len__, __add__) | 📘 Mavzu | "Vektor" / "Pul" klassi |
| [16](dars-16/dars-reja.md) | 6 (04.11) | Inkapsulyatsiya: private/protected, getter/setter, @property | 📘 Mavzu | "Bank hisobi" klassi |
| [17](dars-17/dars-reja.md) | 6 (04.11) | Merosxo'rlik, super(), polimorfizm | 📘 Mavzu | "RPG qahramonlar" o'yini |
| [18](dars-18/dars-reja.md) | 6 (04.11) | Abstraksiya: abc moduli, abstrakt klasslar | 📘 Mavzu | "To'lov tizimi" modeli |
| [19](dars-19/dars-reja.md) | 7 (11.11) | Oraliq nazorat #1 (Python + OOP) | 🎤 Nazorat/Demo | Nazorat natijasi |
| [20](dars-20/dars-reja.md) | 7 (11.11) | Aiogram 3: BotFather, echo bot, /start, /help | 📘 Mavzu | Birinchi bot |
| [21](dars-21/dars-reja.md) | 7 (11.11) | Reply/inline keyboard, callback query | 📘 Mavzu | Menyuli bot |
| [22](dars-22/dars-reja.md) | 8 (18.11) | FSM: holatlar, anketa ssenariysi | 📘 Mavzu | Ro'yxatdan o'tish boti |
| [23](dars-23/dars-reja.md) | 8 (18.11) | Bot + tashqi API, fayl/JSON saqlash | 📘 Mavzu | Ob-havo/valyuta boti |
| [24](dars-24/dars-reja.md) | 8 (18.11) | AI bot: botga LLM ulash (Gemini API) | 🤖 AI | "Aqlli yordamchi" bot |
| [25](dars-25/dars-reja.md) | 9 (25.11) | Bot hakaton: 9.2 vs 9.3 (80 daqiqada foydali bot) | 🏆 Challenge | Hakaton boti |
| [26](dars-26/dars-reja.md) | 9 (25.11) | Linux 1: fayl tizimi, asosiy buyruqlar, fayl ruxsatlari, foydalanuvchilar | 📘 Mavzu | Terminalda ishlash ko'nikmasi |
| [27](dars-27/dars-reja.md) | 9 (25.11) | Linux 2: jarayonlar, paketlar, bash script + "Terminal Quest" (OverTheWire Bandit) | 🏆 Challenge | Bash skript, Bandit darajalari |

### III bob. PostgreSQL

| № | Hafta | Mavzu | Tur | O'quvchi natijasi |
|---|---|---|---|---|
| [28](dars-28/dars-reja.md) | 10 (02.12) | Ma'lumotlar bazasi turlari, MBBT, SQL, loyihalash, normalizatsiya | 📘 Mavzu | Maktab bazasining ER-sxemasi |
| [29](dars-29/dars-reja.md) | 10 (02.12) | PostgreSQL o'rnatish, psql, pgAdmin, CREATE DATABASE/TABLE, data types | 📘 Mavzu | Birinchi baza |
| [30](dars-30/dars-reja.md) | 10 (02.12) | CRUD: INSERT, SELECT, UPDATE, DELETE | 📘 Mavzu | To'ldirilgan jadvallar |
| [31](dars-31/dars-reja.md) | 11 (09.12) | Constraints (PK, FK, UNIQUE, CHECK, NOT NULL), ALTER TABLE | 📘 Mavzu | Himoyalangan jadvallar |
| [32](dars-32/dars-reja.md) | 11 (09.12) | Filtrlash (WHERE, LIKE, IN, BETWEEN), agregat funksiyalar, GROUP BY/HAVING | 📘 Mavzu | Hisobot so'rovlari |
| [33](dars-33/dars-reja.md) | 11 (09.12) | JOIN: INNER, LEFT, RIGHT | 📘 Mavzu | Bog'langan so'rovlar |
| [34](dars-34/dars-reja.md) | 12 (16.12) | SQL Murder Mystery: SQL bilan jinoyatni ochish | 🏆 Challenge | Ochilgan "jinoyat" |
| [35](dars-35/dars-reja.md) | 12 (16.12) | AI + SQL: text-to-SQL, AI yozgan so'rovni tekshirish va optimallashtirish | 🤖 AI | AI va qo'lda yozilgan so'rovlar taqqoslamasi |
| [36](dars-36/dars-reja.md) | 12 (16.12) | Mini loyiha: Telegram bot + PostgreSQL (asyncpg) | 🚀 Loyiha | Bazali bot |
| [37](dars-37/dars-reja.md) | 13 (23.12) | Oraliq nazorat #2 (SQL) | 🎤 Nazorat/Demo | Nazorat natijasi |

### IV bob. FastAPI va asinxron dasturlash

| № | Hafta | Mavzu | Tur | O'quvchi natijasi |
|---|---|---|---|---|
| [38](dars-38/dars-reja.md) | 13 (23.12) | Asinxron dasturlash: async/await, event loop, asyncio | 📘 Mavzu | Asinxron yuklab oluvchi |
| [39](dars-39/dars-reja.md) | 13 (23.12) | FastAPI'ga kirish: routing, path va query parametrlar | 📘 Mavzu | Birinchi API |
| [40](dars-40/dars-reja.md) | 14 (30.12) | Pydantic modellar, validatsiya, Field, Enum | 📘 Mavzu | Validatsiyali API |
| [41](dars-41/dars-reja.md) | 14 (30.12) | Request/Response, status kodlar, xatolarni boshqarish | 📘 Mavzu | To'g'ri javob beruvchi API |
| [42](dars-42/dars-reja.md) | 14 (30.12) | SQLAlchemy ORM: modellar, sessiya | 📘 Mavzu | Bazaga ulangan API |
| [43](dars-43/dars-reja.md) | 15 (06.01) | SQLAlchemy bilan CRUD | 📘 Mavzu | CRUD API |
| [44](dars-44/dars-reja.md) | 15 (06.01) | Alembic: migratsiyalar, upgrade/downgrade | 📘 Mavzu | Migratsiyali loyiha |
| [45](dars-45/dars-reja.md) | 15 (06.01) | Fayllar bilan ishlash: upload/download, static | 📘 Mavzu | Rasm yuklaydigan API |
| [46](dars-46/dars-reja.md) | 16 (13.01) | Autentifikatsiya: parol hash, JWT token | 📘 Mavzu | Login/register API |
| [47](dars-47/dars-reja.md) | 16 (13.01) | OAuth2, himoyalangan endpointlar, Swagger UI va Redoc | 📘 Mavzu | Hujjatlashtirilgan, himoyalangan API |
| [48](dars-48/dars-reja.md) | 16 (13.01) | AI bilan API: AI yordamida endpoint va pytest testlari yozish | 🤖 AI | Testlar bilan qoplangan API |
| [49](dars-49/dars-reja.md) | 17 (20.01) | API hakaton: 9.2 vs 9.3 | 🏆 Challenge | Hakaton API'si |
| [50](dars-50/dars-reja.md) | 17 (20.01) | Startap haftasi: muammo, g'oya, Lean Canvas, jamoa rollari | 🚀 Loyiha | Lean Canvas, backlog |
| [51](dars-51/dars-reja.md) | 17 (20.01) | Startap MVP 1-sprint: FastAPI backend | 🚀 Loyiha | MVP API |
| [52](dars-52/dars-reja.md) | 18 (27.01) | Oraliq nazorat #3 (FastAPI) | 🎤 Nazorat/Demo | Nazorat natijasi |

### V bob. DevOps

| № | Hafta | Mavzu | Tur | O'quvchi natijasi |
|---|---|---|---|---|
| [53](dars-53/dars-reja.md) | 18 (27.01) | DevOps tushunchasi, CI/CD. Git chuqur: branch, merge, conflict | 📘 Mavzu | Branch strategiyasi bilan repo |
| [54](dars-54/dars-reja.md) | 18 (27.01) | GitHub jamoaviy: issues, pull request, code review, .gitignore | 📘 Mavzu | Birinchi PR va review |
| [55](dars-55/dars-reja.md) | 19 (03.02) | Docker: image, container, asosiy buyruqlar | 📘 Mavzu | Ishga tushirilgan konteynerlar |
| [56](dars-56/dars-reja.md) | 19 (03.02) | Dockerfile: FastAPI ilovani konteynerlash | 📘 Mavzu | O'z image'i |
| [57](dars-57/dars-reja.md) | 19 (03.02) | Docker Compose: FastAPI + PostgreSQL, env o'zgaruvchilar | 📘 Mavzu | Ko'p xizmatli stack |
| [58](dars-58/dars-reja.md) | 20 (10.02) | Nginx: reverse proxy, load balancer | 📘 Mavzu | Nginx ortidagi API |
| [59](dars-59/dars-reja.md) | 20 (10.02) | GitHub Actions: CI (lint + pytest) | 📘 Mavzu | Yashil CI pipeline |
| [60](dars-60/dars-reja.md) | 20 (10.02) | GitHub Actions: CD, secrets, Docker image build | 📘 Mavzu | Avtomatik build |
| [61](dars-61/dars-reja.md) | 21 (17.02) | Monitoring va logging, xavfsizlik, backup | 📘 Mavzu | Loglar va backup skripti |
| [62](dars-62/dars-reja.md) | 21 (17.02) | Deploy: serverga joylash (VPS/Render), rollback | 📘 Mavzu | Internetdagi API |
| [63](dars-63/dars-reja.md) | 21 (17.02) | AI DevOps: AI bilan Dockerfile/workflow yozish, xato loglarini tahlil qilish | 🤖 AI | AI yordamida tuzatilgan pipeline |
| [64](dars-64/dars-reja.md) | 22 (24.02) | Startap MVP 2-sprint: Docker Compose + Nginx | 🚀 Loyiha | Konteynerdagi MVP |
| [65](dars-65/dars-reja.md) | 22 (24.02) | Startap MVP 3-sprint: CI/CD + deploy | 🚀 Loyiha | Internetdagi startap |
| [66](dars-66/dars-reja.md) | 22 (24.02) | DevOps challenge: "Buzilgan serverni tuzat" (incident o'yini) | 🏆 Challenge | Tiklangan xizmat |
| [67](dars-67/dars-reja.md) | 23 (03.03) | Pitch tayyorlash | 🚀 Loyiha | Pitch deck |
| [68](dars-68/dars-reja.md) | 23 (03.03) | Yakuniy nazorat | 🎤 Nazorat/Demo | Nazorat natijasi |
| [69](dars-69/dars-reja.md) | 23 (03.03) | Demo Day: 9.2 vs 9.3 startaplari | 🎤 Nazorat/Demo | Pitch + jonli demo |
| [70](dars-70/dars-reja.md) | 24 (10.03) | Yakun: refleksiya, GitHub portfolio, 10-sinf yo'l xaritasi, mukofotlash | 🎤 Nazorat/Demo | Portfolio |

## Rasmiy dastur bilan moslik
| Bob | Rasmiy (102) | Bu reja (70) | Izoh |
|---|---|---|---|
| I. Python asoslari | 26 | 13 | Guruh Python'ni oldin o'rgangan, shuning uchun tezkor |
| II. OOP, bot, Linux | 21 | 14 | To'liq |
| III. PostgreSQL | 14 | 10 | To'liq + SQL Murder Mystery |
| IV. FastAPI | 20 | 15 | To'liq + startap |
| V. DevOps | 21 | 18 | To'liq + startap deploy |

## Baholash
- Har chorakda: oraliq nazorat (amaliy + test) + loyiha.
- Yakuniy baho = 40% loyihalar + 30% nazoratlar + 20% uyga vazifalar + 10% faollik (XP).
