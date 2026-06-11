import streamlit as st
import json
from backend import MockBackend
from agent import run_optimization_agent
from database import log_allocation, get_audit_logs

st.set_page_config(page_title="Corporate Treasury Allocation Agent", layout="wide")

st.title("Enterprise Cash Allocation Agent")
st.markdown("Automated evaluation tool for optimizing excess corporate liquidity positions.")

# Sidebar Configuration
st.sidebar.header("Credentials & Configurations")
api_key = st.sidebar.text_input("Anthropic API Key", type="password")

st.sidebar.subheader("Liquidity Metrics (EUR)")
total_cash = st.sidebar.number_input("Total Cash Asset Base", value=500000)
inflows = st.sidebar.number_input("Projected Monthly Inflows", value=100000)
outflows = st.sidebar.number_input("Projected Monthly Outflows", value=50000)
buffer = st.sidebar.number_input("Mandatory Operations Buffer", value=120000)

# Build context object
backend = MockBackend(total_cash, inflows, outflows, buffer)
forecast = backend.run_cashflow_forecast()
products = backend.get_available_products()

# Core UI Layout split into tabs
tab1, tab2 = st.tabs(["Optimization Control", "Audit Logs"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Current Financial Stance")
        st.metric("Net Running Cashflow", f"€{forecast['net_cashflow']:,}")
        st.metric("Deployable Surplus Base", f"€{forecast['surplus']:,}")
    
    with col2:
        st.subheader("Available Yield Instruments")
        for p in products["products"]:
            st.write(f"- **{p['name']}**: Yield target of `{p['rate']}%`")

    st.markdown("---")
    
    prompt_input = st.text_area("Allocation Constraints / Instructions", value=f"Optimize allocation for €{forecast['surplus']} surplus.")

    if st.button("Execute Treasury Optimization Engine", type="primary"):
        if not api_key:
            st.error("Please enter a valid API key in the sidebar.")
        else:
            with st.spinner("Processing scenario parameters..."):
                system_instruction = (
                    "You are an expert corporate treasurer. Provide recommendations strictly in a structured JSON schema. "
                    f"Available options: {json.dumps(products)}. "
                    "Include the keys 'total_allocated_eur' and 'expected_annual_yield_eur'."
                )
                
                result = run_optimization_agent(api_key, prompt_input, system_instruction)
                
                if "error" in result:
                    st.error(result["error"])
                else:
                    log_allocation(prompt_input, total_cash, result)
                    st.success("Allocation Strategy Compiled and Logged.")
                    st.json(result)

with tab2:
    st.subheader("Historical Decisions Data Frame")
    logs_df = get_audit_logs()
    if not logs_df.empty:
        st.dataframe(logs_df, use_container_width=True)
    else:
        st.info("No records located in outcomes.db.")
