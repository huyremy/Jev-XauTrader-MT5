# data_formatter.py
import json
import numpy as np

class DataFormatter:
    @staticmethod
    def format_for_jev(df, indicators):
        """Định dạng dữ liệu thành payload cho API Jev AI"""
        data = {
            "open": df['open'].tolist(),
            "close": df['close'].tolist(),
            "high": df['high'].tolist(),
            "low": df['low'].tolist(),
            "volume": df['tick_volume'].tolist(),
            "rsi": round(indicators['rsi'], 2),
            "macd": round(indicators['macd'], 4),
            "macd_signal": round(indicators['macd_signal'], 4),
            "macd_histogram": round(indicators['macd_histogram'], 4)
        }
        return data

    @staticmethod
    def create_prompt(data):
        """Tạo prompt mô tả cho Jev AI"""
        prompt = f"""
Analyze XAU/USD (Gold/US Dollar) price action for trading decision.

Price Data (last {len(data['close'])} candles):
- Open: {data['open'][-1]:.2f}
- Close: {data['close'][-1]:.2f}
- High: {data['high'][-1]:.2f}
- Low: {data['low'][-1]:.2f}
- Volume: {data['volume'][-1]}

Technical Indicators:
- RSI (14): {data['rsi']}
- MACD: {data['macd']:.4f}
- MACD Signal: {data['macd_signal']:.4f}
- MACD Histogram: {data['macd_histogram']:.4f}

Current Market Context:
- Trend: {'Bullish' if data['macd'] > data['macd_signal'] else 'Bearish'}
- Momentum: {'Strong' if data['rsi'] > 70 or data['rsi'] < 30 else 'Normal'}
- Volatility: {'High' if abs(data['macd_histogram']) > abs(data['macd']) * 0.5 else 'Normal'}

Provide trading signal with confidence score.
"""
        return prompt.strip()

# Sử dụng
if __name__ == "__main__":
    from mt5_connector import MT5Connector
    from indicators import Indicators
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
    connector = MT5Connector(config)
    df = connector.get_rates()
    ind = Indicators()
    indicators = ind.calculate_all(df)
    formatter = DataFormatter()

    data = formatter.format_for_jev(df, indicators)
    prompt = formatter.create_prompt(data)

    print("📋 Payload gửi API Jev AI:")
    print(json.dumps(data, indent=2))
    print(f"\n💬 Prompt mô tả:")
    print(prompt)
    connector.shutdown()
