# 12-dars slaydlari: AI pair programming

## 1-slayd
🤖👨‍💻 **Pair programming: siz — pilot, AI — shturman**

## 2-slayd — LLM qanday ishlaydi?
Matn → **tokenlar** → model keyingi tokenning **ehtimolini** hisoblaydi → eng mosini tanlaydi → takrorlaydi
"Kontekst oynasi" — AI bir vaqtda "ko'ra oladigan" matn hajmi

## 3-slayd — AI'ning 5 ta roli
✍️ **Yozuvchi:** "Funksiya yoz..."
🧑‍🏫 **Tushuntiruvchi:** "Bu kod nima qiladi? 9-sinf o'quvchisiga tushuntir"
🔍 **Reviewer:** "Senior sifatida review qil: xatolar, xavfsizlik, nomlash"
🧪 **Tester:** "Bu funksiya uchun chegaraviy holatlarni sanab ber"
🦆 **Rezina o'rdak:** "Menga savollar ber, men o'zim xatoni topay"

## 4-slayd — Kuchli prompt
```
Rol: Sen tajribali Python mentorisan.
Kontekst: Men 9-sinfdaman, OOP'ni hali o'rganmaganman. Python 3.12.
Vazifa: JSON faylda saqlanadigan viktorina o'yini uchun funksiyalar yoz.
Cheklovlar: faqat standart kutubxona, klasslarsiz, type hint va docstring bilan,
har bir funksiya 15 qatordan oshmasin.
Format: avval funksiyalar ro'yxati va vazifalari, keyin kod.
```

## 5-slayd — Bosqichma-bosqich so'rang
1️⃣ "Reja tuz" → 2️⃣ "1-funksiyani yoz" → 3️⃣ "Test qanday qilaman?" → 4️⃣ "Review qil"
Hammasini bitta promptda so'ramang!

## 6-slayd — ⚠️ AI xatolari
- Mavjud bo'lmagan kutubxona va funksiyalar
- Eskirgan sintaksis
- Xavfsizlik muammolari (parollar kodda, `eval()`)
- Ishonch bilan aytilgan noto'g'ri ma'lumot

## 7-slayd — Qoidalar
1. Siz — kodning egasisiz, javobgarlik sizda
2. Tushunmagan qatorni ishlatmang
3. Maxfiy ma'lumotni (parol, token) AI'ga bermang
4. Nazoratlarda AI yo'q
