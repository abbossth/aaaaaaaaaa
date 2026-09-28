# 11-dars slaydlari: Semantik HTML va media

## 1-slayd
📰 **Sahifa = gazeta**

## 2-slayd — div vs semantik
```html
<!-- ❌ -->
<div class="top"><div class="menu">...</div></div>
<!-- ✅ -->
<header><nav>...</nav></header>
```

## 3-slayd — Sahifa xaritasi
```
┌──────────── header ────────────┐
│ logo          nav (menyu)      │
├────────────── main ────────────┤
│ section           │ aside      │
│  article          │ (yon panel)│
│  article          │            │
├──────────── footer ────────────┤
└────────────────────────────────┘
```

## 4-slayd — Nega muhim?
🔍 Google sahifani yaxshiroq tushunadi (SEO)
🦯 Ko'zi ojizlar ekran o'quvchi bilan saytda yura oladi
👩‍💻 Kodni o'qish oson

## 5-slayd — figure
```html
<figure>
  <img src="samarqand.jpg" alt="Registon">
  <figcaption>Registon maydoni, Samarqand</figcaption>
</figure>
```

## 6-slayd — Video va audio
```html
<video src="video.mp4" controls width="400"></video>
<audio src="qoshiq.mp3" controls></audio>
```
`controls` tugmalar · `autoplay muted` avtomatik (ovozsiz) · `loop` takror

## 7-slayd — iframe: boshqa saytni joylash
YouTube → Share → **Embed** → kodni nusxalash
Google Maps → Share → **Embed a map** → kodni nusxalash
