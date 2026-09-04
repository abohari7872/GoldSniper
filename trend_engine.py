def get_trend(data):

    closes = data["close"]

    latest = closes.iloc[-1]

    average = closes.tail(50).mean()

    if latest > average:
        return "BULLISH"

    if latest < average:
        return "BEARISH"

    return "NEUTRAL"