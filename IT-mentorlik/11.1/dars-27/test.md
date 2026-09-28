# 27-dars tezkor test

1. Sozlamalar qaysi papkada? — `/etc`
2. `chmod 640 f` — kim nima qila oladi? — egasi o'qish/yozish, guruh o'qish, boshqalar hech narsa
3. Servisni server yoqilganda avtomatik ishga tushirish? — `systemctl enable`
4. Servis loglarini ko'rish? — `journalctl -u nom`
5. `Restart=always` nima qiladi? — Jarayon qulasa, systemd uni qayta ishga tushiradi
6. Nega ilovani root sifatida ishga tushirmaslik kerak? — Buzilsa, hujumchi butun serverni egallaydi (least privilege)
