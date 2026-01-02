import streamlit as st
from utils.data_io import load_allocations, save_allocations
from utils.calculations import calculate_totals

st.title("🧮 Allocation Grid")

# -----------------------------
# FUND DICTIONARY
# -----------------------------
mutual_funds = {
    "Bandhan Small Cap Fund": "147946",
    "Axis Small Cap Fund": "125354",
    "SBI Small Cap Fund": "125497",
    "quant Small Cap Fund": "120828",

    "Motilal Oswal Midcap Fund": "127042",
    "HSBC Midcap Fund": "151034",
    "Kotak Midcap Fund": "119775",
    "quant Mid Cap Fund": "120841",
    "Edelweiss Nifty Midcap150 Momentum 50 Index Fund": "150902",

    "Parag Parikh Flexi Cap Fund": "122639",
    "Kotak Flexicap Fund": "112090",

    "Nippon India Large Cap Fund": "118632",
    "Mirae Asset Large & Midcap Fund": "118834",
    "ICICI Pru BHARAT 22 FOF": "143903",
    "quant Focused Fund": "120834",

    "Mirae Asset FANG+": "148928",
    "ICICI Pru Technology Fund": "120594",
    "SBI Magnum Children's Benefit Fund": "148490"
}

FUND_OPTIONS = list(mutual_funds.keys())

CATEGORY_OPTIONS = ["LargeCap", "MidCap", "SmallCap", "Flexi", "International", "Other"]
MONTH_OPTIONS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                 "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
YEAR_OPTIONS = ["2025", "2026", "2027"]

# -----------------------------
# LOAD DATA
# -----------------------------
data = load_allocations()

# Remove legacy columns
for col in ["previous_year", "Jan", "Feb", "Mar"]:
    if col in data.columns:
        data = data.drop(columns=[col])

# Ensure required columns exist
for col in ["fund_name", "category", "month", "year", "amount"]:
    if col not in data.columns:
        data[col] = ""

# -----------------------------
# DATA EDITOR
# -----------------------------
edited = st.data_editor(
    data,
    num_rows="dynamic",
    use_container_width=True,
    column_config={
        "fund_name": st.column_config.SelectboxColumn(
            "Fund Name",
            options=FUND_OPTIONS,
            required=True
        ),
        "category": st.column_config.SelectboxColumn(
            "Category",
            options=CATEGORY_OPTIONS,
            required=True
        ),
        "month": st.column_config.SelectboxColumn(
            "Month",
            options=MONTH_OPTIONS,
            required=True
        ),
        "year": st.column_config.SelectboxColumn(
            "Year",
            options=YEAR_OPTIONS,
            required=True
        ),
        "amount": st.column_config.NumberColumn(
            "Amount",
            min_value=0,
            step=100
        )
    }
)

# -----------------------------
# SAVE BUTTON
# -----------------------------
if st.button("Save Allocations"):
    save_allocations(edited)
    st.success("Saved!")

# -----------------------------
# TOTALS
# -----------------------------
totals = calculate_totals(edited)

st.subheader("Category Totals")
st.dataframe(totals["category_totals"])

st.subheader("Monthly Totals")
st.dataframe(totals["monthly_totals"])
