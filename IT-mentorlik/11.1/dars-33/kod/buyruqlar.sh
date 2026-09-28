#!/usr/bin/env bash
# 33-dars: network, volume, compose — namoyish ssenariysi (qatorma-qator)

# --- 1) Network: konteynerlar bir-birini NOMI bilan topadi ---
docker network create mvp-net
docker run -d --name db --network mvp-net -e POSTGRES_PASSWORD=parol postgres:16-alpine
docker run --rm -it --network mvp-net alpine ping -c 2 db        # "db" DNS nomi ishlaydi!
docker run --rm -it --network mvp-net postgres:16-alpine psql -h db -U postgres -c 'select version()'

# --- 2) Volume: konteyner o'lsa ham ma'lumot tirik ---
docker rm -f db
docker volume create pgdata
docker run -d --name db --network mvp-net -e POSTGRES_PASSWORD=parol \
  -v pgdata:/var/lib/postgresql/data postgres:16-alpine
sleep 3
docker exec -it db psql -U postgres -c "CREATE TABLE test(x int); INSERT INTO test VALUES (42);"
docker rm -f db                                                   # konteynerni o'ldiramiz 💀
docker run -d --name db --network mvp-net -e POSTGRES_PASSWORD=parol \
  -v pgdata:/var/lib/postgresql/data postgres:16-alpine
sleep 3
docker exec -it db psql -U postgres -c "SELECT * FROM test;"      # 42 — omon qoldi! 🎉
docker volume ls
docker volume inspect pgdata

# Tozalash
docker rm -f db && docker volume rm pgdata && docker network rm mvp-net

# --- 3) Compose: yuqoridagilarning hammasi — BITTA faylda ---
cp .env.example .env
docker compose up -d --build
docker compose ps
docker compose logs -f server           # Ctrl+C bilan chiqish
curl localhost:3000/api/health
curl -X POST localhost:3000/api/items -H 'Content-Type: application/json' -d '{"title":"Docker Compose ishlaydi"}'
curl localhost:3000/api/items
docker compose exec db psql -U mvp -d mvp -c 'SELECT * FROM items;'

docker compose down                     # konteynerlar va tarmoq o'chadi, VOLUME qoladi
docker compose up -d && curl localhost:3000/api/items   # ma'lumot joyida
docker compose down -v                  # ⚠️ volume ham o'chadi (ma'lumot yo'qoladi)
