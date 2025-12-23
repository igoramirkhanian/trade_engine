
from datetime import datetime

class Transaction:
    def __init__(self, user_id: int, type_: str, amount: float):
        self.user_id = user_id
        self.type = type_  # "buy" или "sell"
        self.amount = amount
        self.date = datetime.now()

    def __repr__(self):
        return f"<Transaction {self.type} User:{self.user_id} Amount:{self.amount} Date:{self.date.strftime('%Y-%m-%d %H:%M:%S')}>"

