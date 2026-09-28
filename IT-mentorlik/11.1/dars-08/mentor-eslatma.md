# 8-dars mentor eslatmasi

## Ko'p uchraydigan muammolar
| Muammo | Yechim |
|---|---|
| `Cannot use import statement outside a module` | package.json'ga `"type": "module"` |
| `chalk` v5 `require` bilan ishlamaydi | chalk 5 faqat ESM. `import` ishlating |
| PowerShell'da `npm` skriptlari bloklangan | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` yoki Git Bash/CMD |
| `npm install` sekin yoki maktab proxy'si | Mentor oldindan `node_modules` ni fleshkada tayyorlab qo'yadi |

## Maslahat
- Bu dars keyingi barcha darslarning asosi: Clean Code, testlar, Express va Docker'da hammasi Node'da bo'ladi. O'quvchilarning hammasida Node va npm ishlashiga ishonch hosil qiling.
- Python'ni bilishni xohlaydigan kuchli o'quvchilarga: *"Qo'llanmadagi misollar Python'da. Xohlasangiz, har bir mavzuni ikki tilda qilib ko'ring (+10 XP)."*
