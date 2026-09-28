# 6-dars amaliy topshiriq

## 🟢 Oson (+5 XP)
Tech Lead jamoa reposiga `.github/pull_request_template.md` ni (`kod/pull_request_template.md`) qo'shadi. Buni ham PR orqali qiladi!

## 🟡 O'rta (+10 XP)
1. 5-darsda boshlagan feature branch'ingiz uchun **PR oching**: shablonni to'liq to'ldiring, reviewer sifatida jamoadoshingizni tanlang.
2. Jamoadoshingiz PR'ini review qiling: **kamida 3 ta inline komment** (biri maqtov bo'lsin 👍, biri `suggestion:`). Keyin "Approve" yoki "Request changes" bosing.
3. O'z PR'ingizdagi kommentlarga javob bering yoki tuzating, keyin **Squash and merge** qiling.

## 🔴 Qiyin (+20 XP)
4. PR'ingizni merge qilishdan oldin main o'zgarib qolgan bo'lsa, GitHub "This branch has conflicts" deydi. Lokal hal qiling:
```bash
git switch feature/mening-branchim
git pull origin main     # konflikt chiqadi
# VS Code'da: "Accept Current / Incoming / Both" yoki qo'lda tahrirlash
git add .
git commit -m "chore: resolve merge conflict with main"
git push
```
