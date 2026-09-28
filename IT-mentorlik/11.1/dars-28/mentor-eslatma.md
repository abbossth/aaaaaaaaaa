# 28-dars mentor eslatmasi

- **O'quv serveri:** eng arzon VPS (oyiga ~5$, masalan Hetzner, DigitalOcean, yoki mahalliy provayder) + har jamoaga alohida foydalanuvchi. Yoki har jamoaga killercoda.com'dagi playground (bepul, 1 soat).
- Windows'da `ssh-copy-id` yo'q. Muqobil: `type $env:USERPROFILE\.ssh\id_ed25519.pub | ssh user@server "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"` yoki Git Bash'da `ssh-copy-id` bor.
- "Serverni mustahkamla" challenge'i uchun zaif muhitni oldindan tayyorlang (skript bilan).
- **Etika:** o'quvchilar faqat **o'z** o'quv serverlarida mashq qilsin. Begona serverlarga ulanishga urinish — qonunbuzarlik. Buni aniq ayting.
