# mt5_connector.py
import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MT5Connector:
    def __init__(self, config):
        self.config = config
        self.initialize()

    def initialize(self):
        """Khởi tạo kết nối MT5"""
        if not mt5.initialize(self.config.mt5_path):
            logger.error(f"Khởi tạo MT5 thất bại: {mt5.last_error()}")
            raise ConnectionError("Không thể kết nối MT5")

        # Đăng nhập
        authorized = mt5.login(
            self.config.mt5_login,
            self.config.mt5_password,
            self.config.mt5_server
        )

        if not authorized:
            logger.error(f"Đăng nhập MT5 thất bại: {mt5.last_error()}")
            raise PermissionError("Đăng nhập không thành công")

        logger.info("✅ Kết nối MT5 thành công!")

    def get_rates(self):
        """Lấy dữ liệu giá từ MT5"""
        rates = mt5.copy_rates_from_pos(
            self.config.symbol,
            self._get_timeframe_value(),
            0,
            self.config.num_bars
        )

        if rates is None or len(rates) == 0:
            logger.error("Không lấy được dữ liệu giá")
            return None

        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')

        logger.info(f"📊 Đã lấy {len(df)} cây nến {self.config.symbol} {self.config.timeframe}")
        return df

    def _get_timeframe_value(self):
        """Chuyển đổi tên timeframe sang giá trị số"""
        timeframes = {
            "M1": mt5.TIMEFRAME_M1,
            "M5": mt5.TIMEFRAME_M5,
            "M15": mt5.TIMEFRAME_M15,
            "M30": mt5.TIMEFRAME_M30,
            "H1": mt5.TIMEFRAME_H1,
            "H4": mt5.TIMEFRAME_H4,
            "D1": mt5.TIMEFRAME_D1,
        }
        return timeframes.get(self.config.timeframe, mt5.TIMEFRAME_H1)

    def shutdown(self):
        """Đóng kết nối MT5"""
        mt5.shutdown()
        logger.info("❌ Đã đóng kết nối MT5")
