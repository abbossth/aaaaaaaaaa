# 3-dars slaydlari: Git — vaqt mashinasi

## 1-slayd
`diplom_final_FINAL_v3_toʻgʻrisi.docx` 😱 → **Git** ✅

## 2-slayd — Git nima?
Kod tarixini saqlaydigan tizim: kim, qachon, nimani, nega o'zgartirdi.
2005-yilda Linus Torvalds Linux uchun yaratgan.

## 3-slayd — 3 hudud
📝 Working directory (tahrirlash) → 📦 Staging (`git add`) → 🗄 Repository (`git commit`)

## 4-slayd — Asosiy buyruqlar
```
git init                 git status
git add .                git commit -m "..."
git log --oneline        git diff
git switch -c feature    git merge feature
git restore fayl         git push
```

## 5-slayd — Branch = parallel olam 🌳
```
main:     A---B-------E (merge)
               \     /
feature:        C---D
```

## 6-slayd — Yaxshi commit xabari
✅ `feat: login formasini qo'shish` · `fix: parol tekshiruvidagi xato`
❌ `update` · `asdf` · `oxirgi o'zgarishlar`

## 7-slayd — README.md = loyihaning "yuzi"
Nomi · nima qiladi · skrinshot · qanday ishga tushiriladi · texnologiyalar · mualliflar

## 8-slayd — .gitignore
`node_modules/` · `.env` · `dist/` · `.DS_Store` · `*.log`
❗ **Hech qachon `.env` (parollar) ni push qilmang!**
