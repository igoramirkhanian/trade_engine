
import logging
from trade_engine.version import __version__  # версия приложения

from trade_engine.domain.user import User
from trade_engine.domain.wallet import Wallet
from trade_engine.services.trade_service import TradeService


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    logging.info(f"Trade Engine starting, version {__version__}")

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

