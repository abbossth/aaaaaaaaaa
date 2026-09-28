# 16-dars mentor eslatmasi

## Ko'p uchraydigan xatolar
| Xato | Yechim |
|---|---|
| Property va atribut nomi bir xil: `self.yosh = ...` setter ichida → cheksiz rekursiya (`RecursionError`) | Ichki atributni `self._yosh` deb nomlang |
| `@yosh.setter` dan oldin `@property def yosh` yozilmagan | Avval getter, keyin setter |
| Ro'yxat property orqali qaytariladi va tashqaridan `.append` qilinadi | Nusxa yoki tuple qaytarish |

## Maslahat
"Xaker vs Himoyachi" o'quvchilarga juda yoqadi va keyinchalik (46-dars, JWT/auth) xavfsizlik fikrlashining boshlanishi bo'ladi.
