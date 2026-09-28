#!/usr/bin/env bash
# 31-dars: jonli namoyish uchun buyruqlar (qatorma-qator bajaring, hammasini birdan emas)

docker version                      # Client va Server (daemon) — ikkalasi ham ko'rinishi kerak
docker run hello-world              # birinchi konteyner: pull → create → start → xabar → exit

# 1) Nginx veb-server — 1 buyruqda (30-darsda qo'lda sozlagan edik!)
docker run -d -p 8080:80 --name veb nginx:alpine
docker ps
curl localhost:8080                 # yoki brauzerda http://localhost:8080
docker logs veb

# 2) Konteyner ichiga kirish va o'zgartirish
docker exec -it veb sh
#   echo '<h1>Salom, 11.1! 🐳</h1>' > /usr/share/nginx/html/index.html
#   exit
curl localhost:8080

# 3) O'chirish → o'zgarishlar yo'qoladi (konteyner "bir martalik")
docker rm -f veb
docker run -d -p 8080:80 --name veb nginx:alpine
curl localhost:8080                 # yana standart sahifa!

# 4) Papkani ulash (bind mount) — o'zgarish saqlanadi
mkdir -p sayt && echo '<h1>Mening saytim</h1>' > sayt/index.html
docker rm -f veb
docker run -d -p 8080:80 -v "$(pwd)/sayt:/usr/share/nginx/html:ro" --name veb nginx:alpine

# 5) Muhit o'zgaruvchilari (-e) va interaktiv rejim
docker run --rm -it -e ISM=Aziz node:20-alpine node -e 'console.log(`Salom, ${process.env.ISM}!`, process.version)'
docker run --rm -it python:3.12-alpine python -c 'print("Python ham bor 🐍")'

# 6) Image qatlamlari
docker image history nginx:alpine
docker images

# 7) Tozalash
docker rm -f veb
docker system df                    # qancha joy egallangan
docker system prune                 # to'xtagan konteynerlar va keraksiz qatlamlar
