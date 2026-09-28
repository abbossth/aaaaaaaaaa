# 31-dars slaydlari: Docker 🐳

## 1-slayd
🤷 *"Mening kompyuterimda ishlaydi!"* → 🐳 *"Unda kompyuteringni jo'nat"*

## 2-slayd — Konteyner = yuk konteyneri 🚢
Ichida nima bo'lishidan qat'i nazar, hamma kemaga, poyezdga, kranga **bir xil** mos keladi.
Ilova + Node 20 + kutubxonalar + sozlamalar → **bitta paket** → istalgan serverda bir xil ishlaydi.

## 3-slayd — VM vs Konteyner
```
 Virtual mashina              Konteyner
┌──────┬──────┐           ┌──────┬──────┐
│ App  │ App  │           │ App  │ App  │
│ Libs │ Libs │           │ Libs │ Libs │
│ OS 🐢│ OS 🐢│           ├──────┴──────┤
├──────┴──────┤           │ Docker Engine│
│ Hypervisor  │           │  Host OS    │
│  Host OS    │           └─────────────┘
└─────────────┘
GB, daqiqalar              MB, soniyalar ⚡
```

## 4-slayd — Arxitektura
`docker run nginx` → **CLI** → **Docker daemon** → image bormi? yo'q → **Docker Hub**'dan `pull` → container yaratadi → ishga tushiradi

## 5-slayd — Image vs Container
| Image 📀 | Container ▶️ |
|---|---|
| Qolip (klass) | Ishlayotgan nusxa (obyekt) |
| Faqat o'qiladi | Ustiga yoziladigan qatlam bor |
| `docker images` | `docker ps` |
| Bitta image → ko'p container | O'chirsa — ichidagi o'zgarishlar yo'qoladi! |

## 6-slayd — Qatlamlar (layers) 🥞
```
[ app kodi      ]  ← 50 KB  (tez-tez o'zgaradi)
[ npm paketlar  ]  ← 30 MB
[ node:20       ]  ← 130 MB (keshda turadi)
[ debian/alpine ]
```
Bir xil qatlamlar **qayta ishlatiladi** → tez yuklanadi, joy tejaladi

## 7-slayd — Asosiy buyruqlar
```bash
docker run -d -p 8080:80 --name veb nginx   # fon rejimida, port 8080 → 80
docker ps            # ishlayotganlar (-a: hammasi)
docker logs veb      # loglar (-f: jonli)
docker exec -it veb sh   # ichiga kirish
docker stop veb && docker rm veb
docker images / docker rmi nginx
```

## 8-slayd — Port mapping
`-p 8080:80` = **HOST:CONTAINER** → brauzerda `localhost:8080` → konteynerning 80-porti
