import streamlit as st
from utils.layout import load_header

st.set_page_config(page_title="Investment Planner", layout="wide")
load_header()

st.write("Use the sidebar to navigate between:")
st.markdown("- 🧮 Allocation Grid")
st.markdown("- 🎯 Targets & Remaining")
st.markdown("- 📊 Monthly Summary")
