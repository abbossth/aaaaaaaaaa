# 32-dars mentor eslatmasi

- `mvp-skelet`da `package-lock.json` yo'q, shuning uchun Dockerfile'da `npm install` ishlatilgan. Jamoalar lock faylni commit qilgan bo'lsa, `npm ci --omit=dev` ga almashtiring — tezroq va aniqroq.
- `mvp-skelet` `db.json` ga yozadi. `USER node` bilan `/app` egasi `node` bo'lishi shart (`chown`), aks holda `EACCES`. Konteyner o'chsa `db.json` yo'qoladi — bu 33-darsdagi volume mavzusiga ko'prik.
- `HEALTHCHECK` da `curl` emas `wget` — Alpine'da `curl` yo'q, `wget` BusyBox'da bor.
- Docker Hub bepul akkauntda private repo cheklangan — image'lar public bo'ladi. Ichida maxfiy narsa yo'qligini tekshiring!
- Challenge'da distroless image'da `HEALTHCHECK` (wget) ishlamaydi — kuchli jamoalar buni o'zlari topsin.
