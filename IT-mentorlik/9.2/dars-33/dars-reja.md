# 33-dars. JOIN: INNER, LEFT, RIGHT — jadvallarni birlashtirish

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 3-bob, "Jadvallarni birlashtirish (JOIN)"

## Maqsad
- Nega ma'lumot bir nechta jadvalga bo'linishini (normalizatsiya, 28-dars) va JOIN ularni qanday qayta birlashtirishini tushunadi.
- `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN` (`FULL JOIN` bilan tanishuv) farqini Venn diagrammasida va natijada ko'radi.
- Jadval taxalluslari (`t`, `s`), 3–4 jadvalli JOIN, many-to-many (`azolik`) orqali JOIN.
- `LEFT JOIN ... WHERE ... IS NULL` bilan "yo'qlarni" topadi. JOIN + GROUP BY bilan hisobot yozadi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | 32-dars hisoboti: `talaba_id = 5 → 2.50`. *"Direktor: 5 kim?! Ism kerak!"* |
| 5–10 | **Takrorlash** | 32-dars testi |
| 10–30 | **Yangi mavzu** | `taqdimot.md`: "Jonli JOIN" o'yini (pastda) + Venn diagrammalari |
| 30–55 | **Jonli + amaliyot** | `kod/join.sql`, keyin `amaliy-topshiriq.md` |
| 55–72 | **Challenge** | `challenge.md`: "JOIN detektiv" — keyingi darsdagi SQL Murder Mystery'ga razminka |
| 72–80 | **Yakun** | XP, uyga vazifa, Murder Mystery e'loni 🔍 |

### "Jonli JOIN" o'yini (5 daqiqa)
Yarim sinf — "talabalar" (qo'lida `sinf_id` yozilgan qog'oz), yarmi — "sinflar" (qo'lida `id` va nom). Mentor buyuradi: **INNER JOIN** — juftini topganlar qo'l ushlashadi. **LEFT JOIN** — "talabalar" hammasi qoladi, jufti yo'qlar yolg'iz turadi (NULL). Sinfga ataylab `sinf_id` si yo'q 1 ta talaba va talabasiz 1 ta sinf qo'shing.

## Baholash (XP)
- Amaliyot +5/+10/+20 · JOIN detektiv 🥇 +20 · 🥈 +10 · 🥉 +5
