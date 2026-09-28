# 36-dars slaydlari: Bot + API 🌐

## 1-slayd
💱 Dollar qancha? 🌦 Ertaga yomg'ir yog'adimi? — **Bot biladi!**

## 2-slayd — API = ofitsiant 🧑‍🍳
Siz (bot) → **so'rov** (URL) → ofitsiant (API) → oshxona (server) → **javob** (JSON)

## 3-slayd — Brauzerda sinab ko'ring
`https://cbu.uz/uz/arkhiv-kursov-valyut/json/`
```json
[{"Ccy": "USD", "Rate": "12650.50", "CcyNm_UZ": "AQSH dollari", ...}, ...]
```

## 4-slayd — Python: requests
```python
import requests
kurslar = requests.get(URL, timeout=10).json()
usd = next(k for k in kurslar if k["Ccy"] == "USD")
print(usd["Rate"])
```

## 5-slayd — Botda: aiohttp (asinxron)
```python
async with aiohttp.ClientSession() as session:
    async with session.get(URL) as resp:
        data = await resp.json()
```
❓ Nega `requests` emas? — `requests` kutayotganda **butun bot to'xtaydi**, boshqa foydalanuvchilar javob olmaydi

## 6-slayd — Buyruq argumentlari
```python
@dp.message(Command("kurs"))
async def kurs(message: Message, command: CommandObject):
    # /kurs USD 100 → command.args == "USD 100"
    valyuta, summa = command.args.split()
```

## 7-slayd — Xatolarni ushlash 🛡
```python
try:
    data = await get_json(URL)
except (aiohttp.ClientError, TimeoutError):
    await message.answer("😔 Xizmat vaqtincha ishlamayapti")
```
API — **boshqa odamning** serveri. U istalgan payt ishlamay qolishi mumkin!
