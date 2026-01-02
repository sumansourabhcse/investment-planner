import streamlit as st
from utils.data_io import load_allocations, save_allocations
from utils.calculations import calculate_totals

st.title("🧮 Allocation Grid")

CATEGORY_OPTIONS = ["LargeCap", "MidCap", "SmallCap", "Flexi", "International", "Other"]
MONTH_OPTIONS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                 "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
YEAR_OPTIONS = ["2025", "2026", "2027"]

data = load_allocations()

# Remove previous_year column
if "previous_year" in data.columns:
    data = data.drop(columns=["previous_year"])

# Ensure required columns exist
for col in ["category", "month", "year", "amount"]:
    if col not in data.columns:
        data[col] = ""

edited = st.data_editor(
    data,
    num_rows="dynamic",
    use_container_width=True,
    column_config={
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

if st.button("Save Allocations"):
    save_allocations(edited)
    st.success("Saved!")

totals = calculate_totals(edited)

st.subheader("Category Totals")
st.dataframe(totals["category_totals"])

st.subheader("Monthly Totals")
st.dataframe(totals["monthly_totals"])
