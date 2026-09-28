# 14-dars mentor eslatmasi

## Ko'p uchraydigan xatolar
| Xato | Yechim |
|---|---|
| Funksiya `console.log` qiladi, lekin `return` qilmaydi | Testlarda `undefined` chiqadi: `return` va `log` farqini ko'rsating |
| Arrow funksiyada `{}` bilan `return` unutilgan: `(x) => { x * 2 }` | Figurali qavs bo'lsa, `return` majburiy |
| `import` ishlamaydi: "Cannot use import statement outside a module" | `<script type="module">` va Live Server orqali ochish (fayl sifatida `file://` ochilsa, modul ishlamaydi) |

## Maslahat
`testlar.html` — TDD'ga oson kirish. O'quvchilar "qizil → yashil" jarayonini juda yoqtiradi. Keyingi darslarda ham shunday test sahifalaridan foydalanish mumkin.
