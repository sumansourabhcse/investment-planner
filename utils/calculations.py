def calculate_totals(df):
    df = df.fillna(0)
    df["Total"] = df[["Jan", "Feb", "Mar"]].sum(axis=1)

    category_totals = df.groupby("category")["Total"].sum().to_dict()

    monthly_totals = []
    for month in ["Jan", "Feb", "Mar"]:
        monthly_totals.append({
            "Month": month,
            "Total": df[month].sum()
        })

    return {
        "category_totals": category_totals,
        "monthly_totals": pd.DataFrame(monthly_totals)
    }
