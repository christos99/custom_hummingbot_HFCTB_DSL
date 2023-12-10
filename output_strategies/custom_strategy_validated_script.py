"""
    A strategy with a custom price calculation method.
    This PMM strategy is generated with hbot-strategy-dsl.
    Author: Jane Doe
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


class CustomPriceStrategyStrategy(ScriptStrategyBase):
    """A strategy with a custom price calculation method."""


    
    



    def __init__(self):
        super().__init__()
        self.markets = {

            "binance": ['BTC-USD', 'ETH-USD'],

        }

    def calculate_custom_price(self):
        
        # Default price calculation logic
        price = self.mid_price * Decimal('1.01')
        return price
        

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
