# 9-dars slaydlari: Ro'yxatlar va jadvallar

## 1-slayd
📋 **Ro'yxat** va 📊 **Jadval** — ma'lumotni tartiblash

## 2-slayd — Tartibsiz ro'yxat
```html
<ul>
  <li>Non</li>
  <li>Sut</li>
</ul>
```
• Non • Sut

## 3-slayd — Tartibli ro'yxat
```html
<ol>
  <li>Suvni qaynat</li>
  <li>Choy sol</li>
</ol>
```
`<ol type="A">` → A, B, C · `<ol start="5">` → 5, 6, 7

## 4-slayd — Ichma-ich ro'yxat
```html
<ul>
  <li>Mevalar
    <ul><li>Olma</li><li>Nok</li></ul>
  </li>
</ul>
```

## 5-slayd — Jadval tuzilishi
```html
<table border="1">
  <caption>Dars jadvali</caption>
  <thead>
    <tr><th>Kun</th><th>1-dars</th></tr>
  </thead>
  <tbody>
    <tr><td>Dushanba</td><td>Matematika</td></tr>
  </tbody>
</table>
```
`tr` — qator (table row) · `th` — sarlavha katak · `td` — katak (table data)

## 6-slayd — Kataklarni birlashtirish
`colspan="2"` → 2 ustunni egallaydi ↔
`rowspan="2"` → 2 qatorni egallaydi ↕
