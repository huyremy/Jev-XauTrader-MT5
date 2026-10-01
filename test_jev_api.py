# test_jev_api.py
import requests
import json
from config import JEV_API_KEY, JEV_API_URL, JEV_MODEL

def test_jev_api():
    """Test API Jev AI trực tiếp để xem response format"""

    # Sample state và questions
    state = """XAU/USD Price Action Analysis:
- Current Price: 4176.35
- Timeframe: H1
- Market Context:
  • Trend: Bullish
  • RSI: 44.83
  • MACD: 1.2010 vs Signal: 0.4138
  • MACD Histogram: 0.7872
  • Volume: 1523
"""

    questions = {
        "should_buy": {
            "type": "noul",
            "instructions": "Determine if XAU/USD price action indicates a BUY signal.",
            "criteria": {
                "true": "Strong bullish momentum",
                "false": "Bearish or neutral"
            }
        },
        "should_sell": {
            "type": "noul",
            "instructions": "Determine if XAU/USD price action indicates a SELL signal.",
            "criteria": {
                "true": "Strong bearish momentum",
                "false": "Bullish or neutral"
            }
        }
    }

    payload = {
        "model": JEV_MODEL,
        "state": state,
        "questions": questions
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {JEV_API_KEY}"
    }

    print("🔌 Đang gọi API Jev AI...")
    print(f"📡 Payload: {json.dumps(payload, indent=2)}")

    try:
        response = requests.post(
            JEV_API_URL,
            json=payload,
            headers=headers,
            timeout=30
        )
        response.raise_for_status()

        result = response.json()

        print(f"\n✅ Response từ API:")
        print(json.dumps(result, indent=2, ensure_ascii=False))

        # Phân tích response
        print(f"\n📊 Phân tích response:")
        for key, value in result.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                print(f"    - answer: {value.get('answer')}")
                print(f"    - confidence: {value.get('confidence')}")
                print(f"    - reasoning: {value.get('reasoning')}")
            else:
                print(f"  {key}: {value}")

    except Exception as e:
        print(f"❌ Lỗi: {e}")

if __name__ == "__main__":
    test_jev_api()
