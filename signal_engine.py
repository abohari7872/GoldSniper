def generate_signal(values, structure, liquidity, fvg, session):

    score = 0

    # Structure
    if structure == "BULLISH BOS":
        score += 25

    if structure == "BEARISH BOS":
        score += 25

    # Liquidity
    if liquidity != "NO SWEEP":
        score += 20

    # FVG
    if fvg != "NO FVG":
        score += 20

    # Session
    if session == "LONDON":
        score += 15

    elif session == "NEW YORK":
        score += 15

    elif session == "ASIAN":
        score += 10

    # EMA Filter
    if values["ema20"] > values["ema50"]:
        score += 10

    # RSI Filter
    if values["rsi"] > 55:
        score += 10

    signal = "WAIT"

    if score >= 80:
        signal = "BUY"

    elif score >= 60:
        signal = "WATCHLIST"

    else:
        signal = "WAIT"

    return score, signal