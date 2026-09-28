# 31-dars amaliy topshiriq

## 🟢 Oson (+5 XP)
1. `docker run hello-world` natijasini o'qing va 4 ta qadamni o'z so'zingiz bilan yozing.
2. `nginx:alpine` ni `-p 8081:80` bilan ishga tushiring, brauzerda oching, `docker logs` da so'rovingizni toping.

## 🟡 O'rta (+10 XP)
3. Jamoangiz MVP'sining landing sahifasini (`web/` build yoki oddiy HTML) nginx konteynerida bind mount (`-v`) orqali ko'rsating.
4. Bir vaqtda 3 ta nginx konteyner (8081, 8082, 8083 portlar) ishga tushiring. `docker ps --format "table {{.Names}}\t{{.Ports}}\t{{.Status}}"` bilan ko'rsating.

## 🔴 Qiyin (+20 XP)
5. `postgres:16-alpine` konteynerini ishga tushiring (`-e POSTGRES_PASSWORD=...`, `-p 5433:5432`). `docker exec -it <nom> psql -U postgres` bilan kirib, jadval yarating. Konteynerni o'chirib qayta yarating — jadval qoldimi? Nega? (Javob: keyingi darslar — **volume**.)
6. `node:20-alpine` va `node:20` image hajmini solishtiring (`docker images`). Nega farq bunchalik katta?
