# 27-dars. Linux: fayl tizimi, chmod/chown, apt, systemctl

**Guruh:** 11.1 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** II bob, "Unix/Linux muhiti va tarmoq xizmati konfiguratsiyasi"

## Maqsad
- Fayl tizimi iyerarxiyasini biladi: `/etc` (sozlamalar), `/var/log` (loglar), `/usr` (dasturlar), `/home`, `/tmp`, `/opt`.
- Ruxsatlar va egalik: `chmod` (raqamli va harfli), `chown`, `sudo`, foydalanuvchi va guruhlar (`adduser`, `usermod -aG`).
- Paket menejeri (`apt update/install/remove`) va servislarni boshqarish: `systemctl status/start/stop/restart/enable`, `journalctl -u`.
- Node ilovasini **systemd servisi** sifatida ishga tushiradi (server qayta yuklansa ham ishlaydi).

## Muhit
WSL (Ubuntu) yoki **killercoda.com/playgrounds** (brauzerda Ubuntu, `systemd` bilan).

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | *"Sizning MVP'ingiz hozir faqat noutbukda ishlaydi. Noutbuk yopilsa — startap o'ladi. Real serverda u 24/7 ishlashi, qulasa — avtomatik qayta turishi kerak. Bu — Linux + systemd."* |
| 5–25 | **Yangi mavzu** | Fayl tizimi, ruxsatlar, foydalanuvchilar, apt, systemd (`taqdimot.md`) |
| 25–60 | **Amaliyot** | `amaliy-topshiriq.md`: Node API'ni systemd servisi qilish |
| 60–75 | **Challenge** | `challenge.md`: "Server detektivi" |
| 75–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +20/+10/+5
