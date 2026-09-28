# 28-dars slaydlari: SSH 🔐

## 1-slayd
**Internetga ochiq server → bir necha daqiqada birinchi hujum**

## 2-slayd — SSH = xavfsiz masofaviy terminal
```bash
ssh deploy@203.0.113.10
```
Barcha trafik shifrlangan. 22-port (standart)

## 3-slayd — Kalit juftligi 🔑🔒
🔒 **Ochiq kalit** (`id_ed25519.pub`) — **qulf**. Istalgan serverga qo'yishingiz mumkin
🔑 **Yopiq kalit** (`id_ed25519`) — **kalit**. Faqat sizda! Hech kimga bermang!
Server "qulfni" ko'radi → faqat sizning "kalitingiz" ochadi

## 4-slayd — Qadamlar
```bash
ssh-keygen -t ed25519 -C "aziz@11.1"      # 1. kalit yaratish
ssh-copy-id deploy@server                 # 2. qulfni serverga qo'yish
ssh deploy@server                         # 3. parolsiz kirish ✨
```

## 5-slayd — ~/.ssh/config
```
Host mvp
    HostName 203.0.113.10
    User deploy
    IdentityFile ~/.ssh/id_ed25519
```
Endi: `ssh mvp` 🚀

## 6-slayd — Serverni himoyalash 🛡
`/etc/ssh/sshd_config`:
```
PasswordAuthentication no
PermitRootLogin no
```
```bash
sudo ufw allow OpenSSH
sudo ufw allow 80,443/tcp
sudo ufw enable
```

## 7-slayd — GitHub + SSH
GitHub → Settings → SSH and GPG keys → New → `.pub` faylni qo'yish
`git clone git@github.com:user/repo.git` — parolsiz push!
