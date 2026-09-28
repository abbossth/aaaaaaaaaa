-- 31-dars: "Bazani buzib ko'r" — har biri XATO berishi kerak. Qaysi constraint ushladi?
INSERT INTO baholar (talaba_id, fan, baho) VALUES (1, 'Tarix', 7);                  -- 1
INSERT INTO baholar (talaba_id, fan, baho) VALUES (99, 'Tarix', 5);                 -- 2
INSERT INTO talabalar (ism, telefon) VALUES ('Test', '901234567');                  -- 3
INSERT INTO talabalar (ism, tugilgan_sana) VALUES ('Kelajak', '2090-01-01');        -- 4
INSERT INTO talabalar (ism) VALUES (NULL);                                          -- 5
INSERT INTO sinflar (nom) VALUES ('9.2');                                           -- 6
DELETE FROM oqituvchilar WHERE id = 1;                                              -- 7
INSERT INTO baholar (talaba_id, fan, baho, sana) VALUES (1, 'Informatika', 4, '2026-10-01'); -- 8
