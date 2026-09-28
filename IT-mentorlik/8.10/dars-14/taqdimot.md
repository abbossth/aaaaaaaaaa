# 14-dars slaydlari: Box model

## 1-slayd
📦 **Sahifadagi har bir element — quti**

## 2-slayd — Box model
```
┌──────────── margin (tashqi bo'shliq) ────────────┐
│  ┌───────── border (chegara) ─────────┐          │
│  │  ┌────── padding (ichki) ──────┐   │          │
│  │  │        CONTENT (matn)       │   │          │
│  │  └─────────────────────────────┘   │          │
│  └────────────────────────────────────┘          │
└──────────────────────────────────────────────────┘
```

## 3-slayd — margin va padding
```css
padding: 20px;               /* hamma tomondan */
padding: 10px 20px;          /* tepa-past | chap-o'ng */
margin: 0 auto;              /* gorizontal markazga */
margin-top: 30px;            /* faqat tepadan */
```

## 4-slayd — box-sizing
```css
* { box-sizing: border-box; }
```
Shunda `width: 300px` = padding va border bilan birga 300px (hisoblash oson!)

## 5-slayd — Border
```css
border: 2px solid #5f3dc4;    /* qalinlik stil rang */
border-radius: 12px;          /* yumaloq burchak */
border-radius: 50%;           /* doira! */
```
Stillar: `solid` · `dashed` · `dotted` · `double`

## 6-slayd — Soya
```css
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
/*          x  y  blur  rang */
```

## 7-slayd — Background
```css
background-color: #f1f3f5;
background-image: url("rasm.jpg");
background-size: cover;
background: linear-gradient(135deg, #667eea, #764ba2);
```
