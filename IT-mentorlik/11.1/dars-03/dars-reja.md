# 3-dars. Git qayta: commit, branch, merge, README, .gitignore

**Guruh:** 11.1 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** I bob, "Versiyalarni boshqarish tizimlari (Git/GitHub)"

## Maqsad
- Git'ning 3 hududini (working directory → staging → repository) tushunadi.
- `init, status, add, commit, log, diff, branch, switch, merge, restore` buyruqlarini ishonch bilan ishlatadi.
- Sifatli README.md va .gitignore yozadi.
- Jamoa reposini yaratadi, unda har bir a'zo kamida bitta commit qiladi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | *"Tasavvur qiling: `diplom_final_FINAL_v3_toʻgʻrisi.docx`. Tanishmi?"* 😄 *"Git — bu muammoning professional yechimi. Linux yadrosini 20 000+ dasturchi aynan Git bilan yozadi."* |
| 5–10 | **Takrorlash** | 2-dars testi |
| 10–25 | **Yangi mavzu** | 3 hudud (rasm), commit = "o'yindagi save point", branch = "parallel olam", merge. Jonli demo: `kod/git-demo.sh` |
| 25–55 | **Amaliyot** | `amaliy-topshiriq.md` (individual, keyin jamoaviy) |
| 55–70 | **Challenge** | `challenge.md`: "Git vaqt mashinasi" |
| 70–80 | **Yakun** | Jamoa repolarini ekranda ko'rish, XP, uyga vazifa |

## Git hududlari (doskaga)
```
Working dir  --git add-->  Staging  --git commit-->  Repository  --git push-->  GitHub
     ^                                                    |
     +------------------ git restore / switch ------------+
```

## Baholash (XP)
- Amaliyot +5/+10/+20 · Challenge +30/+20/+10 · Jamoa reposida commit +5
