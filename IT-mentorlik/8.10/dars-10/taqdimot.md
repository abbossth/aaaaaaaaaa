# 10-dars slaydlari: Formalar

## 1-slayd
📝 **Internetning yarmi — formalar**

## 2-slayd — Forma tuzilishi
```html
<form>
  <label for="ism">Ismingiz:</label>
  <input type="text" id="ism" name="ism" placeholder="Aziz" required>
  <button type="submit">Yuborish</button>
</form>
```

## 3-slayd — Input turlari
`text` matn · `email` email · `password` •••• · `number` son · `date` sana · `tel` telefon
`checkbox` ☑ · `radio` 🔘 · `color` 🎨 · `range` 🎚 · `file` 📎

## 4-slayd — label nega kerak?
- Label'ni bossangiz, input tanlanadi (telefonda juda qulay!)
- Ko'zi ojizlar uchun ekran o'quvchi dastur aynan label'ni o'qiydi
`<label for="email">` ↔ `<input id="email">`

## 5-slayd — Radio va checkbox
```html
<!-- Radio: faqat BITTASINI tanlash, name bir xil! -->
<input type="radio" id="ogil" name="jins"><label for="ogil">O'g'il</label>
<input type="radio" id="qiz" name="jins"><label for="qiz">Qiz</label>

<!-- Checkbox: BIR NECHTASINI tanlash -->
<input type="checkbox" id="futbol"><label for="futbol">Futbol</label>
```

## 6-slayd — Select va textarea
```html
<select id="sinf">
  <option>8.10</option>
  <option>8.2</option>
</select>
<textarea rows="4" placeholder="Izoh..."></textarea>
```

## 7-slayd — Foydali atributlar
`required` majburiy · `placeholder` ko'rsatma · `min`/`max` chegara · `maxlength` uzunlik · `checked` oldindan belgilangan
