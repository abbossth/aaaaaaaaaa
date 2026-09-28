# 32-dars amaliy topshiriq: "Direktor uchun hisobot"

Bazani yangilang (29 va 30-darslardagi fayllar). Har bir so'rovni `hisobot.sql` fayliga yozing.

## 🟢 Oson (+5 XP)
1. Ismi "a" harfi bilan tugaydigan talabalar.
2. 2010-yildan keyin tug'ilgan va Telegram'i bor talabalar soni.
3. Informatika fanidan olingan eng past baho.

## 🟡 O'rta (+10 XP)
4. Har bir sana bo'yicha qo'yilgan baholar soni va o'rtachasi.
5. Har bir to'garakda nechta a'zo bor (`azolik` jadvali, `togarak_id` bo'yicha). Eng ko'pi birinchi.
6. Faqat 1 ta bahosi bor talabalar (`HAVING COUNT(*) = 1`).

## 🔴 Qiyin (+20 XP)
7. Har bir talaba uchun: baholar soni, o'rtachasi, va `CASE` bilan maqomi: ≥4.5 "a'lochi", ≥3.5 "yaxshi", qolgani "e'tibor kerak".
8. Qaysi fanda "2" yoki "3" baholar ulushi eng yuqori? (Maslahat: `COUNT(*) FILTER (WHERE baho <= 3)` yoki `SUM(CASE ...)`)

> Talaba ismlari bilan chiqarish uchun jadvallarni **birlashtirish** kerak — bu keyingi darsda (JOIN)!
