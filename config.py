# config.py
import os

# Cấu hình MT5
MT5_PATH = "C:/Program Files/MetaTrader 5/terminal64.exe"  # Đường dẫn MT5 terminal, None = auto detect
MT5_LOGIN = 5056xxxx  # Số tài khoản demo
MT5_PASSWORD = "ZeBxxxx"
MT5_SERVER = "MetaQuotes-Demo"  # Ví dụ: "MetaQuotes-Demo"

# Cấu hình Jev AI
JEV_MODEL = "jev-1.13-free"  # Model ID
JEV_API_KEY = "sk-"  
JEV_API_URL = "https://api.beatapi.io/v1/systemone"  # Endpoint BeatAPI

# Cấu hình giao dịch
SYMBOL = "XAUUSD"  # Vàng/Đô la Mỹ
TIMEFRAME = "H1"   # Khung 1 giờ
NUM_BARS = 100     # Số cây nến lấy về

# Ngưỡng quyết định
CONFIDENCE_THRESHOLD = 0.75  # Chỉ giao dịch khi confidence > 75%