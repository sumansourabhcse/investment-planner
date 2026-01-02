import streamlit as st
from utils.data_io import load_allocations, save_allocations
from utils.calculations import calculate_totals

st.title("🧮 Allocation Grid")

data = load_allocations()
edited = st.data_editor(data, num_rows="dynamic", use_container_width=True)

if st.button("Save Allocations"):
    save_allocations(edited)
    st.success("Saved!")

totals = calculate_totals(edited)
st.subheader("Category Totals")
st.dataframe(totals["category_totals"])

st.subheader("Monthly Totals")
st.dataframe(totals["monthly_totals"])
