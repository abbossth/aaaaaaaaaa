# 18-dars slaydlari: Pseudo va Position

## 1-slayd
📌 **Nega menyu "yopishib" turadi?**

## 2-slayd — Pseudo-class (holat)
```css
a:hover { color: red; }            /* sichqoncha ustida */
input:focus { border-color: blue; } /* tanlanganda */
button:active { transform: scale(0.95); } /* bosilganda */
tr:nth-child(even) { background: #f1f3f5; } /* juft qatorlar */
li:first-child { font-weight: bold; }
```

## 3-slayd — Pseudo-element (qism)
```css
.yangi::before { content: "🔥 "; }
h2::after { content: ""; display: block; width: 50px; height: 3px; background: purple; }
::selection { background: yellow; }
input::placeholder { color: #aaa; }
```

## 4-slayd — Position
| Qiymat | Nima qiladi |
|---|---|
| `static` | Oddiy (standart) |
| `relative` | O'z joyiga nisbatan siljiydi; absolute bolalar uchun "yakor" |
| `absolute` | Eng yaqin `relative` otaga nisbatan |
| `fixed` | Ekranga nisbatan: aylantirganda ham joyida |
| `sticky` | Aylantirganda ma'lum joyga yetib, "yopishadi" |

## 5-slayd — Oltin qoida
```css
.karta { position: relative; }          /* ota */
.yorliq { position: absolute; top: 10px; right: 10px; }   /* bola */
```

## 6-slayd — Sticky menyu va fixed tugma
```css
header { position: sticky; top: 0; z-index: 10; }
.yuqoriga { position: fixed; bottom: 20px; right: 20px; }
```
`z-index` — kim ustida turadi (katta raqam — yuqorida)
