# 4-dars slaydlari: GitHub'da jamoaviy ish

## 1-slayd
🐙 **GitHub = dasturchilar ofisi**

## 2-slayd — Local va Remote
💻 Local repo (sizning kompyuteringiz) ⇄ ☁️ Remote (`origin`, GitHub)
`git push` ⬆️ · `git pull` ⬇️ (= `fetch` + `merge`) · `git clone` 📥

## 3-slayd — "Push rejected" nega bo'ladi?
Jamoadoshingiz siz bilmagan holda remote'ga push qilgan. Git sizning o'zgarishlaringiz uning ishini o'chirib yuborishiga yo'l qo'ymaydi.
✅ Yechim: `git pull` → (konflikt bo'lsa, hal qilish) → `git push`

## 4-slayd — Yaxshi Issue anatomiyasi
**Sarlavha:** `[Bug] Login tugmasi telefonda ko'rinmaydi`
**Qadamlar:** 1. Saytni iPhone'da ochish 2. ...
**Kutilgan natija / Haqiqiy natija**
**Skrinshot** · **Label:** bug · **Assignee:** @aziz

## 5-slayd — Label'lar
🐞 bug · ✨ feature · 📄 docs · 🧹 refactor · 🟢 good first issue · 🔥 priority: high

## 6-slayd — Projects (Kanban)
Backlog → To Do → In Progress → Review → ✅ Done

## 7-slayd — Issue'ni avtomatik yopish
Commit yoki PR'da: `Closes #12` · `Fixes #7` → merge qilinganda issue avtomatik yopiladi ✨
