import streamlit as st
from backend import MockBackend
from agent import run_optimization_agent
from database import log_allocation, get_audit_logs

st.title("🏦 UnitPlus Cash Agent")
api_key = st.sidebar.text_input("Anthropic API Key", type="password")

if st.button("Run Agent"):
    backend = MockBackend(500000, 100000, 50000, 120000)
    result = run_optimization_agent(api_key, "Allocate 500k", backend)
    log_allocation("Allocate 500k", 500000, result)
    st.write(result)

st.header("History")
st.dataframe(get_audit_logs())