from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator

def calculate_indicators(data):

    close_prices = data["Close"]

    ema20 = EMAIndicator(close_prices, window=20).ema_indicator()
    ema50 = EMAIndicator(close_prices, window=50).ema_indicator()
    ema200 = EMAIndicator(close_prices, window=200).ema_indicator()

    rsi = RSIIndicator(close_prices, window=14).rsi()

    return {
        "price": close_prices.iloc[-1],
        "ema20": ema20.iloc[-1],
        "ema50": ema50.iloc[-1],
        "ema200": ema200.iloc[-1],
        "rsi": rsi.iloc[-1]
    }