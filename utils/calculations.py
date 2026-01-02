import pandas as pd

def calculate_totals(df):
    # Ensure df is valid
    if df is None or df.empty:
        return {
            "category_totals": {},
            "monthly_totals": pd.DataFrame([{"Month": m, "Total": 0} for m in ["Jan", "Feb", "Mar"]])
        }

    # Ensure required columns exist
    required_months = ["Jan", "Feb", "Mar"]
    for col in required_months:
        if col not in df.columns:
            df[col] = 0

    # Fill NaN
    df = df.fillna(0)

    # Row total
    df["Total"] = df[required_months].sum(axis=1)

    # Category totals
    if "category" in df.columns:
        category_totals = df.groupby("category")["Total"].sum().to_dict()
    else:
        category_totals = {}

    # Monthly totals
    monthly_totals = []
    for month in required_months:
        monthly_totals.append({
            "Month": month,
            "Total": df[month].sum()
        })

    return {
        "category_totals": category_totals,
        "monthly_totals": pd.DataFrame(monthly_totals)
    }
