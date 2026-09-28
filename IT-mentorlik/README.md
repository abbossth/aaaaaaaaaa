# IT Mentorlik — 2026/2027 o'quv yili

"Muhammad al-Xorazmiy vorislari" maxsus guruhlari uchun o'quv rejalar va dars materiallari.

| Guruh | Yo'nalish | Boshlang'ich daraja | Reja |
|---|---|---|---|
| **8.10** | Web Full-stack dasturlash | Noldan (yangi guruh) | [umumiy-reja](8.10/umumiy-reja.md) |
| **8.2** | Web Full-stack dasturlash | HTML, CSS, ozgina JS, Word/Excel | [umumiy-reja](8.2/umumiy-reja.md) |
| **9.2** | Advanced Back-end va DevOps | HTML/CSS/JS, Bootstrap, Git, terminal, Python (yuzaki) | [umumiy-reja](9.2/umumiy-reja.md) |
| **9.3** | Advanced Back-end va DevOps | 9.2 bilan bir xil | [umumiy-reja](9.3/umumiy-reja.md) |
| **11.1** | Professional IT Development | HTML/CSS/JS, Bootstrap, Git, React asoslari (Python yo'q) | [umumiy-reja](11.1/umumiy-reja.md) |

- **Boshlanish:** 30-sentabr 2026
- **Hajm:** har bir guruhga 70 ta dars
- **Jadval:** haftasiga 3 marta, har biri 80 daqiqa
- **Asos:** rasmiy standartlar va o'quv qo'llanmalar (RTRM, 2025–2026)

---

## Papka tuzilishi

```
IT-mentorlik/
├── README.md               ← shu fayl: umumiy qoidalar, gamifikatsiya, dars shabloni
├── 8.10/
│   ├── umumiy-reja.md      ← 70 ta dars: hafta, mavzu, dars turi, natija
│   ├── dars-01/
│   │   ├── dars-reja.md          ← maqsad, daqiqama-daqiqa konspekt, mentor matni
│   │   ├── taqdimot.md           ← slaydlarga ko'chirish uchun matn
│   │   ├── amaliy-topshiriq.md   ← oson / o'rta / qiyin + yechimlar
│   │   ├── challenge.md          ← o'yin yoki musobaqa qoidalari
│   │   ├── uyga-vazifa.md
│   │   ├── test.md               ← savollar + javoblar kaliti
│   │   ├── mentor-eslatma.md     ← ko'p uchraydigan xatolar, maslahatlar
│   │   └── kod/                  ← namuna va starter kodlar
│   └── dars-02/ ...
├── 8.2/   (xuddi shunday)
├── 9.2/   (xuddi shunday)
├── 9.3/   ← 9.2 darslaridan foydalanadi (dastur bir xil), faqat guruhlararo musobaqa jadvali alohida
└── 11.1/  (xuddi shunday)
```

---

## Dars turlari

| Belgi | Tur | Ma'nosi |
|---|---|---|
| 📘 | Mavzu | Standartdagi asosiy mavzu, interaktiv formatda |
| 🤖 | AI | Sun'iy intellekt bilan dasturlash: prompt, AI bilan kod yozish, AI kodini tekshirish |
| 🏆 | Challenge | Musobaqa, hakaton, Bug Hunt, o'yin |
| 🚀 | Loyiha / Startap | Real loyiha, MVP, sprint, pitch tayyorlash |
| 🎤 | Nazorat / Demo Day | Oraliq va yakuniy nazorat, loyiha taqdimoti |

---

## 80 daqiqalik dars shabloni

| Vaqt | Bosqich | Maqsad |
|---|---|---|
| 0–5 | **Hook** | Qiziq savol, "wow" namoyish, hayotiy misol: e'tiborni ushlash |
| 5–10 | **Takrorlash** | 3–5 savollik tezkor quiz (Kahoot / Quizizz / qo'l ko'tarish) |
| 10–25 | **Yangi mavzu** | Qisqa tushuntirish + jonli kod (mentor ekranda yozadi) |
| 25–60 | **Amaliyot** | Oson → o'rta → qiyin topshiriqlar; mentor aylanib yordam beradi |
| 60–72 | **Challenge** | Mini musobaqa, jamoaviy topshiriq, ball yig'ish |
| 72–80 | **Yakun** | "Bugun nimani o'rgandim?" (har kim 1 jumla), uyga vazifa, ballar e'loni |

**Oltin qoidalar:**
1. Mentor 15 daqiqadan ko'p tinimsiz gapirmaydi.
2. Har bir o'quvchi dars oxirida o'zi yasagan **ko'rinadigan natija**ga ega bo'ladi.
3. Xato qilish — normal. "Eng qiziq xato" uchun ham ball beriladi.
4. Kuchli o'quvchi zerikmasligi uchun har doim "qiyin" daraja topshiriq bor.
5. Zaif o'quvchi yo'qolmasligi uchun "juftlikda dasturlash" (pair programming) qo'llaniladi.

---

## Gamifikatsiya tizimi — "XP liga"

### Ball (XP) qanday olinadi

| Harakat | XP |
|---|---|
| Darsga kelish | +5 |
| Tezkor quizda to'g'ri javob | +2 (har biri) |
| Oson topshiriq | +5 |
| O'rta topshiriq | +10 |
| Qiyin topshiriq | +20 |
| Challenge'da 1/2/3-o'rin | +30 / +20 / +10 |
| Uyga vazifa (o'z vaqtida) | +10 |
| Boshqaga yordam berish (mentor tasdiqlaydi) | +5 |
| "Eng qiziq xato" (xatoni topib, tushuntirib berish) | +5 |
| GitHub'ga push qilingan ish | +5 |
| Demo Day'da taqdimot | +50 |

### Darajalar

| XP | Daraja |
|---|---|
| 0–99 | 🥚 Stajyor (Intern) |
| 100–249 | 🐣 Junior |
| 250–499 | 🐥 Middle |
| 500–899 | 🦅 Senior |
| 900+ | 🐉 Tech Lead |

### Badge'lar (nishonlar)
- 🐞 **Bug Hunter**: challenge'da eng ko'p xato topgan
- ⚡ **Speed Coder**: topshiriqni birinchi bo'lib bajargan
- 🤝 **Team Player**: jamoadoshlari tomonidan eng foydali deb topilgan
- 🎨 **Designer**: eng chiroyli interfeys
- 🤖 **AI Whisperer**: eng yaxshi prompt yozgan
- 🚀 **Founder**: startap loyihasini deploy qilgan
- 🔥 **Streak 10**: 10 dars ketma-ket uyga vazifa topshirgan

### Qanday yuritiladi
- Google Sheets'da jadval: o'quvchi | XP | daraja | badge'lar. Har dars oxirida yangilanadi.
- Har hafta sinf devoriga yoki Telegram guruhga **TOP-5** chiqariladi.
- Har chorak oxirida **"Oy/chorak dasturchisi"** e'lon qilinadi (sertifikat, stiker yoki kichik sovg'a).
- 9.2 va 9.3 o'rtasida **guruhlararo liga** bor (qarang: [9.3/umumiy-reja.md](9.3/umumiy-reja.md)).

---

## Sun'iy intellektdan foydalanish qoidalari (o'quvchilar uchun)

1. **Avval o'zing o'yla, keyin AI'dan so'ra.** Kamida 5 daqiqa o'zing urinib ko'r.
2. **AI yozgan kodni tushunmasang, ishlatma.** Har bir qatorini tushuntirib bera olishing kerak.
3. **AI xato qiladi.** Uning kodini doim ishga tushirib tekshir.
4. **Nazorat ishlarida AI taqiqlanadi**, agar mentor boshqacha demasa.
5. **Yaxshi prompt = yaxshi natija:** rol + vazifa + kontekst + format + cheklovlar.

Tavsiya etilgan vositalar: ChatGPT, Claude, Gemini, GitHub Copilot (o'quvchilar uchun GitHub Student Pack orqali bepul), v0.dev, Bolt.new.

---

## Kerakli dasturlar (sinf kompyuterlariga)

- **Hamma guruh:** VS Code, Google Chrome, Git, Telegram Desktop
- **8-sinflar:** Flowgorithm, Figma (brauzerda), Python 3.12+, PostgreSQL + pgAdmin
- **9-sinflar:** Python 3.12+, PostgreSQL + pgAdmin, Postman, Docker Desktop (yoki Play with Docker), WSL / Linux
- **11-sinf:** Node.js LTS, Docker Desktop, Postman, AWS Free Tier akkaunti (mentor orqali), Trello/Jira

> Internet sekin bo'lsa yoki kompyuterlar kuchsiz bo'lsa, onlayn muqobillar: **replit.com**, **codesandbox.io**, **labs.play-with-docker.com**, **sqliteonline.com**, **github.dev**.
