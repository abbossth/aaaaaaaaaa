# 16-dars slaydlari: Flexbox amaliyot

## 1-slayd
🛍 **Galereya = flex + wrap + gap**

## 2-slayd — Galereya formulasi
```css
.galereya {
  display: flex;
  flex-wrap: wrap;   /* sig'masa pastga */
  gap: 20px;
}
.karta {
  flex: 1 1 250px;   /* o'sadi | qisqaradi | asosiy kenglik */
}
```

## 3-slayd — flex: 1 1 250px nima degani?
`flex-grow: 1` — bo'sh joy bo'lsa, kengayadi
`flex-shrink: 1` — joy yetmasa, qisqaradi
`flex-basis: 250px` — boshlang'ich kenglik

## 4-slayd — Tugmani pastga yopishtirish
```css
.karta { display: flex; flex-direction: column; }
.karta .tugma { margin-top: auto; }   /* 🪄 */
```
Matn uzun yoki qisqa bo'lsa ham tugmalar bir chiziqda turadi

## 5-slayd — Alohida element
`align-self: flex-end` — faqat shu element pastga
`order: -1` — birinchi o'ringa
