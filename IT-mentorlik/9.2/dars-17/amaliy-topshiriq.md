# 17-dars amaliy topshiriq: RPG o'yin ⚔️

## 🟢 Oson (+5 XP)
1. `kod/rpg.py` ni bir necha marta ishga tushiring. Kim ko'proq yutadi?
2. `Hayvon` → `Mushuk`, `It`, `Sigir` klasslari. Har biri `ovoz()` metodini o'zicha qaytaradi. Ro'yxatdagi hamma hayvonlarning ovozini bitta `for` bilan chiqaring (polimorfizm!).

## 🟡 O'rta (+10 XP)
3. Yangi qahramon: `Davolovchi` (har 3-yurishda o'zini +20 HP davolaydi, `max_hp` dan oshmasin).
4. `Qahramon` ga `maxsus_qobiliyat()` metodi qo'shing. Har bir klass uni o'zicha qayta yozsin.

## 🔴 Qiyin (+20 XP)
5. **Kompozitsiya:** `Qurol` klassi (`nom`, `bonus`). Qahramon qurolga **ega** (`self.qurol`). Hujum = kuch + qurol bonusi. Jang oldidan qurol tanlash.
6. **Jamoaviy jang:** 3v3. Har bir raundda tasodifiy tirik a'zo tasodifiy tirik dushmanga hujum qiladi. Jamoadagi hamma halok bo'lganda o'yin tugaydi.
