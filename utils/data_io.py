import os
import json
import pandas as pd

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

ALLOC_FILE = os.path.join(DATA_DIR, "fund_allocations.json")
TARGETS_FILE = os.path.join(DATA_DIR, "category_targets.json")
BUFFER_FILE = os.path.join(DATA_DIR, "monthly_buffer.json")

def load_allocations():
    if os.path.exists(ALLOC_FILE):
        return pd.read_json(ALLOC_FILE)
    return pd.DataFrame(columns=["fund_name", "category", "previous_year", "Jan", "Feb", "Mar"])

def save_allocations(df):
    df.to_json(ALLOC_FILE, orient="records")

def load_targets():
    if os.path.exists(TARGETS_FILE):
        return json.load(open(TARGETS_FILE))
    return {"LargeCap": 0, "MidCap": 0, "SmallCap": 0, "Flexi": 0, "International": 0, "Other": 0}

def save_targets(targets):
    with open(TARGETS_FILE, "w") as f:
        json.dump(targets, f)

def load_buffer():
    if os.path.exists(BUFFER_FILE):
        return json.load(open(BUFFER_FILE))
    return {"Jan": 0, "Feb": 0, "Mar": 0}
