import json
import pandas as pd

def load_allocations():
    try:
        return pd.read_json("data/fund_allocations.json")
    except:
        return pd.DataFrame(columns=["fund_name", "category", "previous_year", "Jan", "Feb", "Mar"])

def save_allocations(df):
    df.to_json("data/fund_allocations.json", orient="records")

def load_targets():
    try:
        return json.load(open("data/category_targets.json"))
    except:
        return {"LargeCap": 0, "MidCap": 0, "SmallCap": 0, "Flexi": 0, "International": 0, "Other": 0}

def save_targets(targets):
    with open("data/category_targets.json", "w") as f:
        json.dump(targets, f)

def load_buffer():
    try:
        return json.load(open("data/monthly_buffer.json"))
    except:
        return {"Jan": 0, "Feb": 0, "Mar": 0}
