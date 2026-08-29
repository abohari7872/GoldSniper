def detect_liquidity_sweep(data):

    highs = data["High"].tail(20).tolist()
    lows = data["Low"].tail(20).tolist()

    current_high = highs[-1]
    current_low = lows[-1]

    previous_high = max(highs[:-1])
    previous_low = min(lows[:-1])

    if current_high > previous_high:
        return "BUY SIDE LIQUIDITY TAKEN"

    if current_low < previous_low:
        return "SELL SIDE LIQUIDITY TAKEN"

    return "NO SWEEP"