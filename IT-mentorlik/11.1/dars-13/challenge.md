# 13-dars challenge: "Jonli chat simulyatsiyasi" 💬

**Vaqt:** 14 daqiqa | **Format:** jamoalar

`EventEmitter` asosida terminal chat xonasi simulyatsiyasini yozing:

```js
const room = new ChatRoom("11.1-sinf");
const aziz = new User("Aziz");
const malika = new User("Malika");

aziz.join(room);
malika.join(room);
aziz.say("Salom hammaga!");      // Malika ko'radi: [11.1-sinf] Aziz: Salom hammaga!
malika.leave();
aziz.say("Malika ketdimi?");      // hech kim ko'rmaydi
```

## Talablar
- Foydalanuvchi o'z xabarini **o'zi ko'rmasin**
- `join`/`leave` haqida hammaga tizim xabari: `🟢 Malika qo'shildi`
- **Bonus (+10):** `@Aziz` bilan shaxsiy eslatma, faqat Aziz uchun 🔔 belgisi bilan

**XP:** ishlaydigan birinchi 3 jamoa: 🥇 +20 · 🥈 +10 · 🥉 +5
