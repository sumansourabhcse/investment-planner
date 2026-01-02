import streamlit as st
from utils.data_io import load_allocations, load_buffer
from utils.calculations import calculate_totals

st.title("📊 Monthly Summary")

allocs = load_allocations()
buffer = load_buffer()
totals = calculate_totals(allocs)

monthly = totals["monthly_totals"]
monthly["Buffer"] = monthly["Month"].map(buffer)
monthly["Net"] = monthly["Total"] - monthly["Buffer"]

st.dataframe(monthly)
