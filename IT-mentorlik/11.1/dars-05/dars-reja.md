# 5-dars. Branching strategiyalari (feature/release/hotfix), conventional commits

**Guruh:** 11.1 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** I bob, "Branching, Pull Request va code review metodologiyasi"

## Maqsad
- GitHub Flow, Git Flow va Trunk-based development farqini biladi va jamoasi uchun mosini tanlaydi.
- Branch nomlash qoidalarini (`feature/login-form`, `fix/navbar-mobile`, `hotfix/...`) qo'llaydi.
- Conventional Commits formatida yozadi: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`.
- Kichik, maqsadli (atomic) commit'lar qiladi va branch himoyasini (branch protection) sozlaydi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Ikki repo tarixi yonma-yon: biri `update`, `fix`, `asdf`, `oxirgi`; ikkinchisi `feat(auth): add login form`, `fix(nav): close menu on mobile`. *"Qaysi loyihada 6 oydan keyin xatoni topish osonroq? Qaysi jamoaga ishga kirishni xohlaysiz?"* |
| 5–10 | **Takrorlash** | 4-dars testi |
| 10–25 | **Yangi mavzu** | 3 ta branching strategiyasi (sxemalar). Branch nomlash. Conventional Commits. Atomic commit. `git add -p` (qisman qo'shish) |
| 25–35 | **Jonli demo** | `kod/demo.sh`: GitHub Flow bo'yicha feature → commit'lar → push. Branch protection sozlamasi |
| 35–60 | **Amaliyot** | `amaliy-topshiriq.md` |
| 60–74 | **Challenge** | `challenge.md`: "Commit tarjimoni" |
| 74–80 | **Yakun** | Jamoalar o'z "Git qoidalari"ni `CONTRIBUTING.md` ga yozadi. Uyga vazifa |

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +20/+10/+5
