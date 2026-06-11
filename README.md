# 🏦 Cash Agent

Cash Agent is a prototype treasury optimization system that evaluates available cash, estimates short-term liquidity requirements, and recommends allocations into yield-generating products while maintaining an operational cash buffer.

The project demonstrates how a large language model can be integrated with deterministic financial rules and simulated banking APIs to support treasury decision-making workflows.

---

## Overview

The workflow implemented in this project is:

1. Retrieve account balances from a backend service.
2. Estimate available surplus cash after reserving a liquidity buffer.
3. Query available investment products and interest rates.
4. Generate an allocation recommendation.
5. Persist recommendations to a local database for auditing and analysis.

The application is intentionally lightweight and designed as a proof-of-concept rather than a production treasury platform.

---

## Features

### Cash Position Analysis

The system evaluates available cash balances and estimates surplus liquidity based on projected inflows, outflows, and a required operational buffer.

### Allocation Recommendations

A language model is used to generate structured allocation recommendations based on the financial context provided to it.

### Audit Logging

All recommendations are stored in a local SQLite database, allowing historical recommendations to be reviewed and analyzed.

### Interactive Dashboard

A simple Streamlit interface allows users to run allocation scenarios and inspect historical recommendations.

---

## Project Structure

```text
cash-agent/
├── app.py
├── agent.py
├── backend.py
├── database.py
├── requirements.txt
└── README.md
```

### app.py

Streamlit user interface for running allocation scenarios and viewing historical recommendations.

### agent.py

Handles communication with the Anthropic API and converts model responses into structured JSON output.

### backend.py

Provides a mock treasury backend that simulates account balances, cashflow forecasts, and available investment products.

### database.py

Creates and manages the SQLite audit database used to store allocation recommendations.

### requirements.txt

Lists Python dependencies required to run the application.

---

## Installation

### Prerequisites

* Python 3.9+
* Anthropic API key

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## Example Workflow

1. Enter an Anthropic API key.
2. Run the allocation agent.
3. Review the generated recommendation.
4. Inspect historical recommendations stored in SQLite.

---

## Current Limitations

This repository is intentionally simplified and has several limitations:

* Uses a mock backend instead of real banking APIs.
* Supports only a small set of simulated investment products.
* Relies on LLM-generated recommendations rather than a deterministic optimization engine.
* Uses SQLite for persistence.
* Does not include authentication, authorization, or production deployment infrastructure.

---

## Future Improvements

Potential future enhancements include:

* Deterministic portfolio optimization logic.
* Real market data integration.
* Multiple investment products and allocation constraints.
* Scenario analysis and stress testing.
* Automated performance tracking of recommendations.
* Containerized deployment with Docker.
* Unit and integration test coverage.

---

## Purpose

This project was built as a learning exercise to explore:

* Agent-based financial workflows
* Treasury optimization concepts
* Streamlit application development
* SQLite persistence
* Integration with large language model APIs

The focus is on demonstrating the end-to-end workflow rather than building a production-ready treasury management system.

