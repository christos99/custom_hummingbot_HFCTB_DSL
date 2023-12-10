"""
    A strategy to place only three buy orders.
    This Script strategy is generated with hbot-strategy-dsl.
    Author: Christos
"""

from decimal import Decimal
from typing import Dict

from hummingbot.connector.connector_base import ConnectorBase, TradeType
from hummingbot.core.data_type.common import OrderType
from hummingbot.data_feed.candles_feed.candles_factory import CandlesConfig
from hummingbot.smart_components.controllers.macd_bb_v1 import MACDBBV1, MACDBBV1Config
from hummingbot.smart_components.strategy_frameworks.data_types import (
    ExecutorHandlerStatus,
    OrderLevel,
    TripleBarrierConf,
)
from hummingbot.smart_components.strategy_frameworks.directional_trading.directional_trading_executor_handler import (
    DirectionalTradingExecutorHandler,
)
from hummingbot.strategy.script_strategy_base import ScriptStrategyBase


logger = logging.getLogger(__name__)


class BuyOnlyThreeTimesExampleStrategy(ScriptStrategyBase):
    """A strategy to place only three buy orders."""


order_amount_usd: float = 100  # Amount in USD for each order
orders_to_create: int = 3  # Total number of orders to create
base_asset: str = "ETH"  # Base asset symbol
quote_asset: str = "USDT"  # Quote asset symbol

    def __init__(self):
        """
            Initialize the strategy.

            This method sets up the initial state of the strategy upon instantiation.
            It initializes the markets that the strategy will interact with.

            The `super().__init__()` call ensures that the initialization logic of the
            base class (ScriptStrategyBase or any other relevant base class) is also executed,
            setting up essential components and configurations.
        """
        super().__init__()
        self.markets = {
            "kucoin_paper_trade": ['ETH-USDT'],
            "binance_paper_trade": ['BTC-USDT'],
            }
    
    def on_tick(self):
        """Main strategy operation executed periodically."""
        proposal = self._create_order_proposal()
        if proposal:
            self._execute_order_proposal(proposal)

    def _create_order_proposal(self) -> List[OrderCandidate]:
        """Generates order proposals based on strategy logic."""
        # Custom logic here...
        return []

    def _execute_order_proposal(self, proposal: List[OrderCandidate]):
        """Executes the given order proposal."""
        # Custom logic here...

    def did_fill_order(self, event: OrderFilledEvent):
        """Handles order filled events."""
        order_info = f"{event.trade_type.name} order of {event.amount} {event.trading_pair} at {event.price}"
        logger.info(f"Filled: {order_info}")
        self.notify_hb_app_with_timestamp(f"Filled: {order_info}")
