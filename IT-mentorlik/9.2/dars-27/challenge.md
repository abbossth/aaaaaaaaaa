# 27-dars challenge: "Terminal Quest" — OverTheWire Bandit 🏴‍☠️

**Vaqt:** 40 daqiqa | **Format:** individual | **Sayt:** overthewire.org/wargames/bandit

## Qoidalar
1. Har bir darajada keyingi darajaning **parolini** topasiz.
2. Keyingi darajaga ulanish: `ssh banditN@bandit.labs.overthewire.org -p 2220`
3. Parollarni `bandit-parollar.txt` fayliga yozib boring (kompyuteringizda!).
4. Internetdagi tayyor yechimlarni qidirish **taqiqlanadi**. Faqat `man` va sayt maslahatlari.
5. 40 daqiqadan keyin eng yuqori daraja hisoblanadi.

## Darajalar va kerakli buyruqlar (maslahat)
| Daraja | Mavzu |
|---|---|
| 0 → 1 | `ls`, `cat` |
| 1 → 2 | `-` nomli fayl: `cat ./-` |
| 2 → 3 | Probelli nom: `cat "spaces in this filename"` |
| 3 → 4 | Yashirin fayl: `ls -la` |
| 4 → 5 | `file ./*` (odam o'qiy oladigan faylni topish) |
| 5 → 6 | `find . -size 1033c ! -executable` |
| 6 → 7 | `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null` |
| 7 → 8 | `grep millionth data.txt` |
| 8 → 9 | `sort data.txt \| uniq -u` |
| 9 → 10 | `strings data.txt \| grep "==="` |

**XP:** har bir daraja +3 · 🥇 +30 · 🥈 +20 · 🥉 +10 · 5+ daraja → 🐧 "Linux Ninja"
**Liga:** 9.2 va 9.3 ning o'rtacha darajasi solishtiriladi (bonus, asosiy liga jadvalidan tashqari)
