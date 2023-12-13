# Import necessary modules
import pandas as pd
from decimal import Decimal
from hummingbot.data_feed.candles_feed.candles_factory import CandlesConfig, CandlesFactory
from hummingbot.strategy.directional_strategy_base import DirectionalStrategyBase

# Strategy Class Definition
class RSI_Strategy(DirectionalStrategyBase):
    # Strategy Metadata
    strategy_name: str = "RSI_Strategy"    
    
    # Market configuration
    trading_pair: str = "ETH-USDT"
    exchange: str = "binance_perpetual"
    api_key = "your_api_key"
    api_secret = "your_api_secret"
    order_amount_usd = Decimal("40")
    leverage = 10    
    
    # Configure the parameters for the position
    stop_loss: float = 0.0075
    take_profit: float = 0.015
    time_limit: int = 60
    trailing_stop_activation_delta = 0.004
    trailing_stop_trailing_delta = 0.001

    # Candles configuration 
    candles = [CandlesFactory.get_candle(CandlesConfig(connector="binance_perpetual", trading_pair="ETH-USDT", interval="3m", max_records=1000))]


    # RSI Indicator Setup
    rsi_length = 7
    rsi_overbought = 70
    rsi_oversold = 30
    
        
    
    # Function to process indicators
    def get_processed_df(self):

        candles_df = self.candles[0].candles_df.copy()

        # Calculate RSI
        candles_df["RSI_7"] = ta.rsi(candles_df["close"], length=7)
        return candles_df
    
    
    def get_signal(self):
        candles_df = self.get_processed_df()
        # Check for buy conditions
        if candles_df["RSI"].iat[-1] < 30:
            return 1
        # Check for sell conditions
        elif candles_df["RSI"].iat[-1] > 70:
            return -1
        # Default to hold if no conditions met
        else:
            return 0
