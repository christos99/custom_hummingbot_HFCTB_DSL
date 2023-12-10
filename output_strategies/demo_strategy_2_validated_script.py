"""
    An advanced trading strategy with multiple markets and dynamic parameters.
    This Script strategy is generated with hbot-strategy-dsl.
    Author: John Smith
"""

 import logging
import time
from decimal import Decimal
from typing import List

from hummingbot.connector.utils import split_hb_trading_pair
from hummingbot.core.data_type.order_candidate import OrderCandidate
from hummingbot.core.event.events import OrderFilledEvent, OrderType, TradeType
from hummingbot.core.rate_oracle.rate_oracle import RateOracle
from hummingbot.strategy.script_strategy_base import ScriptStrategyBase


logger = logging.getLogger(__name__)


class AdvancedStrategyStrategy(ScriptStrategyBase):
    """An advanced trading strategy with multiple markets and dynamic parameters."""


    buy_spread = 0.02  # Spread percentage for buy orders

    sell_spread = 0.02  # Spread percentage for sell orders

    order_amount = 0.5  # The amount of each order


    def __init__(self):
        super().__init__()
        self.markets = {

            "binance": ['BTC-USD', 'ETH-USD'],

            "kucoin": ['LTC-USD', 'XRP-USD'],

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
