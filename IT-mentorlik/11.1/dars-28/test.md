# 28-dars tezkor test

1. SSH standart porti? — 22
2. Qaysi kalitni serverga qo'yamiz: ochiq yoki yopiq? — Ochiq (`.pub`)
3. Kalit yaratish buyrug'i? — `ssh-keygen -t ed25519`
4. Parolli SSH kirishni qanday o'chiramiz? — `PasswordAuthentication no`
5. `ufw` nima? — Oddiy firewall (Uncomplicated Firewall)
6. SSH sozlamasini o'zgartirishdan oldin nima qilish kerak? — Ikkinchi sessiyani ochiq qoldirish va `sshd -t` bilan tekshirish
