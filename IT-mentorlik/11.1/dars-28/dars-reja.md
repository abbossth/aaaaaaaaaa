# 28-dars. SSH: kalit juftligi, serverga ulanish, ufw, xavfsizlik

**Guruh:** 11.1 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** II bob, "SSH uchun kalit juftligi (ssh-keygen), kalitni serverga joylash (ssh-copy-id), xavfsizlik"

## Maqsad
- SSH nima ekanini va nega Telnet/parolli kirish xavfli ekanini tushunadi.
- Asimmetrik kriptografiya g'oyasini sodda tushunadi: ochiq kalit (qulf) va yopiq kalit (kalit).
- `ssh-keygen -t ed25519` bilan kalit juftligi yaratadi, `ssh-copy-id` yoki `authorized_keys` orqali serverga joylaydi.
- `~/.ssh/config` bilan qisqa nomlar (host alias) sozlaydi.
- Serverni himoyalaydi: parolli kirishni o'chirish, root login'ni taqiqlash, `ufw` firewall, portlar.
- GitHub'ga SSH kalit qo'shib, parolsiz push qiladi.

## Muhit
- Mentor tayyorlagan o'quv serveri (VPS) yoki **killercoda.com** (2 ta mashinali "Ubuntu" playground)
- Minimal: GitHub'ga SSH kalit bilan ulanish (hamma uchun ishlaydi)

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Statistika: internetga ochiq har qanday server bir necha daqiqa ichida avtomatik botlar tomonidan parol terish hujumiga uchraydi (`/var/log/auth.log` dagi real yozuvlar skrinshoti). *"Parol bilan kirish — eshikni kalit bilan emas, raqamli qulf bilan yopish. Buni botlar terib ko'radi."* |
| 5–20 | **Yangi mavzu** | SSH, kalit juftligi (qulf va kalit analogiyasi), fingerprint, `known_hosts` |
| 20–50 | **Amaliyot** | `amaliy-topshiriq.md` |
| 50–68 | **Challenge** | `challenge.md`: "Serverni mustahkamla" |
| 68–80 | **Yakun** | XP, uyga vazifa |

## Baholash (XP)
- GitHub SSH +10 · Serverga kalit bilan kirish +10 · Xavfsizlik sozlamalari +20
