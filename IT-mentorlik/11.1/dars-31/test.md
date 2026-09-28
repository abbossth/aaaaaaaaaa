# 31-dars tezkor test

1. Konteynerning VM'dan asosiy farqi? — Host OS yadrosidan umumiy foydalanadi, o'z OS'i yo'q → yengil va tez
2. Image va container farqi? — Image — qolip (faqat o'qiladi), container — undan ishga tushirilgan nusxa
3. `-p 8080:80` da 8080 qaysi port? — Host (kompyuter) porti
4. Ishlayotgan konteynerlar ro'yxati? — `docker ps`
5. Konteyner ichida buyruq bajarish? — `docker exec -it <nom> sh`
6. Konteyner o'chirilsa, ichidagi fayllar? — Yo'qoladi (volume/bind mount ishlatilmasa)
7. Image'lar qayerdan yuklanadi? — Registry'dan (standart — Docker Hub)
