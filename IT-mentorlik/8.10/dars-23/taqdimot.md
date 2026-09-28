# 23-dars slaydlari: Animatsiyalar ✨

## 1-slayd
**Sahifaga jon kiritamiz — JavaScript'siz!**

## 2-slayd — transition: silliq o'tish
```css
.tugma { background: blue; transition: all 0.3s ease; }
.tugma:hover { background: purple; }
```
`0.3s` davomiylik · `ease` tezlik egri chizig'i

## 3-slayd — transform
`translateY(-10px)` ⬆️ yuqoriga siljish
`scale(1.1)` 🔍 kattalashtirish
`rotate(45deg)` 🔄 burish
Birgalikda: `transform: translateY(-5px) scale(1.05);`

## 4-slayd — @keyframes
```css
@keyframes aylan {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}
.loader { animation: aylan 1s linear infinite; }
```

## 5-slayd — animation xossalari
`animation: nom davomiylik tezlik takror yo'nalish;`
`infinite` cheksiz · `alternate` borib-qaytish · `2s` kechikish (delay) · `forwards` oxirgi holatda qolish

## 6-slayd — Me'yor ⚖️
✅ Hover effekt, yuklanish belgisi, e'tiborni tortish
❌ Hamma narsa aylanib, sakrab turishi → bosh aylanadi 😵
