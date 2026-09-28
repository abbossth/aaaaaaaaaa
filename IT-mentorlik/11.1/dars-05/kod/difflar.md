# "Commit tarjimoni" uchun difflar

## 1
```diff
- <button class="btn">Kirish</button>
+ <button class="btn" type="submit" disabled={loading}>Kirish</button>
```
Javob: `fix(auth): disable login button while loading`

## 2
```diff
+ ## O'rnatish
+ 1. `npm install`
+ 2. `npm run dev`
```
Javob: `docs: add installation steps to README`

## 3
```diff
+ export function formatPrice(n) {
+   return n.toLocaleString("uz-UZ") + " so'm";
+ }
```
Javob: `feat(utils): add price formatter`

## 4
```diff
- const total = items.reduce((s, i) => s + i.price, 0)
+ const total = items.reduce((s, i) => s + i.price * i.qty, 0)
```
Javob: `fix(cart): include quantity in total price`

## 5
```diff
- "react": "^18.2.0"
+ "react": "^18.3.1"
```
Javob: `chore(deps): bump react to 18.3.1`
