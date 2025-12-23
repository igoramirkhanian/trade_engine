
from domain.wallet import Wallet

class TradeService:
    def buy(self, wallet: Wallet, amount: float):
        wallet.balance += amount
        print(f"Пополнение: {amount}, баланс теперь {wallet.balance}")

    def sell(self, wallet: Wallet, amount: float):
        if wallet.balance < amount:
            print("Недостаточно средств")
            return
        wallet.balance -= amount
        print(f"Продажа: {amount}, баланс теперь {wallet.balance}")

