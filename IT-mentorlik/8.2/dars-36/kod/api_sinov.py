"""36-dars: API bilan tanishuv — botsiz, oddiy Python'da (requests).
pip install requests
"""
import requests

# 1) Valyuta kursi — Markaziy bank (O'zbekiston)
javob = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/", timeout=10)
print("Status:", javob.status_code)          # 200 = OK
kurslar = javob.json()                        # JSON → Python ro'yxati
for k in kurslar:
    if k["Ccy"] in ("USD", "EUR", "RUB"):
        print(f"1 {k['Ccy']} = {k['Rate']} so'm")

# 2) Ob-havo — Open-Meteo (kalit kerak emas)
params = {"latitude": 41.31, "longitude": 69.28, "current": "temperature_2m,wind_speed_10m"}
havo = requests.get("https://api.open-meteo.com/v1/forecast", params=params, timeout=10).json()
print("Toshkent:", havo["current"]["temperature_2m"], "°C,", havo["current"]["wind_speed_10m"], "km/soat")
