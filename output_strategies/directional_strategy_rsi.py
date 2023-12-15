# Import necessary modules
from decimal import Decimal
from hummingbot.data_feed.candles_feed.candles_factory import CandlesConfig, CandlesFactory
from typing import List
from hummingbot.core.data_type.common import OrderType, PriceType, TradeType
from hummingbot.core.data_type.order_candidate import OrderCandidate
from hummingbot.core.event.events import OrderFilledEvent
from hummingbot.strategy.script_strategy_base import ScriptStrategyBase

# Strategy Class Definition
class RSI_Strategy():
    # Strategy Metadata
    strategy_name: str = "RSI_Strategy"    
    
    # Market configuration
    trading_pair: str = "ETH-USDT"
    exchange: str = "binance_perpetual"
    api_key = "your_api_key"
    api_secret = "your_api_secret"
    order_amount_usd = Decimal("40")
    leverage = 10

    # PMM Parameters
    bid_spread = 10
    ask_spread = 10
    order_refresh_time = 10
    price_source = PriceType.MidPrice 

    # Candles configuration 
    candles = [CandlesFactory.get_candle(CandlesConfig(connector="binance_perpetual", trading_pair="ETH-USDT", interval="3m", max_records=1000))]

    # Market initialization
    markets = binance_perpetual: ETH-USDT
    
    
    # RSI Indicator Setup
    rsi_length = 14
    rsi_overbought = 70
    rsi_oversold = 30
    
    
    # This is the order order_management section 
    def on_tick(self):
        if self.create_timestamp <= self.current_timestamp:
            self.cancel_all_orders()
            proposal = self.create_proposal()
            proposal_adjusted = self.adjust_proposal_to_budget(proposal)
            self.place_orders(proposal_adjusted)
            self.create_timestamp = self.order_refresh_time + self.current_timestamp

    def create_proposal(self) -> List[OrderCandidate]:
        ref_price = self.connectors[self.exchange].get_price_by_type(self.trading_pair, self.price_source)
        buy_price = ref_price * Decimal(1 - self.bid_spread)
        sell_price = ref_price * Decimal(1 + self.ask_spread)

        buy_order = OrderCandidate(
            trading_pair=self.trading_pair, 
            is_maker=True, 
            order_type=OrderType.LIMIT,
            order_side=TradeType.BUY, 
            amount=Decimal(self.order_amount), 
            price=buy_price
        )

        sell_order = OrderCandidate(
            trading_pair=self.trading_pair, 
            is_maker=False, 
            order_type=OrderType.MARKET,
            order_side=TradeType.SELL, 
            amount=Decimal(self.order_amount), 
            price=sell_price
        )

        return [buy_order, sell_order]

    def adjust_proposal_to_budget(self, proposal: List[OrderCandidate]) -> List[OrderCandidate]:
        proposal_adjusted = self.connectors[self.exchange].budget_checker.adjust_candidates(proposal, all_or_none=True)
        return proposal_adjusted

    def place_orders(self, proposal: List[OrderCandidate]) -> None:
        for order in proposal:
            self.place_order(connector_name=self.exchange, order=order)

    def place_order(self, connector_name: str, order: OrderCandidate):
        if order.order_side == TradeType.SELL:
            self.sell(connector_name=connector_name, trading_pair=order.trading_pair, amount=order.amount,
                    order_type=order.order_type, price=order.price)
        elif order.order_side == TradeType.BUY:
            self.buy(connector_name=connector_name, trading_pair=order.trading_pair, amount=order.amount,
                    order_type=order.order_type, price=order.price)

    def cancel_all_orders(self):
        for order in self.get_active_orders(connector_name=self.exchange):
            self.cancel(self.exchange, order.trading_pair, order.client_order_id)

    def did_fill_order(self, event: OrderFilledEvent):
        msg = (f"{event.trade_type.name} {round(event.amount, 2)} {event.trading_pair} {self.exchange} at {round(event.price, 2)}")
        self.log_with_clock(logging.INFO, msg)
        self.notify_hb_app_with_timestamp(msg)
    