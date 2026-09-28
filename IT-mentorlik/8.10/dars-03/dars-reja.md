# 3-dars. Internet qanday ishlaydi? Client-server, IP, DNS, hosting, domen. Front-end va Back-end

**Guruh:** 8.10 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa

## Maqsad
- Brauzerga `youtube.com` yozilganda nima sodir bo'lishini bosqichma-bosqich tushuntira oladi.
- Client, server, IP-manzil, DNS, domen va hosting tushunchalarini biladi.
- Front-end va back-end farqini real misollarda ajrata oladi.

## Kerakli narsalar
- Rol o'yini uchun kartochkalar (`challenge.md` bo'yicha)
- Brauzer, `cmd` (buyruqlar qatori)

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Savol: *"YouTube'dagi video qayerda turadi? Sizning telefoningizdami?"* Javoblarni tinglash. *"Video minglab km uzoqdagi kompyuterda turadi va 1 soniyada sizga yetib keladi. Bugun bu qanday ishlashini bilib olamiz."* |
| 5–10 | **Takrorlash** | 2-dars testi |
| 10–25 | **Yangi mavzu** | Pochta analogiyasi: client = xat yozuvchi, server = javob beruvchi idora, IP = uy manzili, DNS = telefon kitobi (nom → raqam), domen = oson eslanadigan nom, hosting = serverdan joy ijarasi. Slaydlar 2–7. |
| 25–35 | **Jonli namoyish** | `cmd` → `ping google.com` (IP va vaqt ko'rinadi), `nslookup youtube.com`, `tracert google.com` (paket qaysi yo'llardan o'tadi). Brauzerda `F12` → Network: sahifa ochilganda nechta so'rov ketadi. |
| 35–55 | **Challenge (rol o'yini)** | `challenge.md`: "Men — internetman!" |
| 55–70 | **Amaliyot** | `amaliy-topshiriq.md`: Front-end yoki Back-end saralash o'yini + DNS tadqiqoti |
| 70–80 | **Yakun** | "Brauzerga youtube.com yozildi. Keyin nima bo'ladi?" — zanjir bo'ylab har bir o'quvchi bitta qadamni aytadi. Uyga vazifa. |

## Asosiy zanjir (doskaga yozing)
```
1. Siz brauzerga youtube.com yozasiz (CLIENT)
2. Brauzer DNS'dan so'raydi: "youtube.com qaysi IP'da?"
3. DNS javob beradi: 142.250.x.x
4. Brauzer shu IP'dagi SERVER'ga so'rov (request) yuboradi
5. Server javob (response) qaytaradi: HTML, CSS, JS, video
6. Brauzer ularni chizadi, siz sahifani ko'rasiz
```

## Baholash (XP)
- Rol o'yinida faol ishtirok: +10
- Saralash o'yini 100% to'g'ri: +10
- DNS tadqiqoti (qiyin): +20
