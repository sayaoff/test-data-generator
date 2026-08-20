import csv
import json
import tempfile
import unittest
from pathlib import Path

from exporters import save_to_csv, save_to_json

SAMPLE_USERS = [
    {
        "first_name": "Alex",
        "last_name": "Ivanov",
        "email": "alex@example.com",
        "phone": "+79123456789",
        "username": "alex_ivanov",
        "password": "Test123!",
        "data_type": "valid",
    }
]


class ExporterTests(unittest.TestCase):
    def test_save_to_json(self):
        with tempfile.TemporaryDirectory() as directory:
            path = save_to_json(SAMPLE_USERS, str(Path(directory) / "users.json"))
            with path.open(encoding="utf-8") as file:
                self.assertEqual(json.load(file), SAMPLE_USERS)

    def test_save_to_csv(self):
        with tempfile.TemporaryDirectory() as directory:
            path = save_to_csv(SAMPLE_USERS, str(Path(directory) / "users.csv"))
            with path.open(encoding="utf-8", newline="") as file:
                rows = list(csv.DictReader(file))
            self.assertEqual(rows, SAMPLE_USERS)


if __name__ == "__main__":
    unittest.main()
