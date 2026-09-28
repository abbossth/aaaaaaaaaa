# 20-dars slaydlari: Responsiv dizayn 📱💻

## 1-slayd
**Bitta sayt — hamma ekranlar uchun**

## 2-slayd — Nega?
Veb-saytlarga kirishlarning **yarmidan ko'pi** telefondan.
Google telefonga moslashmagan saytlarni qidiruvda pastga tushiradi.

## 3-slayd — 1-qadam: viewport
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
(VS Code'ning `!` shablonida allaqachon bor ✅)

## 4-slayd — Qat'iy emas, nisbiy
❌ `width: 1000px` → telefonga sig'maydi
✅ `max-width: 1000px; width: 100%;`
✅ Rasmlar: `img { max-width: 100%; height: auto; }`

## 5-slayd — Media query
```css
/* Avval telefon uchun (mobile-first) */
.galereya { grid-template-columns: 1fr; }

/* Planshet va undan katta */
@media (min-width: 768px) {
  .galereya { grid-template-columns: repeat(2, 1fr); }
}

/* Kompyuter */
@media (min-width: 1200px) {
  .galereya { grid-template-columns: repeat(3, 1fr); }
}
```

## 6-slayd — Breakpoint'lar
📱 < 768px · 📲 768–1199px · 💻 1200px+

## 7-slayd — Sinash
`F12` → `Ctrl+Shift+M` → iPhone, iPad, Galaxy...
