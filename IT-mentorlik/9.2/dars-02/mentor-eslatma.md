# 2-dars mentor eslatmasi

## Ko'p uchraydigan muammolar
| Muammo | Yechim |
|---|---|
| `python` topilmadi (Windows) | O'rnatishda "Add Python to PATH" belgilanmagan. Qayta o'rnatish yoki `py` buyrug'idan foydalanish |
| `python` Microsoft Store'ni ochadi | Sozlamalar → Ilovalar → "App execution aliases" dan python.exe'ni o'chirish |
| `activate` ishlamaydi: "running scripts is disabled" (PowerShell) | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` yoki terminalni **Command Prompt**/Git Bash'ga almashtirish |
| VS Code boshqa interpretatorni ishlatadi | `Ctrl+Shift+P` → "Python: Select Interpreter" → `.venv` |
| pip'da proxy/tarmoq xatosi | Mentor oldindan offline paket tayyorlab qo'yadi: `pip download rich -d paketlar/`, keyin `pip install --no-index -f paketlar rich` |

## Maslahat
Dars oldidan kamida 2 ta kompyuterda butun jarayonni sinab ko'ring. Birinchi darslarda texnik muammolar vaqtni eng ko'p yeydi.
