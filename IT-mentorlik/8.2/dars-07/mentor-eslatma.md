# 7-dars mentor eslatmasi

## Ko'p uchraydigan muammolar
| Muammo | Yechim |
|---|---|
| Push'da parol so'raydi va o'tmaydi | VS Code'ning Source Control paneli orqali "Sign in with GitHub" qilish eng oson. Yoki Personal Access Token |
| Maktab kompyuterida boshqa birovning GitHub akkaunti saqlangan | Windows → "Credential Manager" → github.com yozuvini o'chirish. **Dars oxirida hamma log out qilsin!** |
| GitHub Pages 404 | Asosiy fayl nomi `index.html` bo'lishi kerak (katta harfsiz). Deploy 1–2 daqiqa oladi |
| CSS ishlamaydi (deploy'dan keyin) | Yo'lda katta-kichik harf farqi (`Style.css` va `style.css`) — Linux serverda muhim! |
| `rejected ... fetch first` | Repo README bilan yaratilgan. `git pull origin main --allow-unrelated-histories`, keyin push |

## Maslahat
- Netlify'ning **drag-and-drop** usuli (app.netlify.com/drop) Git'siz ham ishlaydi. Git'da qiynalayotgan o'quvchilar uchun zaxira reja, lekin keyin baribir Git'ni o'rganishsin.
- Bu dars o'quvchilar uchun juda motivatsion. Deploy qilingan barcha saytlar havolalarini `8.2/saytlar.md` fayliga yig'ib boring.
