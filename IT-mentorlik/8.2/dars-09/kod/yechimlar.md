# CSS Battle namuna yechimlari (mentor uchun)

Yechimlar qisqalik uchun emas, **tushunarlilik** uchun yozilgan. Rang kodlarini target sahifasidan tekshiring.

## #2 Carrom
```html
<style>
  body { margin: 0; background: #62374e; }
  div { position: absolute; width: 50px; height: 50px; background: #fdc57b; }
  .a { top: 50px; left: 50px; }
  .b { top: 50px; right: 50px; }
  .c { bottom: 50px; left: 50px; }
  .d { bottom: 50px; right: 50px; }
</style>
<div class="a"></div><div class="b"></div><div class="c"></div><div class="d"></div>
```
Qisqaroq g'oya: bitta div + `box-shadow` bilan 3 ta nusxa.

## #3 Push Button
G'oya: markazda katta oval (to'rtburchak + `border-radius`), uning ichida ikkita doira (tashqi halqa va ichki tugma). `display: grid; place-items: center;` bilan markazlash.

## #5 Acid Rain
G'oya: 3 ta shakl. Har biri `border-radius` bilan bitta burchagi o'tkir qoldirilgan tomchi (masalan, `border-radius: 50% 0 50% 50%`) va ular ustma-ust joylashtiriladi.

## #7 Leafy Trail
G'oya: bir xil bargsimon shakl (`border-radius: 150px 0`) uch marta, har biri 50px o'ngga siljigan holda. Nusxalarni `box-shadow` bilan yaratish mumkin.
