import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_gejala():
    with open(os.path.join(DATA_DIR, "gejala.json"), "r", encoding="utf-8") as f:
        return json.load(f)

def load_diagnosa():
    with open(os.path.join(DATA_DIR, "diagnosa.json"), "r", encoding="utf-8") as f:
        return json.load(f)

def load_rules():
    with open(os.path.join(DATA_DIR, "rules.json"), "r", encoding="utf-8") as f:
        return json.load(f)