
from domain.user import User
from domain.wallet import Wallet
from services.trade_service import TradeService

# создаем пользователя и кошелек
user = User(1, "Alice")
wallet = Wallet(user_id=user.id)

trade = TradeService()

trade.buy(wallet, 100)
trade.sell(wallet, 30)
trade.sell(wallet, 100)

