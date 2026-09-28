# 3-dars mentor eslatmasi

## Ko'p uchraydigan muammolar
| Muammo | Yechim |
|---|---|
| `Author identity unknown` | `git config --global user.name "Ism"` va `user.email` |
| Push'da parol so'raydi va o'tmaydi | GitHub parol bilan push'ni qabul qilmaydi. **Personal Access Token** yoki **GitHub Desktop / VS Code** orqali login qiling |
| `git switch` topilmadi | Eski Git versiyasi. `git checkout -b` ishlating yoki Git'ni yangilang |
| Vim ochilib qoldi (merge commit xabari) | `Esc`, keyin `:wq` va Enter. Kelajakda: `git config --global core.editor "code --wait"` |
| Maktab kompyuterida boshqa birovning GitHub akkaunti saqlanib qolgan | Windows "Credential Manager" → github.com yozuvini o'chirish |

## Maslahat
- `challenge-setup.sh` ni dars oldidan bir marta ishga tushirib tekshiring.
- 11.1 Git'ni biladi, lekin odatda faqat `add/commit/push` darajasida. `branch/merge/log/show` ular uchun yangilik bo'ladi, shuni ta'kidlang.
