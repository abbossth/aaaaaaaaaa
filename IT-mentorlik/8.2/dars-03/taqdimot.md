# 3-dars slaydlari: CSS — Flexbox va Grid

## 1-slayd
**CSS: Flex va Grid olimpiadasi** 🐸🥕

## 2-slayd — Selektorlar
`p` teg · `.card` class · `#logo` id · `nav a` ichidagi · `a:hover` holat · `*` hammasi

## 3-slayd — Box model
```
margin (tashqi)
  border (chegara)
    padding (ichki)
      content (kontent)
```
`box-sizing: border-box;` — o'lchamni to'g'ri hisoblash uchun

## 4-slayd — Flexbox 🐸 (bir o'lchamli: qator YOKI ustun)
```css
.container {
  display: flex;
  flex-direction: row;          /* row | column */
  justify-content: center;      /* asosiy o'q bo'yicha */
  align-items: center;          /* ko'ndalang o'q bo'yicha */
  flex-wrap: wrap;              /* sig'masa keyingi qatorga */
  gap: 16px;
}
```

## 5-slayd — Grid 🥕 (ikki o'lchamli: qator VA ustun)
```css
.gallery {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}
.big { grid-column: span 2; }
```

## 6-slayd — Qachon qaysi biri?
Menyu, tugmalar qatori, markazga qo'yish → **Flex**
Galereya, kartochkalar to'ri, sahifa maketi → **Grid**
