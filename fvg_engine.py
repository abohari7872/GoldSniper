def detect_fvg(data):

    candles = data.tail(5)

    highs = candles["High"].tolist()
    lows = candles["Low"].tolist()

    # Bullish FVG
    if lows[2] > highs[0]:
        return "BULLISH FVG"

    # Bearishighs[2] < lows[0]:
        return "BEARISH FVG"

    return "NO FVG"
