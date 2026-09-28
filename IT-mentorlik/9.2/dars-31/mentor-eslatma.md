# 31-dars mentor eslatmasi

- Dars boshida hamma bazani **qayta yaratsin** (30-darsdagi CRUD tajribalari ma'lumotni o'zgartirgan bo'lishi mumkin).
- `buzib-kor.sql` kutilgan natijalari:
  1. `baho_oraliq` (CHECK) · 2. FK `baholar_talaba_id_fkey` · 3. `telefon_format` (CHECK) · 4. `sana_otmishda` (CHECK) · 5. NOT NULL (`ism`) · 6. UNIQUE (`sinflar_nom_key`) · 7. FK `sinflar_rahbar_id_fkey` (RESTRICT) · 8. `bir_kunda_bir_baho` (UNIQUE)
- psql'da xatodan keyin qolgan so'rovlar ham bajariladi (har biri alohida tranzaksiya) — bu challenge uchun qulay.
- 7-qadamdagi `RENAME COLUMN nom TO nomi` keyingi darslardagi so'rovlarga ta'sir qiladi. 32-dars boshida bazani yana qayta yarating.
