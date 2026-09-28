# 6-dars. Pull Request, code review, merge conflict

**Guruh:** 11.1 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** I bob, "Branching, Pull Request va code review metodologiyasi"

## Maqsad
- Sifatli PR ochadi: What/Why/How shabloni, checklist, skrinshot, `Closes #N`.
- Code review qiladi: inline komment, "Request changes" / "Approve", konstruktiv feedback.
- Merge conflict'ni tushunadi va hal qiladi (VS Code va qo'lda).
- Merge usullarini biladi: merge commit, squash, rebase.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Statistika: Google'da har bir kod o'zgarishi kamida bitta boshqa dasturchi tomonidan review qilinadi. *"Code review — xatolarni topishning eng arzon usuli. Va eng yaxshi o'qituvchi."* |
| 5–10 | **Takrorlash** | 5-dars testi |
| 10–22 | **Yangi mavzu** | PR anatomiyasi (shablon). Review madaniyati: kodni tanqid qil, odamni emas. Konflikt markerlari `<<<<<<< ======= >>>>>>>` |
| 22–45 | **Amaliyot 1** | PR ochish va juftlikda review (`amaliy-topshiriq.md`) |
| 45–70 | **Challenge** | `challenge.md`: "Konflikt jangi" |
| 70–80 | **Yakun** | Birinchi "real" PR'lar merge qilinadi 🎉. Uyga vazifa |

## Review feedback formulasi (doskaga)
❌ "Bu kod yomon."
✅ "Bu yerda `data` o'rniga `userList` deb nomlasak, tushunish osonroq bo'ladi. Nima deysiz?"
**Prefikslar:** `nit:` (mayda, majburiy emas) · `question:` · `suggestion:` · `blocker:` (tuzatilmasa merge bo'lmaydi)

## Baholash (XP)
- PR shablon bo'yicha +10 · Har bir sifatli review komment +2 (max 10) · Konflikt hal qilindi +10 · Challenge +30/+20/+10
