# 🤖 AUTO TRADE XAU/USD with Jev AI

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Jev AI](https://img.shields.io/badge/Jev%20AI-System%20One-orange)](https://www.beatapi.com)
[![MT5](https://img.shields.io/badge/MT5-MetaTrader%205-blue)](https://www.metatrader5.com)

> Hệ thống giao dịch tự động cho XAU/USD (Vàng) sử dụng Jev AI System One để phân tích kỹ thuật và ra quyết định giao dịch chính xác.

---

## 🎯 Overview

AUTO TRADE XAU/USD là hệ thống giao dịch tự động kết hợp phân tích kỹ thuật truyền thống với trí tuệ nhân tạo Jev AI System One. Hệ thống tự động:

- Kết nối MetaTrader 5 để lấy dữ liệu giá thời gian thực
- Tính toán các chỉ số kỹ thuật: RSI, MACD, EMA, Bollinger Bands
- Gửi dữ liệu cho Jev AI phân tích và ra tín hiệu giao dịch
- Quản lý rủi ro với ngưỡng confidence và dừng lỗ
- Lưu trữ kết quả giao dịch đầy đủ vào file JSON

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **Jev AI Integration** | Tích hợp trực tiếp với Jev AI System One - mô hình AI chuyên dụng cho phân tích tài chính |
| 📈 **Technical Indicators** | Tính toán đầy đủ các chỉ số: RSI, MACD, MACD Signal, MACD Histogram, EMA |
| ⚡ **High Performance** | Xử lý dữ liệu thị trường theo thời gian thực với tốc độ cao |
| 📊 **Logging & Analytics** | Lưu trữ đầy đủ lịch sử giao dịch, kết quả phân tích vào file JSON có cấu trúc |
| 🔧 **Easy Configuration** | Cấu hình đơn giản qua file config.py - thay đổi symbol, timeframe, ngưỡng rủi ro chỉ với vài dòng code |

---

## 🚀 Installation

### Prerequisites

- Python 3.10+
- MetaTrader 5 terminal cài đặt sẵn
- Tài khoản MT5 với quyền truy cập API
- API Key từ Jev AI ([https://www.beatapi.com](https://www.beatapi.com))

### Steps

```bash
# 1. Clone repository
git clone https://github.com/huyremy/Jev-XauTrader-MT5.git
cd Jev-XauTrader-MT5

# 2. Install dependencies
pip install -r requirements.txt
pip install mt5-trader  # MetaTrader 5 Python API

# 3. Configure API Keys
# Create config.py file (see Configuration section below)

# 4. Run the system
python main.py
⚙️ Configuration
Tạo file config.py trong thư mục gốc:

# config.py
MT5_PATH = "C:/Program Files/MetaTrader 5/mt5.exe"
MT5_LOGIN = 12345678
MT5_PASSWORD = "your_password"
MT5_SERVER = "your_server"
JEV_API_KEY = "your_jev_api_key"
JEV_API_URL = "https://api.beatapi.com/v1/chat"
JEV_MODEL = "jev-1.13-free"
SYMBOL = "XAUUSD"
TIMEFRAME = "H1"
NUM_BARS = 100
CONFIDENCE_THRESHOLD = 0.75
Parameter Description
Parameter	Default	Description
MT5_PATH	"C:/Program Files/MetaTrader 5/mt5.exe"	Đường dẫn đến MT5 terminal
MT5_LOGIN	12345678	Số tài khoản MT5
MT5_PASSWORD	"your_password"	Mật khẩu tài khoản MT5
MT5_SERVER	"your_server"	Server MT5
JEV_API_KEY	"your_jev_api_key"	API Key từ Jev AI
JEV_API_URL	"https://api.beatapi.com/v1/chat"	URL API Jev AI
JEV_MODEL	"jev-1.13-free"	Model Jev AI sử dụng
SYMBOL	"XAUUSD"	Cặp tiền giao dịch
TIMEFRAME	"H1"	Khung thời gian: M1, M5, M15, M30, H1, H4, D1
NUM_BARS	100	Số lượng nến lấy từ MT5
CONFIDENCE_THRESHOLD	0.75	Ngưỡng tối thiểu để thực hiện giao dịch
📁 Project Structure
autotrader-xau/
├── main.py              # Main entry point
├── config.py            # Configuration file
├── requirements.txt     # Python dependencies
├── README.md            # This file
├── results/             # Saved trading results
│   └── *.json           # JSON log files
├── src/
│   ├── mt5_connector.py # MetaTrader 5 connector
│   ├── indicators.py    # Technical indicators calculation
│   ├── data_formatter.py # Data formatting utilities
│   └── jev_client.py    # Jev AI API client
└── tests/
    └── test_jev_api.py  # API testing utilities
🛠️ Technology Stack
Technology	Description
Python 3.10+	Core programming language
Pandas	Data manipulation and analysis
Requests	HTTP client for API calls
MetaTrader 5	Trading platform and API
Jev AI System One	AI-powered decision making
📖 Usage
Basic Usage
from jev_client import get_trading_signal
from indicators import Indicators

# Lấy tín hiệu giao dịch
signal = get_trading_signal(df, indicators, config)

if signal['buy']:
    print(f"🟢 BUY Signal - Confidence: {signal['confidence']:.2%}")
elif signal['sell']:
    print(f"🔴 SELL Signal - Confidence: {signal['confidence']:.2%}")
else:
    print(f"⚪ HOLD - Confidence: {signal['confidence']:.2%}")

# Lưu kết quả
save_result(df, indicators, signal)
Example Trading Log
============================================================
🤖 AUTO TRADE XAU/USD WITH JEV AI
============================================================
📅 Thời gian: 2026-10-02 02:56:27
📊 Cặp tiền: XAUUSD | Khung: H1
============================================================

🔌 Đang kết nối MT5...
✅ Kết nối MT5 thành công!

📥 Đang lấy dữ liệu giá...
📊 Đã lấy 100 cây nến XAUUSD H1

📊 Đang tính chỉ số kỹ thuật...
🤖 Đang gọi API Jev AI...

🔍 DEBUG Response:
{
  "answers": {
    "is_strong_signal": {"noul": 0.17, "type": "noul"},
    "is_trending": {"noul": 0.49, "type": "noul"},
    "should_buy": {"noul": 0.21, "type": "noul"},
    "should_sell": {"noul": 0.12, "type": "noul"}
  }
}

🎯 TÍN HIỆU GIAO DỊCH TỪ JEV AI
----------------------------------------
📈 Giá hiện tại: 4176.61
📉 RSI: 44.94
📊 MACD: 1.2217
📉 MACD Signal: 0.4179
----------------------------------------
✅ SIGNAL: ⚪ HOLD
🔢 CONFIDENCE: 9.00%
⚠️  RISK LEVEL: MEDIUM
💭 REASONING: Buy: 0.21, Sell: 0.12
----------------------------------------

⏭️  Bỏ qua: Confidence 9.00% < 75.00%

💾 Đã lưu kết quả: results/20261002_025628.json

============================================================
✅ Chương trình kết thúc
============================================================
🔑 Jev AI API Configuration
Getting API Key
Đăng ký tài khoản tại https://www.beatapi.com
Lấy API Key từ dashboard
Thêm vào file config.py:
JEV_API_KEY = "your_actual_api_key_here"
API Response Format
Jev AI System One trả về response theo cấu trúc sau:

{
  "answers": {
    "should_buy": {"noul": 0.21, "type": "noul"},
    "should_sell": {"noul": 0.12, "type": "noul"},
    "is_strong_signal": {"noul": 0.17, "type": "noul"},
    "is_trending": {"noul": 0.49, "type": "noul"}
  },
  "id": "task_...",
  "model": "jev-1.13-free",
  "usage": {"input_tokens": 772, "output_tokens": 76}
}
```

## Understanding noul Values
| Question |	noul | Value	Interpretation
|----------|---------|------------------------
| should_buy|	0.21 |	Low probability of buy
| should_sell |	0.12 |	Very low probability of sell
| is_strong_signal |	0.17 |	Weak signal strength
| is_trending |	0.49 |	Near neutral trend

Logic: Nếu should_buy.noul > 0.5 → Tín hiệu MUA, nếu should_sell.noul > 0.5 → Tín hiệu BÁN, nếu cả hai đều thấp → HOLD.

---

⚠️ ## Risk Disclaimer

⚠️ ## WARNING: Hệ thống giao dịch tự động có thể dẫn đến thiệt hại tài chính đáng kể. Hãy hiểu rõ các rủi ro trước khi sử dụng.

## Key Risks
- Hệ thống không đảm bảo lợi nhuận - chỉ là công cụ hỗ trợ quyết định
- Rủi ro thị trường có thể dẫn đến thua lỗ lớn
- Lỗi kỹ thuật hoặc kết nối mạng có thể gây giao dịch bất ngờ
- Cần giám sát liên tục và sẵn sàng can thiệp thủ công

🛡️ Stop Loss	Luôn đặt lệnh dừng lỗ cho mọi giao dịch

📊 Position Sizing	Chỉ giao dịch 1-2% vốn cho mỗi lệnh

🔄 Diversification	Không tập trung vào một cặp tiền duy nhất

📈 Regular Review	Kiểm tra kết quả giao dịch hàng ngày

🤝 Contributing
## Fork repository

- Create feature branch (git checkout -b feature/amazing-feature)
- Commit changes (git commit -m 'Add amazing feature')
- Push to branch (git push origin feature/amazing-feature)
Open Pull Request
🙏 Acknowledgments

- Jev AI - AI-powered decision making
- MetaTrader 5 - Trading platform
- Pandas - Data analysis
- Requests - HTTP client

📞 Support
Website: https://www.matilda.vn - Email: huynq@isi.com.vn


```
