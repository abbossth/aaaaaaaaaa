# 22-dars slaydlari: Maketdan kodga 🎨→💻

## 1-slayd
**Chizgan maketingiz bugun "jonlanadi"!**

## 2-slayd — 5 qadamli algoritm
1️⃣ Maketni **bo'limlarga** ajrat (header, hero, features, footer)
2️⃣ Har bir bo'lim uchun **semantik HTML** skeletini yoz (hali CSS'siz!)
3️⃣ **Ranglar va shriftlarni** `:root` ga yoz
4️⃣ Har bir bo'limni **tepadan pastga** CSS bilan qur (Flex/Grid)
5️⃣ **Telefonda** tekshir va moslashtir

## 3-slayd — Figma → CSS
Elementni tanlang → o'ng panel → **Inspect** (yoki Dev Mode):
```css
width: 320px;
padding: 24px;
gap: 16px;
border-radius: 16px;
background: #FFFFFF;
font-family: Poppins;
font-size: 18px;
```

## 4-slayd — CSS o'zgaruvchilari
```css
:root {
  --asosiy: #5f3dc4;
  --urgu: #fcc419;
  --fon: #f8f9fa;
}
.tugma { background: var(--asosiy); }
```
Rangni bir joyda o'zgartirsangiz — hamma joyda o'zgaradi ✨

## 5-slayd — Auto Layout → Flexbox
Figma: horizontal, spacing 16, padding 24 → CSS: `display: flex; gap: 16px; padding: 24px;`

## 6-slayd — ❌ Taqiqlangan!
Figma'dagi `position: absolute; left: 324px; top: 812px;` ni ko'chirmang!
Faqat Flex va Grid bilan quring.
