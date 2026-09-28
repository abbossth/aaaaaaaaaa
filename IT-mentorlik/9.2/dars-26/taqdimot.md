# 26-dars slaydlari: Linux 🐧

## 1-slayd
**Serverlarning ~90%+ i Linux'da ishlaydi**

## 2-slayd — Fayl tizimi
```
/                 ← ildiz (hamma narsaning boshi)
├── home/aziz     ← foydalanuvchi papkasi (~)
├── etc/          ← sozlamalar (nginx, ssh...)
├── var/log/      ← loglar
├── usr/bin/      ← dasturlar
├── tmp/          ← vaqtinchalik fayllar
└── root/         ← administrator papkasi
```
Windows'dagi `C:\` o'rniga — `/`

## 3-slayd — Navigatsiya
`pwd` qayerdaman? · `ls -la` nima bor (yashirinlari ham)? · `cd papka` · `cd ..` yuqoriga · `cd ~` uyga
**Tab** — avtomatik to'ldirish! · **↑** — oldingi buyruq

## 4-slayd — Fayllar
`mkdir -p a/b/c` · `touch fayl.txt` · `cp a b` · `mv a b` (ko'chirish/nomini o'zgartirish) · `rm fayl` · `rm -r papka`
`cat` · `less` · `head -n 5` · `tail -f log.txt` (jonli kuzatish!)
`nano fayl.txt` — terminal muharriri (`Ctrl+O` saqlash, `Ctrl+X` chiqish)

## 5-slayd — Qidiruv
`grep "ERROR" app.log` — fayl ichidan · `grep -r "TOKEN" .` — papka bo'ylab
`find . -name "*.py"` — fayl nomlarini

## 6-slayd — Ruxsatlar
```
-rwxr-xr--  1 aziz  dev  script.sh
 │  │  │
 │  │  └─ boshqalar: r-- (faqat o'qish)
 │  └──── guruh:     r-x (o'qish, bajarish)
 └─────── egasi:     rwx (o'qish, yozish, bajarish)
```
r=4 w=2 x=1 → `chmod 754 script.sh` · `chmod +x script.sh`

## 7-slayd — sudo va ⚠️ xavf
`sudo` — administrator huquqi bilan bajarish
⚠️ `rm -rf /` — hamma narsani o'chiradi. **HECH QACHON!**
⚠️ Internetdan olingan buyruqni tushunmasdan `sudo` bilan bajarmang
