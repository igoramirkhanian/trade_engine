
from trade_engine.domain.wallet import Wallet
from trade_engine.domain.transaction import Transaction

class TradeService:
    def __init__(self):
        self.transactions = []  # история всех операций

    def buy(self, wallet: Wallet, amount: float):
        wallet.balance += amount
        tx = Transaction(wallet.user_id, "buy", amount)
        self.transactions.append(tx)
        print(f"[BUY] User {wallet.user_id} +{amount}, balance={wallet.balance}")

    def sell(self, wallet: Wallet, amount: float):
        if wallet.balance < amount:
            print(f"[SELL] User {wallet.user_id} insufficient balance ({wallet.balance})")
            return
        wallet.balance -= amount
        tx = Transaction(wallet.user_id, "sell", amount)
        self.transactions.append(tx)
        print(f"[SELL] User {wallet.user_id} -{amount}, balance={wallet.balance}")

    def show_history(self, user_id: int):
        print(f"\nTransaction history for User {user_id}:")
        for tx in self.transactions:
            if tx.user_id == user_id:
                print(tx)

