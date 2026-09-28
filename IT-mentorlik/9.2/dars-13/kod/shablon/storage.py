"""JSON faylga saqlash va yuklash (2-a'zo)."""
import json
from pathlib import Path

FAYL = Path(__file__).parent / "data.json"


def yuklash() -> dict:
    try:
        with open(FAYL, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"elementlar": []}


def saqlash(data: dict) -> None:
    with open(FAYL, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
