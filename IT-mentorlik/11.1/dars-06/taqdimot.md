# 6-dars slaydlari: Pull Request va Code Review

## 1-slayd
👀 **Kodni ikkinchi ko'z ko'rmaguncha — main'ga yo'q!**

## 2-slayd — PR hayotiy sikli
Branch → Push → PR ochish → Review → Tuzatishlar → Approve ✅ → Merge → Branch o'chiriladi

## 3-slayd — Yaxshi PR
**Sarlavha:** `feat(team): add member cards`
**Nima?** Jamoa a'zolari kartochkalari qo'shildi
**Nega?** Landing page'da jamoa bo'limi yo'q edi (#4)
**Qanday tekshirildi?** Chrome + iPhone SE rejimida
**Skrinshot** 📸 · `Closes #4`

## 4-slayd — Review checklist
☑️ Ishlaydimi? ☑️ Nomlar tushunarlimi? ☑️ Takrorlanish bormi?
☑️ Xavfsizlik (parol/kalit kodda qolmaganmi?) ☑️ Test/hujjat kerakmi?

## 5-slayd — Review madaniyati 🤝
Kodni tanqid qiling, odamni emas · Savol bering, buyruq bermang · Yaxshi joyni ham maqtang 👍
Prefikslar: `nit:` · `question:` · `suggestion:` · `blocker:`

## 6-slayd — Merge conflict 💥
```
<<<<<<< HEAD
<h1>Startap Inkubator</h1>
=======
<h1>IT Inkubator 2026</h1>
>>>>>>> feature/title
```
Ikki kishi bir qatorni o'zgartirgan → Git kimnikini olishni bilmaydi → **siz hal qilasiz**

## 7-slayd — Merge usullari
**Merge commit:** tarix to'liq saqlanadi · **Squash:** PR 1 ta commit'ga aylanadi (toza tarix) · **Rebase:** chiziqli tarix
Kichik jamoaga tavsiya: **Squash and merge**
