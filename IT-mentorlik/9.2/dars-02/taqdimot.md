# 2-dars slaydlari: Python ish muhiti

## 1-slayd — "Salom, dunyo!" 5 tilda
```c
// C
#include <stdio.h>
int main() { printf("Salom, dunyo!\n"); return 0; }
```
```java
// Java
public class Main { public static void main(String[] a) { System.out.println("Salom, dunyo!"); } }
```
```python
# Python
print("Salom, dunyo!")
```

## 2-slayd — Tillar darajalari
🔽 **Mashina kodi:** `10110000 01100001`
🔽 **Assembly:** `MOV AL, 61h`
🔼 **Yuqori daraja:** Python, JavaScript, Java, C#
Qanchalik yuqori bo'lsa, inson tiliga shunchalik yaqin.

## 3-slayd — Kompilyator va interpretator
| | Kompilyator | Interpretator |
|---|---|---|
| Analogiya | Kitobni to'liq tarjima qilib beradi | Sinxron tarjimon |
| Qachon | Ishga tushirishdan oldin | Ishlash davomida |
| Tezlik | Tezroq ishlaydi | Sekinroq, lekin qulay |
| Misollar | C, C++, Go, Rust | Python, JavaScript, PHP |

## 4-slayd — Nega Python?
✅ Oddiy sintaksis · ✅ Ulkan kutubxonalar (PyPI: 500 000+)
✅ Back-end (FastAPI, Django) · ✅ DevOps (Ansible, skriptlar) · ✅ AI (PyTorch)
Instagram, Spotify, Dropbox, YouTube back-endida Python bor

## 5-slayd — Virtual muhit (venv) 📦
Har bir loyiha — alohida "quti". Loyiha A'ga `fastapi 0.110`, loyiha B'ga `fastapi 0.95` kerak. venv'siz ular urishib qoladi.
`python -m venv .venv` → `activate` → `pip install ...`

## 6-slayd — pip = Python'ning "Play Market"i
`pip install rich` · `pip list` · `pip freeze > requirements.txt` · `pip install -r requirements.txt`
