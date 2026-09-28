# 28-dars amaliy topshiriq

## 🟢 Oson (+10 XP): GitHub + SSH (hamma uchun)
1. `ssh-keygen -t ed25519 -C "email@example.com"` (Enter, Enter — passphrase ixtiyoriy)
2. `cat ~/.ssh/id_ed25519.pub` → GitHub → Settings → SSH and GPG keys → New SSH key
3. `ssh -T git@github.com` → "Hi username! You've successfully authenticated" ✅
4. Jamoa reposini SSH manzili bilan qayta clone qiling (`git@github.com:...`) va parolsiz push qiling.

## 🟡 O'rta (+10 XP): Serverga kirish
(Mentor o'quv serveri yoki killercoda'dagi 2-mashina)
5. Mentor bergan foydalanuvchi bilan parol orqali kiring.
6. O'z ochiq kalitingizni `~/.ssh/authorized_keys` ga qo'shing (`ssh-copy-id` yoki qo'lda). Endi parolsiz kiring.
7. `~/.ssh/config` da alias yarating va `ssh mvp` bilan kiring.

## 🔴 Qiyin (+20 XP): Xavfsizlik
8. `sudo tail -n 30 /var/log/auth.log` — begona IP'lardan urinishlar bormi?
9. Mentor bilan `kod/harden.sh` ni tahlil qiling (har qatori nima qiladi?) va o'quv serverida qo'llang.
10. `sudo ufw status` — qaysi portlar ochiq? Nega aynan shular?
11. **Bonus:** `fail2ban` o'rnating va sozlang (5 ta noto'g'ri urinishdan keyin IP bloklanadi).
