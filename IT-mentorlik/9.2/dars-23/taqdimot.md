# 23-dars slaydlari: Bot + API 🌐

## 1-slayd
**Bot internetning istalgan ma'lumotini olib keladi**

## 2-slayd — Nega aiohttp?
`requests.get()` — **sinxron**: bot javob kutayotganda BOSHQA HAMMA foydalanuvchilar "muzlab" turadi 🥶
`aiohttp` — **asinxron**: kutish vaqtida bot boshqalarga javob beradi ✅

## 3-slayd — So'rov
```python
import aiohttp

async def kurs_ol() -> list[dict]:
    url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(url) as resp:
            resp.raise_for_status()
            return await resp.json(content_type=None)
```

## 4-slayd — Xatolarni ushlash
```python
try:
    data = await kurs_ol()
except (aiohttp.ClientError, TimeoutError):
    await message.answer("😔 Server javob bermadi, keyinroq urinib ko'ring")
    return
```

## 5-slayd — Keshlash 🗄
Har bir foydalanuvchi uchun Markaziy bankka so'rov yuborish shart emas: kurs kuniga bir marta o'zgaradi!
```python
kesh = {"vaqt": 0, "data": None}
if time.time() - kesh["vaqt"] > 1800:   # 30 daqiqa
    kesh.update(vaqt=time.time(), data=await kurs_ol())
```

## 6-slayd — Foydali bepul API'lar
🌤 open-meteo.com (ob-havo, kalitsiz) · 💱 cbu.uz (valyuta) · 📖 api.dictionaryapi.dev (lug'at) · 🌍 restcountries.com · 😂 official-joke-api.appspot.com
