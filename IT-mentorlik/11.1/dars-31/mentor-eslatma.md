# 31-dars mentor eslatmasi

- **Dars oldidan:** maktab kompyuterlarida Docker Desktop o'rnatilganini tekshiring (Windows'da WSL2 va BIOS'da virtualizatsiya kerak). Ishlamasa — [Play with Docker](https://labs.play-with-docker.com) (har bir o'quvchiga Docker Hub akkaunti kerak).
- Image'larni oldindan yuklab qo'ying (`nginx:alpine`, `node:20-alpine`, `redis:7-alpine`, `postgres:16-alpine`) — 20 kishi bir vaqtda yuklasa, internet "o'ladi".
- Docker Hub'dan anonim yuklash limiti bor (6 soatda 100 ta pull, IP bo'yicha). Butun sinf bitta IP'da bo'lsa — `docker login` qildiring.
- Eng ko'p xato: `port is already allocated` (port band), `Cannot connect to the Docker daemon` (Docker Desktop yoqilmagan), Windows'da `$(pwd)` PowerShell'da `${PWD}` bo'ladi.
- `kod/buyruqlar.sh` ni birdaniga ishga tushirmang — u namoyish ssenariysi.
