# 6-dars slaydlari: Animatsiya + Bootstrap

## 1-slayd
✨ **Sahifaga jon kiritamiz** + ⚡ **30 daqiqada sayt**

## 2-slayd — transition
```css
.btn { background: blue; transition: all 0.3s ease; }
.btn:hover { background: purple; transform: scale(1.1); }
```

## 3-slayd — transform
`translateY(-10px)` yuqoriga · `scale(1.2)` kattalashtirish · `rotate(45deg)` burish · `skew(10deg)` qiyshaytirish

## 4-slayd — @keyframes
```css
@keyframes aylan { from { transform: rotate(0); } to { transform: rotate(360deg); } }
.loader { animation: aylan 1s linear infinite; }
```

## 5-slayd — Bootstrap nima?
Tayyor CSS/JS komponentlar kutubxonasi. Twitter muhandislari yaratgan.
1 qator bilan ulanadi (CDN) — 100+ tayyor komponent.

## 6-slayd — Bootstrap grid
```html
<div class="container">
  <div class="row">
    <div class="col-12 col-md-6 col-lg-4">...</div>
  </div>
</div>
```
12 ustunli tizim. `col-md-6` = planshetdan boshlab yarim kenglik

## 7-slayd — O'zim yozaymi yoki Bootstrap?
✅ Bootstrap: tez prototip, admin panel, standart interfeys
✅ O'z CSS: noyob dizayn, yengil sayt, Figma maketi bo'yicha
💡 Bugun ko'p ishlatiladigan: **Tailwind CSS**
