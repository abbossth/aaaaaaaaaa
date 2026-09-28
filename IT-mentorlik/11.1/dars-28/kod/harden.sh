#!/bin/bash
# Yangi Ubuntu serverni asosiy himoyalash (mentor bilan birga, FAQAT o'quv serverida!)
# DIQQAT: SSH kalitingiz 'deploy' foydalanuvchisiga qo'yilganini TEKSHIRMASDAN ishga tushirmang,
# aks holda serverga kira olmay qolasiz.
set -euo pipefail

# 1. deploy foydalanuvchisi
id deploy &>/dev/null || sudo adduser --disabled-password --gecos "" deploy
sudo usermod -aG sudo deploy

# 2. SSH sozlamalari
sudo sed -i 's/^#\?PasswordAuthentication .*/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo sed -i 's/^#\?PermitRootLogin .*/PermitRootLogin no/' /etc/ssh/sshd_config
sudo sshd -t && sudo systemctl reload ssh

# 3. Firewall
sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw --force enable
sudo ufw status verbose
