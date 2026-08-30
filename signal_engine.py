def generate_signal(values, structure, liquidity, fvg, choch, session):

    score = 0

    # Structure (BOS)
    if structure == "BULLISH BOS":
        score += 25

    elif structure == "BEARISH BOS":
        score += 25

    # Liquidity Sweep
    if liquidity != "NO SWEEP":
        score += 20

    # FVG
    if fvg != "NO FVG":
        score += 20

    # CHOCH
    if choch != "NO CHOCH":
        score += 15

    # Session Score
    if session == "LONDON":
        score += 15

    elif session == "NEW YORK":
        score += 15

    elif session == "ASIAN":
        score += 10

    # EMA Confirmation
    if values["ema20"] > values["ema50"]:
        score += 10

    # RSI Confirmation
    if values["rsi"] > 55:
        score += 10

    # Default Signal
    signal = "WAIT"

    if score >= 85:
        signal = "BUY"

    elif score >= 65:
        signal = "WATCHLIST"

    else:
        signal = "WAIT"

    return score, signal