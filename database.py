import sqlite3
import json
from datetime import datetime, timezone
import pandas as pd
from typing import Dict, Any

DB_PATH = "outcomes.db"

def init_db():
    """Initializes schema if table is missing."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS allocation_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                user_prompt TEXT,
                total_cash_eur REAL,
                recommendation_json TEXT,
                total_allocated_eur REAL,
                expected_yield_eur REAL
            )
        """)
        conn.commit()

def log_allocation(prompt: str, total_cash: float, rec: Dict[str, Any]):
    """Logs an allocation decision to the persistent SQLite audit store."""
    init_db()  # Ensures database structure exists
    
    # AI Fix: modern timezone-aware UTC format
    timestamp = datetime.now(timezone.utc).isoformat()
    
    total_allocated = rec.get("total_allocated_eur", 0.0)
    expected_yield = rec.get("expected_annual_yield_eur", 0.0)

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """INSERT INTO allocation_log (
                timestamp, user_prompt, total_cash_eur, recommendation_json, total_allocated_eur, expected_yield_eur
               ) VALUES (?, ?, ?, ?, ?, ?)""",
            (timestamp, prompt, total_cash, json.dumps(rec), float(total_allocated), float(expected_yield))
        )
        conn.commit()

def get_audit_logs() -> pd.DataFrame:
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query("SELECT * FROM allocation_log ORDER BY timestamp DESC", conn)
    return df
