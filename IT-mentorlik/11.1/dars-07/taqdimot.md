# 7-dars slaydlari: Git qutqaruv xizmati 🚑

## 1-slayd
😱 "Men hammasini o'chirib yubordim!" → 😌 `git reflog`

## 2-slayd — Branch = ko'rsatkich
Branch — bu commit'ga yopishtirilgan stiker. HEAD — "siz hozir qayerdasiz" stikeri.

## 3-slayd — Qutqaruv jadvali
| Holat | Yechim |
|---|---|
| Faylni buzdim, hali commit qilmadim | `git restore fayl` |
| `add` qildim, lekin staging'dan olmoqchiman | `git restore --staged fayl` |
| Oxirgi commit xabari noto'g'ri | `git commit --amend -m "..."` (faqat push qilinmagan bo'lsa!) |
| Oxirgi commit'ni bekor qilaman, o'zgarishlar qolsin | `git reset --soft HEAD~1` |
| Push qilingan commit'ni bekor qilish | `git revert <hash>` (yangi "teskari" commit) |
| Tugallanmagan ishni vaqtincha chetga qo'yish | `git stash` → `git stash pop` |
| `reset --hard` qilib, hammasini yo'qotdim | `git reflog` → `git reset --hard <hash>` |

## 4-slayd — ⚠️ Oltin qoida
**Push qilingan tarixni qayta yozmang** (`reset`, `amend`, `rebase`), boshqalarning ishi buziladi. Push qilingan bo'lsa → `revert`.
