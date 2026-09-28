# 33-dars challenge: "Compose-doktor" 🩺

**Vaqt:** 10 daqiqa | **Format:** jamoalar

Quyidagi `docker-compose.yml` da **6 ta xato** bor. Topib, tuzating (har biri +4 XP):

```yaml
services:
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: 12345
    ports:
      - "5432:5432"
  server:
    build: ./server
    environment:
      DATABASE_URL: postgres://postgres:12345@localhost:5432/postgres
    ports:
      - "3000"
    depends_on:
      - db
```

<details><summary>Mentor uchun javoblar</summary>

1. `postgres` — versiyasiz (`latest`) → `postgres:16-alpine`
2. Parol faylning ichida va juda oddiy → `${DB_PASSWORD}` + `.env`
3. Baza porti tashqariga ochiq (`5432:5432`) → olib tashlash
4. `localhost` → `db` (konteyner ichida localhost — serverning o'zi)
5. `ports: "3000"` — host porti tasodifiy bo'ladi → `"3000:3000"`
6. Volume yo'q → `pgdata:/var/lib/postgresql/data` + `volumes:` bo'limi; bonus: `depends_on` ga `condition: service_healthy` + healthcheck
</details>
