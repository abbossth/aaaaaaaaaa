# 3-dars challenge: "Men — internetman!" 🎭 (rol o'yini)

**Vaqt:** 20 daqiqa | **Format:** butun sinf

## Rollar (kartochkalarga yozib tarqating)
| Rol | Nechta o'quvchi | Vazifasi |
|---|---|---|
| 💻 Client (brauzer) | 2 | So'rov yozadi: "Menga youtube.com kerak" |
| 📒 DNS server | 1 | Kitobchada domen → IP jadvali bor, IP'ni aytadi |
| 🚚 Router (yo'naltiruvchi) | 2–3 | Paketni keyingi routerga yoki serverga uzatadi |
| 🖥 YouTube server | 1 | So'rovni oladi, "javob paketi"ni tayyorlaydi |
| 🖥 Kun.uz server | 1 | Xuddi shunday |
| 🦹 Xaker (qiyin raund) | 1 | Paketni "o'g'irlashga" urinadi |

## Tayyorlanadigan narsalar
- DNS kitobchasi: `youtube.com → 1.1.1.1`, `kun.uz → 2.2.2.2`, `google.com → 3.3.3.3`
- Qog'oz "paketlar": konvert yoki buklangan qog'oz. Ustiga **kimdan** (client IP) va **kimga** (server IP) yoziladi.

## 1-raund (oddiy)
1. Client DNS'dan IP so'raydi.
2. Client paketga IP yozib, routerga beradi.
3. Routerlar paketni serverga yetkazadi.
4. Server javob paketini yozadi (masalan, qog'ozga video "kadr" chizadi) va teskari yo'l bilan qaytaradi.
5. Mentor sekundomer bilan vaqtni o'lchaydi.

## 2-raund (tezlik)
Ikki client bir vaqtda so'rov yuboradi. Qaysi so'rov birinchi qaytadi? Routerlar "yuklama"ni his qiladi.

## 3-raund (xavfsizlik)
Xaker paketni yo'lda ochib o'qishga urinadi. Client va server oldindan kelishilgan "shifr" (masalan, har bir harfni keyingisiga almashtirish) bilan yozishadi.
➡️ Xulosa: **HTTPS** va qulf belgisi 🔒 aynan shuning uchun kerak.

## Xulosa savollari
- DNS "kasal bo'lib qolsa" nima bo'ladi? (Sayt nomi ishlamaydi, lekin IP bilan kirish mumkin)
- Server o'chib qolsa-chi? (Sayt ochilmaydi)
- Nega routerlar ko'p? (Bittasi buzilsa, boshqa yo'l topiladi)

## XP
Barcha faol ishtirokchilarga +10 XP, xakerni "fosh qilgan" o'quvchiga +5 XP.
