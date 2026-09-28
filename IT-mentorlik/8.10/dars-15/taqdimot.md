# 15-dars slaydlari: Flexbox

## 1-slayd
🐸 **Flexbox — CSS'ning sehrli tayoqchasi**

## 2-slayd — Ota va bolalar
```html
<div class="konteyner">     <!-- ota: display: flex -->
  <div>1</div>             <!-- bolalar avtomatik qatorga turadi -->
  <div>2</div>
  <div>3</div>
</div>
```
```css
.konteyner { display: flex; }
```

## 3-slayd — O'qlar
```
flex-direction: row
  ──────── asosiy o'q (main axis) ────────▶
  │ [1] [2] [3]
  ▼ ko'ndalang o'q (cross axis)
```
`column` bo'lsa — o'qlar joy almashadi!

## 4-slayd — justify-content (asosiy o'q bo'yicha)
`flex-start` |123    | · `center` |  123  | · `flex-end` |    123|
`space-between` |1  2  3| · `space-around` · `space-evenly`

## 5-slayd — align-items (ko'ndalang o'q bo'yicha)
`stretch` (cho'zish) · `center` · `flex-start` · `flex-end`

## 6-slayd — Mukammal markaz 🎯
```css
.ota {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
```

## 7-slayd — Yana
`flex-wrap: wrap` — sig'masa keyingi qatorga · `gap: 20px` — bolalar orasida bo'shliq
