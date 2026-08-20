"""Сохранение тестовых данных в JSON и CSV."""

import csv
import json
from pathlib import Path


def save_to_json(users: list[dict[str, str]], filename: str) -> Path:
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=2)
    return path


def save_to_csv(users: list[dict[str, str]], filename: str) -> Path:
    if not users:
        raise ValueError("Нельзя сохранить пустой список")

    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=users[0].keys())
        writer.writeheader()
        writer.writerows(users)
    return path
