import sqlite3
import json
from datetime import datetime
import pandas as pd

def init_db():
    conn = sqlite3.connect("outcomes.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS allocation_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            user_prompt TEXT,
            total_cash_eur REAL,
            recommendation_json TEXT,
            total_allocated_eur REAL,
            expected_yield_eur REAL
        )
    """)
    conn.commit()
    return conn

def log_allocation(prompt, total_cash, rec):
    conn = init_db()
    conn.execute(
        "INSERT INTO allocation_log (timestamp, user_prompt, total_cash_eur, recommendation_json, total_allocated_eur, expected_yield_eur) VALUES (?,?,?,?,?,?)",
        (datetime.utcnow().isoformat(), prompt, total_cash, json.dumps(rec), rec.get("total_allocated_eur", 0), rec.get("expected_annual_yield_eur", 0))
    )
    conn.commit()
    conn.close()

def get_audit_logs():
    conn = init_db()
    df = pd.read_sql_query("SELECT * FROM allocation_log ORDER BY timestamp DESC", conn)
    conn.close()
    return df