# 35-dars mentor eslatmasi

- Batafsil material: `../../9.2/dars-22/`.
- FSM'ni doskada **holatlar diagrammasi** sifatida chizmasdan kodga o'tmang — 8.2 uchun eng qiyin joy aynan tushunish.
- Eng ko'p xato: `set_state` unutiladi → keyingi xabar hech qaysi handler'ga tushmaydi; handler tartibi — `Command("cancel")` FSM handler'laridan **oldin** bo'lishi kerak.
- Standart `MemoryStorage` — bot qayta yoqilsa holatlar yo'qoladi. Buni aytib o'ting (Redis — keyingi yillarda).
