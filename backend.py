from typing import Dict, Any

class MockBackend:
    """
    Simulates core banking data endpoints, treasury positions, 
    and cash flow forecasting metrics.
    """
    def __init__(self, total_cash: float, inflows: float, outflows: float, buffer: float):
        self.total_cash = total_cash
        self.inflows = inflows
        self.outflows = outflows
        self.buffer = buffer

    def get_account_balances(self) -> Dict[str, Any]:
        return {
            "total_eur": self.total_cash, 
            "accounts": [
                {"name": "Corporate Operating Base", "balance": self.total_cash * 0.6},
                {"name": "Secondary Operational Vault", "balance": self.total_cash * 0.4}
            ]
        }

    def run_cashflow_forecast(self) -> Dict[str, float]:
        net_cashflow = self.inflows - self.outflows
        surplus = self.total_cash - self.buffer
        return {
            "net_cashflow": float(net_cashflow),
            "surplus": float(max(0.0, surplus))
        }

    def get_available_products(self) -> Dict[str, Any]:
        return {
            "products": [
                {"id": "cash_plus_01", "name": "UnitPlus Cash (EUR)", "rate": 3.10},
                {"id": "gov_bond_01", "name": "Euro Short-Term Sovereign", "rate": 3.45},
                {"id": "mff_liquidity", "name": "Institutional Money Market", "rate": 3.25}
            ]
        }
