# 33-dars. Docker network, volume va Docker Compose (server + PostgreSQL)

**Guruh:** 11.1 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** II bob, "Docker Compose yordamida ko'p konteynerli ilovalar"

## Maqsad
- Docker tarmoqlari: bridge network, konteynerlar bir-birini **xizmat nomi** bilan topishi (ichki DNS).
- Ma'lumotni saqlash: named volume va bind mount farqi; konteyner "bir martalik", volume — "doimiy".
- `docker-compose.yml`: `services`, `image`/`build`, `environment`, `ports`, `volumes`, `depends_on` + `healthcheck`, `restart`.
- `docker compose up -d --build / ps / logs / exec / down (-v)`.
- `.env` orqali parollarni compose faylidan tashqarida saqlash.
- **Jamoa natijasi:** MVP (server + PostgreSQL) bitta `docker compose up` bilan ko'tariladi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | 32-darsdagi konteynerni o'chirib qayta yoqamiz — `db.json`dagi hamma ma'lumot yo'q 😱. *"Real startap buni ko'tara olmaydi"* |
| 5–10 | **Takrorlash** | "Eng kichik image" g'olibi, 32-dars testi |
| 10–25 | **Yangi mavzu** | `taqdimot.md`: network → volume → compose |
| 25–40 | **Jonli** | `kod/buyruqlar.sh`: 1–2 qism (network, volume) — keyin 3-qism (compose) bilan bir xil natija 1 buyruqda |
| 40–65 | **Jamoaviy amaliyot** | `amaliy-topshiriq.md`: MVP'ni Compose'ga o'tkazish |
| 65–75 | **Challenge** | `challenge.md`: "Compose-doktor" 🩺 |
| 75–80 | **Yakun** | XP, uyga vazifa. Keyingi dars — CI 🤖 |

## Baholash (XP)
- `docker compose up` bilan ishlaydigan MVP +15 · Amaliyot +5/+10/+20 · Challenge: har bir topilgan xato +4
