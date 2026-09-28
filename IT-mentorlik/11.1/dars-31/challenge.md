# 31-dars challenge: "Docker Quest" 🗺

**Vaqt:** 15 daqiqa | **Format:** jamoalar (MVP jamoalari) | Bosqichlar ketma-ket, har biri +5 XP

1. 🔎 Docker Hub'dan **rasmiy** Redis image'ini toping va ishga tushiring (fon rejimida, nom: `kesh`).
2. 🗝 `docker exec` bilan `redis-cli` ga kiring, `SET jamoa "<jamoa nomi>"` va `GET jamoa` qiling.
3. 🕵️ `docker inspect kesh` dan konteynerning **IP manzilini** toping.
4. 📜 `docker logs kesh` dan Redis versiyasini toping.
5. 🧹 Kompyuterdagi **barcha** to'xtagan konteynerlarni **bitta** buyruq bilan o'chiring.
6. 🏁 Mentorga bitta skrinshotda: `docker ps -a` (bo'sh) + `docker images` ko'rsating.

**XP:** har bir bosqich +5 · birinchi tugatgan jamoa +15
<details><summary>Mentor uchun javoblar</summary>

1. `docker run -d --name kesh redis:7-alpine` · 2. `docker exec -it kesh redis-cli` · 3. `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' kesh` · 4. `docker logs kesh | grep -i version` · 5. `docker container prune` (yoki `docker rm $(docker ps -aq -f status=exited)`)
</details>
