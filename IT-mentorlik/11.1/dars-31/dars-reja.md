# 31-dars. Docker: arxitektura, image va container, qatlamlar

**Guruh:** 11.1 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** II bob, "Konteynerlashtirish va Docker"

## Maqsad
- "Mening kompyuterimda ishlaydi" 🤷 muammosini va konteynerlar uni qanday hal qilishini tushunadi.
- Virtual mashina va konteyner farqini biladi (yadro umumiy, tez, yengil).
- Docker arxitekturasi: Docker CLI → Docker daemon (Engine) → registry (Docker Hub).
- Image (qolip, faqat o'qiladi, qatlamlardan iborat) va container (ishlayotgan nusxa) farqi.
- Asosiy buyruqlar: `run`, `ps`, `images`, `pull`, `stop`, `rm`, `logs`, `exec`, `-p`, `-d`, `-e`, `--name`.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Jamoadan biri MVP'ni boshqa kompyuterda ishga tushirishga urinadi: Node versiyasi boshqa, `npm install` xato... *"Butun kompyuterni konteynerga solib jo'natsak-chi?"* 📦 |
| 5–10 | **Takrorlash** | 30-dars: Nginx reverse proxy (bugun uni Docker'da 1 buyruq bilan ko'taramiz!) |
| 10–28 | **Yangi mavzu** | `taqdimot.md`: VM vs konteyner, arxitektura, image qatlamlari |
| 28–55 | **Jonli + amaliyot** | `kod/buyruqlar.sh` qadamma-qadam, keyin `amaliy-topshiriq.md` |
| 55–72 | **Challenge** | `challenge.md`: "Docker Quest" |
| 72–80 | **Yakun** | XP, uyga vazifa: keyingi darsda MVP'ni o'zimiz konteynerlaymiz |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Docker Quest: har bir bosqich +5, birinchi tugatgan +15

## Kerakli narsalar
- Docker Desktop (Windows: WSL2 yoqilgan) **yoki** brauzerda [Play with Docker](https://labs.play-with-docker.com) (Docker Hub akkaunti bilan, bepul, 4 soatlik sessiya).
