const mahsulotlar = [
  { nom: "Redmi Note 13", kategoriya: "telefon", narx: 2_900_000, reyting: 4.7, omborda: 15 },
  { nom: "Samsung A15", kategoriya: "telefon", narx: 2_100_000, reyting: 4.5, omborda: 20 },
  { nom: "Nokia 105", kategoriya: "telefon", narx: 290_000, reyting: 4.2, omborda: 50 },
  { nom: "iPhone 15", kategoriya: "telefon", narx: 11_500_000, reyting: 4.9, omborda: 5 },
  { nom: "Lenovo IdeaPad", kategoriya: "noutbuk", narx: 6_800_000, reyting: 4.4, omborda: 7 },
  { nom: "MacBook Air M3", kategoriya: "noutbuk", narx: 15_900_000, reyting: 4.9, omborda: 3 },
  { nom: "HP 250 G9", kategoriya: "noutbuk", narx: 5_200_000, reyting: 4.1, omborda: 10 },
  { nom: "AirPods Pro", kategoriya: "quloqchin", narx: 3_100_000, reyting: 4.8, omborda: 12 },
  { nom: "JBL Tune 520", kategoriya: "quloqchin", narx: 650_000, reyting: 4.6, omborda: 30 },
  { nom: "Xiaomi Buds 5", kategoriya: "quloqchin", narx: 780_000, reyting: 4.3, omborda: 25 },
  { nom: "Apple Watch SE", kategoriya: "soat", narx: 3_400_000, reyting: 4.7, omborda: 8 },
  { nom: "Mi Band 9", kategoriya: "soat", narx: 450_000, reyting: 4.6, omborda: 40 },
];

// Javoblar (mentor uchun):
// 1. mahsulotlar.filter(m => m.kategoriya === "telefon" && m.narx < 1_000_000).map(m => m.nom)  -> ["Nokia 105"]
// 2. mahsulotlar.filter(m => m.reyting > 4.5).sort((a, b) => a.narx - b.narx)
// 3. mahsulotlar.filter(m => m.kategoriya === "noutbuk").reduce((a, b) => (a.narx > b.narx ? a : b))  -> MacBook Air M3
// 4. mahsulotlar.reduce((s, m) => s + m.narx * m.omborda, 0)
// 5. [...new Set(mahsulotlar.map(m => m.kategoriya))]
// 6. mahsulotlar.reduce((acc, m) => { acc[m.kategoriya] = (acc[m.kategoriya] || 0) + 1; return acc; }, {})
