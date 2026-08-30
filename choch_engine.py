def detect_choch(data):

    highs = data["High"].tail(20).tolist()
    lows = data["Low"].tail(20).tolist()

    latest_high = highs[-1]
    latest_low = lows[-1]

    previous_high = highs[-5]
    previous_low = lows[-5]

    if latest_high > previous_high:
        return "BULLISH CHOCH"

    if latest_low < previous_low:
        return "BEARISH CHOCH"

    return "NO CHOCH"