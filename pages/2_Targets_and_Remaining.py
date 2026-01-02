import streamlit as st
from utils.data_io import load_targets, save_targets, load_allocations
from utils.calculations import calculate_totals

st.title("🎯 Targets & Remaining")

targets = load_targets()
for cat in targets:
    targets[cat] = st.number_input(f"{cat} Target", value=targets[cat], min_value=0)

if st.button("Save Targets"):
    save_targets(targets)
    st.success("Targets saved!")

allocs = load_allocations()
totals = calculate_totals(allocs)

st.subheader("Remaining vs Target")
remaining = []
for cat, target in targets.items():
    invested = totals["category_totals"].get(cat, 0)
    remaining.append({
        "Category": cat,
        "Target": target,
        "Invested": invested,
        "Remaining": target - invested
    })

st.dataframe(remaining)
