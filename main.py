# main.py
import json
import time
from datetime import datetime
from config import MT5_PATH, MT5_LOGIN, MT5_PASSWORD, MT5_SERVER, JEV_API_KEY, JEV_API_URL, JEV_MODEL, SYMBOL, TIMEFRAME, NUM_BARS, CONFIDENCE_THRESHOLD
from mt5_connector import MT5Connector
from indicators import Indicators
from data_formatter import DataFormatter
from jev_client import get_trading_signal

def print_header():
    """In tiêu đề đẹp"""
    print("\n" + "="*60)
    print("🤖 AUTO TRADE XAU/USD WITH JEV AI")
    print("="*60)
    print(f"📅 Thời gian: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📊 Cặp tiền: {SYMBOL} | Khung: {TIMEFRAME}")
    print("="*60 + "\n")

def print_signal_result(signal, df):
    """In kết quả tín hiệu đẹp"""
    last_candle = df.iloc[-1]
    print(f"\n🎯 TÍN HIỆU GIAO DỊCH TỪ JEV AI")
    print("-" * 40)
    print(f"📈 Giá hiện tại: {last_candle['close']:.2f}")
    print(f"📉 RSI: {signal.get('rsi', 'N/A'):.2f}")
    print(f"📊 MACD: {signal.get('macd', 'N/A'):.4f}")
    print(f"📉 MACD Signal: {signal.get('macd_signal', 'N/A'):.4f}")
    print("-" * 40)
    print(f"✅ SIGNAL: {signal['buy'] and '🟢 BUY' or signal['sell'] and '🔴 SELL' or '⚪ HOLD'}")
    print(f"🔢 CONFIDENCE: {signal['confidence']:.2%}")
    print(f"⚠️  RISK LEVEL: {'LOW' if signal['strong_signal'] else 'MEDIUM'}")
    print(f"💭 REASONING: {signal['reasoning']}")
    print("-" * 40)

def execute_trade(signal, df):
    """Thực hiện giao dịch (thí nghiệm - không thật)**
    """
    confidence = signal['confidence']

    if confidence < CONFIDENCE_THRESHOLD:
        print(f"\n⏭️  Bỏ qua: Confidence {confidence:.2%} < {CONFIDENCE_THRESHOLD:.2%}")
        return False

    last_candle = df.iloc[-1]

    print(f"\n🔄 ĐANG THỰC HIỆN GIAO DỊCH...")
    print(f"   → Giá vào: {last_candle['close']:.2f}")
    print(f"   → Volume: {last_candle['tick_volume']}")

    if signal['buy']:
        print(f"   → Lệnh: MUA XAU/USD")
    elif signal['sell']:
        print(f"   → Lệnh: BÁN XAU/USD")
    else:
        print(f"   → Lệnh: KHÔNG GIAO DỊCH (HOLD)")

    print(f"   → Risk: {'LOW' if signal['strong_signal'] else 'MEDIUM'}")
    return True

def main():
    """Chạy chính chương trình"""
    print_header()

    # Tạo config object từ các biến trong config.py
    class Config:
        def __init__(self):
            self.mt5_path = MT5_PATH
            self.mt5_login = MT5_LOGIN
            self.mt5_password = MT5_PASSWORD
            self.mt5_server = MT5_SERVER
            self.beatapi_api_key = JEV_API_KEY
            self.base_url = JEV_API_URL
            self.model = JEV_MODEL
            self.symbol = SYMBOL
            self.timeframe = TIMEFRAME
            self.num_bars = NUM_BARS
            self.confidence_threshold = CONFIDENCE_THRESHOLD

    config = Config()

    try:
        # 1. Kết nối MT5
        print("🔌 Đang kết nối MT5...")
        connector = MT5Connector(config)

        # 2. Lấy dữ liệu
        print("📥 Đang lấy dữ liệu giá...")
        df = connector.get_rates()

        if df is None or len(df) == 0:
            print("❌ Không có dữ liệu, thoát chương trình")
            return

        # 3. Tính chỉ số
        print("📊 Đang tính chỉ số kỹ thuật...")
        ind = Indicators()
        indicators = ind.calculate_all(df)

        # 4. Lấy tín hiệu từ Jev AI
        print("🤖 Đang gọi API Jev AI...")
        signal = get_trading_signal(df, indicators, config)

        if signal is None:
            print("❌ API Jev AI không phản hồi")
            return

        # 5. Hiển thị kết quả
        print_signal_result(signal, df)

        # 6. Thực hiện giao dịch (thí nghiệm)
        execute_trade(signal, df)

        # 7. Lưu kết quả
        save_result(df, indicators, signal)

    except Exception as e:
        print(f"\n❌ LỖI: {e}")
        import traceback
        traceback.print_exc()

    finally:
        # Đóng kết nối
        if 'connector' in locals():
            connector.shutdown()
        print("\n" + "="*60)
        print("✅ Chương trình kết thúc")
        print("="*60 + "\n")

def save_result(df, indicators, signal):
    """Lưu kết quả vào file JSON"""
    last_candle_dict = df.iloc[-1].to_dict()
    last_candle_dict['time'] = str(last_candle_dict['time'])

    result = {
        "timestamp": datetime.now().isoformat(),
        "symbol": SYMBOL,
        "timeframe": TIMEFRAME,
        "data_points": len(df),
        "last_candle": last_candle_dict,
        "indicators": indicators,
        "signal": signal
    }

    import os
    os.makedirs("results", exist_ok=True)

    filename = f"results/{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\n💾 Đã lưu kết quả: {filename}")

if __name__ == "__main__":
    main()
