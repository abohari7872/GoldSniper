def detect_structure_v2(data):

    highs = data["high"].tail(20).tolist()
    lows = data["low"].tail(20).tolist()

    recent_high = max(highs[:-5])
    recent_low = min(lows[:-5])

    current_high = highs[-1]
    current_low = lows[-1]

    if current_high > recent_high:
        return "BULLISH BOS"

    if current_low < recent_low:
        return "BEARISH BOS"

    return "RANGE"