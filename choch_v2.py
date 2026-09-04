def detect_choch_v2(data):

    highs = data["high"].tail(30).tolist()
    lows = data["low"].tail(30).tolist()

    recent_high = max(highs[:-10])
    recent_low = min(lows[:-10])

    current_high = highs[-1]
    current_low = lows[-1]

    if current_high > recent_high:
        return "BULLISH CHOCH"

    if current_low < recent_low:
        return "BEARISH CHOCH"

    return "NO CHOCH"