# 🏦 UnitPlus Cash Agent

The **UnitPlus Cash Agent** is an AI-powered treasury management tool designed to help businesses optimize their idle cash. Using the Claude 3.5 Sonnet model, the agent analyzes liquidity, forecasts cash flow, and recommends high-yield allocations across UnitPlus investment products.

## 🌟 Key Features
*   **Autonomous Orchestration:** Uses a ReAct (Reasoning and Acting) loop to fetch real-time account balances and market rates before making decisions.
*   **Safety First:** Maintains a strict liquidity buffer to ensure the business always has enough cash for operations.
*   **Audit Trail:** Every recommendation is logged into a local SQLite database (`outcomes.db`), creating a "data moat" for future performance analysis.
*   **Professional UI:** A clean Streamlit dashboard that visualizes cash allocations and projected annual yields.

## 🛠️ Project Structure
*   `app.py`: The main user interface and dashboard.
*   `agent.py`: The logic that connects to Anthropic's Claude AI.
*   `backend.py`: Simulates banking APIs and cash flow forecasting.
*   `database.py`: Handles the persistence of agent decisions and outcomes.
*   `requirements.txt`: Lists the necessary Python libraries to run the project.

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.9+ installed and an **Anthropic API Key**.

### 2. Installation
Clone the repository or download the files, then install the dependencies:
```bash
pip install -r requirements.txt
