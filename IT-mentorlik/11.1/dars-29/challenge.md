# 29-dars challenge: "502 detektivi" 🕵️

**Vaqt:** 17 daqiqa | **Format:** jamoalar

Mentor ataylab 4 ta "buzilish" yaratadi (har jamoada boshqa tartibda). Jamoa faqat **loglar va diagnostika buyruqlari** orqali sababni topib, tuzatadi:

| Belgi | Mumkin bo'lgan sabab | Qanday topiladi |
|---|---|---|
| `502 Bad Gateway` | Express to'xtatilgan (`systemctl stop mvp-api`) | `error.log`: "connect() failed (111: Connection refused)" |
| `nginx -t` xato | Konfiguratsiyada `;` yoki `}` yo'q | `sudo nginx -t` |
| React sahifasi `404` (yangilanganda) | `try_files` o'chirilgan | `access.log` + konfig |
| `403 Forbidden` | `/var/www/mvp` ga ruxsat yo'q (`chmod 700`) | `error.log`: "Permission denied" |

**Qoida:** avval **tashxis** (log/buyruq skrinshoti) → keyin tuzatish.
**XP:** har bir to'g'ri tashxis + tuzatish +5 · birinchi 4/4 jamoa +20
