import json
import os

FILE_PATH = "data/last_notice.json"


def load_data():
    if not os.path.exists(FILE_PATH):
        return {}

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}


def save_data(data):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)