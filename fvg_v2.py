def detect_fvg_v2(data):

    candles = data.tail(10)

    highs = candles["high"].tolist()
    lows = candles["low"].tolist()

    for i in range(len(candles) - 2):

        first_high = highs[i]
        first_low = lows[i]

        third_high = highs[i + 2]
        third_low = lows[i + 2]

        # Bullish FVG
        if third_low > first_high:

            gap = third_low - first_high

            if gap > 1:
                return "BULLISH FVG"

        # Bearish FVG
        if third_high < first_low:

            gap = first_low - third_high

            if gap > 1:
                return "BEARISH FVG"

    return "NO FVG"