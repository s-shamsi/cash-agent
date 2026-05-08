class MockBackend:
    def __init__(self, total_cash, inflows, outflows, buffer):
        self.total_cash = total_cash
        self.inflows = inflows
        self.outflows = outflows
        self.buffer = buffer

    def get_account_balances(self):
        return {"total_eur": self.total_cash, "accounts": [{"name": "Main", "balance": self.total_cash}]}

    def run_cashflow_forecast(self):
        return {"net_cashflow": self.inflows - self.outflows, "surplus": self.total_cash - self.buffer}

    def get_available_products(self):
        return {"products": [{"id": "cash_plus", "name": "UnitPlus Cash", "rate": 3.1}]}