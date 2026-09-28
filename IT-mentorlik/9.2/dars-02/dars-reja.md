# 2-dars. Dasturlash tillari, kompilyator va interpretator. Python o'rnatish, VS Code, venv, pip

**Guruh:** 9.2 / 9.3 | **Turi:** 📘 Mavzu | **Davomiyligi:** 80 daqiqa
**Qo'llanma:** 1-bob, "Python: o'rnatish, ilk dasturni yozish"

## Maqsad
- Dasturlash tillarining turlarini (past/yuqori darajali) va kompilyator bilan interpretator farqini tushuntira oladi.
- Python va VS Code'ni to'g'ri sozlaydi, terminaldan dastur ishga tushiradi.
- Virtual muhit (`venv`) va `pip` nima uchun kerakligini tushunadi. Birinchi tashqi kutubxonani o'rnatib ishlatadi.

## Dars rejasi

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 0–5 | **Hook** | Ekranda bir xil dastur ("Salom, dunyo!") 5 tilda: Assembly, C, Java, JavaScript, Python. *"Qaysi biri eng qisqa? Nega Python'ni back-end, AI va DevOps'da shuncha yaxshi ko'rishadi?"* |
| 5–10 | **Takrorlash** | Diagnostika natijalari va vakansiyalar tahlili (uyga vazifa) |
| 10–25 | **Yangi mavzu** | Mashina kodi → Assembly → yuqori darajali tillar. Kompilyator (butun kitobni tarjima qilib beradi) va interpretator (sinxron tarjimon). Python — interpretatsiya qilinadigan til. |
| 25–40 | **Jonli kod** | Terminal: `python --version`, `python` REPL, `python fayl.py`. VS Code: papka ochish, Python kengaytmasi, Run tugmasi. `venv` yaratish va faollashtirish, `pip install rich` |
| 40–62 | **Amaliyot** | `amaliy-topshiriq.md` |
| 62–74 | **Challenge** | `challenge.md`: "Rangli terminal" (rich kutubxonasi) |
| 74–80 | **Yakun** | XP, uyga vazifa |

## Asosiy buyruqlar (doskaga)
```bash
python --version
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
pip install rich
pip list
pip freeze > requirements.txt
deactivate
```

## Baholash (XP)
- Muhit to'liq sozlangan: +10 · Amaliyot: +5/+10/+20 · Challenge TOP-3: +30/+20/+10
