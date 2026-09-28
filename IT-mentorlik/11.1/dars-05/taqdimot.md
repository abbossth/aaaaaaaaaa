# 5-dars slaydlari: Branching va Conventional Commits

## 1-slayd
`asdf` 🆚 `feat(auth): add login form` — qaysi biri professional?

## 2-slayd — GitHub Flow (tavsiya: kichik jamoalar uchun ✅)
```
main ──●────────●────────●──
        \      /  \     /
feature  ●──●─●    ●───●
```
main doim ishlaydigan holatda · har bir vazifa — alohida branch · PR orqali merge

## 3-slayd — Git Flow (katta, reliz'li loyihalar)
`main` (production) · `develop` · `feature/*` · `release/*` · `hotfix/*`

## 4-slayd — Trunk-based
Hamma kichik o'zgarishlarni kuniga bir necha marta main'ga qo'shadi. Kuchli CI va feature flag'lar talab qiladi (Google, Meta)

## 5-slayd — Branch nomlash
`feature/login-form` · `fix/navbar-mobile` · `docs/readme-install` · `hotfix/payment-crash` · `refactor/api-client`

## 6-slayd — Conventional Commits
```
<tur>(<soha>): <qisqa tavsif>

feat(auth): add Google login
fix(cart): correct total price rounding
docs: update install instructions
refactor(api): extract fetch helper
test(auth): add login validation tests
chore: bump dependencies
```
Afzalliklari: avtomatik CHANGELOG, versiyalash (semver), tarixni o'qish oson

## 7-slayd — Atomic commit
✅ 1 commit = 1 mantiqiy o'zgarish
❌ "login + dizayn + bug fix + README" bitta commit'da
💡 `git add -p` — faylning faqat bir qismini qo'shish

## 8-slayd — Branch protection
Settings → Branches → main:
✅ Require pull request before merging · ✅ Require approvals (1) · ✅ Require status checks (keyinroq, CI bilan)
