def detect_structure(data):

    highs = data["High"].tail(10).tolist()
    lows = data["Low"].tail(10).tolist()

    recent_high = max(highs[:-1])
    current_high = highs[-1]

    recent_low = min(lows[:-1])
    current_low = lows[-1]

    structure = "RANGE"

    if current_high > recent_high:
        structure = "BULLISH BOS"

    elif current_low < recent_low:
        structure = "BEARISH BOS"

    return structure