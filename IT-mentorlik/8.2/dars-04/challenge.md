# 4-dars challenge: "Qurilmalar ruleti" 🎰

**Vaqt:** 12 daqiqa | **Format:** juftliklar

1. Mentor ekranda "ruletka"ni aylantiradi (wheelofnames.com): Galaxy Fold, iPhone SE, iPad Mini, Nest Hub, 4K monitor (DevTools'da "Edit" orqali custom 2560px qo'shiladi).
2. Juftliklar sahifani o'sha qurilmada ochadi. Agar biror narsa buzilgan bo'lsa (gorizontal scroll, sig'magan matn, cho'zilgan rasm), 3 daqiqada tuzatishi kerak.
3. 3 raund o'tkaziladi.

**Ball:** qurilmada mukammal ko'rinsa +5, tuzatib ulgursa +3.
**XP:** eng ko'p ball to'plagan juftlikka +20.

💡 Gorizontal scroll'ni topishning tezkor usuli: DevTools Console'da
```js
document.querySelectorAll('*').forEach(el => { if (el.offsetWidth > document.documentElement.offsetWidth) console.log(el); });
```
