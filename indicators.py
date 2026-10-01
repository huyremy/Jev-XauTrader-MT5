# indicators.py
import numpy as np
import pandas as pd

class Indicators:
    @staticmethod
    def calculate_rsi(prices, period=14):
        """Tính RSI (Relative Strength Index)"""
        delta = pd.Series(prices).diff()

        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))

        return rsi.iloc[-1] if len(rsi) > 0 else 50

    @staticmethod
    def calculate_macd(prices, fast=12, slow=26, signal=9):
        """Tính MACD (Moving Average Convergence Divergence)"""
        ema_fast = pd.Series(prices).ewm(span=fast, adjust=False).mean()
        ema_slow = pd.Series(prices).ewm(span=slow, adjust=False).mean()

        macd_line = ema_fast - ema_slow
        signal_line = macd_line.ewm(span=signal, adjust=False).mean()

        histogram = macd_line - signal_line

        return {
            "macd": macd_line.iloc[-1] if len(macd_line) > 0 else 0,
            "signal": signal_line.iloc[-1] if len(signal_line) > 0 else 0,
            "histogram": histogram.iloc[-1] if len(histogram) > 0 else 0
        }

    @staticmethod
    def calculate_all(df):
        """Tính tất cả chỉ số từ DataFrame giá"""
        close_prices = df['close'].values

        rsi = Indicators.calculate_rsi(close_prices)
        macd = Indicators.calculate_macd(close_prices)

        return {
            "rsi": rsi,
            "macd": macd["macd"],
            "macd_signal": macd["signal"],
            "macd_histogram": macd["histogram"]
        }

# Sử dụng
if __name__ == "__main__":
    import MetaTrader5 as mt5
    from config import MT5_PATH, MT5_LOGIN, MT5_PASSWORD, MT5_SERVER, SYMBOL, TIMEFRAME, NUM_BARS

    # Tạo config object
    class Config:
        def __init__(self):
            self.mt5_path = MT5_PATH
            self.mt5_login = MT5_LOGIN
            self.mt5_password = MT5_PASSWORD
            self.mt5_server = MT5_SERVER
            self.symbol = SYMBOL
            self.timeframe = TIMEFRAME
            self.num_bars = NUM_BARS

    config = Config()
    mt5.initialize()
    rates = mt5.copy_rates_from_pos(config.symbol, mt5.TIMEFRAME_H1, 0, 100)
    df = pd.DataFrame(rates)

    ind = Indicators()
    results = ind.calculate_all(df)
    print(f"RSI: {results['rsi']:.2f}")
    print(f"MACD: {results['macd']:.4f}")
    print(f"MACD Signal: {results['macd_signal']:.4f}")
    print(f"MACD Histogram: {results['macd_histogram']:.4f}")
