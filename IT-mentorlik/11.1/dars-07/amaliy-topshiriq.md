# 7-dars 2-raund: "Git qutqaruv xizmati" 🚑

**Vaqt:** 25 daqiqa | **Format:** juftlik

Har bir holatni `kod/qutqaruv.sh` bilan tayyorlang (skript har bir holat uchun alohida papka yaratadi), keyin muammoni hal qiling. Har biri +5 XP.

| № | Holat | Maqsad |
|---|---|---|
| 1 | `index.html` buzilgan (commit qilinmagan) | Oxirgi commit holatiga qaytaring |
| 2 | Oxirgi commit xabari: `asdf` | Uni `docs: add readme` ga o'zgartiring |
| 3 | Oxirgi 2 ta commit xato edi | Ularni bekor qiling, lekin o'zgarishlar fayllarda qolsin |
| 4 | Siz `feature` branch'da ishlayapsiz, commit qilinmagan o'zgarishlar bor. Main'dagi shoshilinch xatoni tuzatish kerak | `stash` → `main` → tuzatish → commit → `feature` ga qaytish → `stash pop` |
| 5 | `git reset --hard HEAD~3` qilinib, 3 ta commit "yo'qolgan" | `reflog` orqali qaytaring |
| 6 | Xato commit allaqachon "push qilingan" (deb faraz qilamiz) | Tarixni buzmasdan bekor qiling |

---
Javoblar: 1) `git restore index.html` · 2) `git commit --amend -m "docs: add readme"` · 3) `git reset --soft HEAD~2` · 4) `git stash; git switch main; ...; git switch feature; git stash pop` · 5) `git reflog`, keyin `git reset --hard HEAD@{1}` (yoki kerakli hash) · 6) `git revert HEAD`
