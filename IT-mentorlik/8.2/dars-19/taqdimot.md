# 19-dars slaydlari: To-Do ilova

## 1-slayd
✅ **Birinchi haqiqiy ilova**

## 2-slayd — Arxitektura
```
  todos = [...]   ← STATE (haqiqat manbai)
       │
   render()       ← ekranni state'dan chizish
       │
     DOM
       │
  foydalanuvchi harakati → state'ni o'zgartir → save() → render()
```

## 3-slayd — Todo obyekti
```js
{ id: 1727712345678, matn: "Uy vazifasi", bajarildi: false }
```
`id: Date.now()` — oddiy noyob ID

## 4-slayd — Saqlash va yuklash
```js
const save = () => localStorage.setItem("todos", JSON.stringify(todos));
let todos = JSON.parse(localStorage.getItem("todos")) || [];
```

## 5-slayd — Validatsiya
```js
const matn = input.value.trim();
if (matn.length < 2) return showError("Kamida 2 ta belgi");
if (todos.some((t) => t.matn.toLowerCase() === matn.toLowerCase())) return showError("Bu vazifa allaqachon bor");
```

## 6-slayd — Event delegation
```js
list.addEventListener("click", (e) => {
  const id = Number(e.target.closest("li")?.dataset.id);
  if (e.target.matches(".delete")) remove(id);
  if (e.target.matches(".toggle")) toggle(id);
});
```
