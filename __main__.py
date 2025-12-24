
from trade_engine.domain.user import User
from trade_engine.domain.wallet import Wallet
from trade_engine.services.trade_service import TradeService

def main():
    # создаем пользователя и кошелек
    user = User(1, "Alice")
    wallet = Wallet(user.id)

    trade = TradeService()

    # операции
    trade.buy(wallet, 100)
    trade.sell(wallet, 30)
    trade.sell(wallet, 100)

if __name__ == "__main__":
    main()

