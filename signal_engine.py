def generate_signal(values, structure, liquidity, fvg, choch, order_block, session):

    score = 0

    # Structure
    if structure == "BULLISH BOS":
        score += 25

    elif structure == "BEARISH BOS":
        score += 25

    # Liquidity
    if liquidity != "NO SWEEP":
        score += 20

    # FVG
    if fvg != "NO FVG":
        score += 20

    # CHOCH
    if choch != "NO CHOCH":
        score += 15

    # Order Block
    if order_block != "NO ORDER BLOCK":
        score += 20

    # Session
    if session == "LONDON":
        score += 15

    elif session == "NEW YORK":
        score += 15

    elif session == "ASIAN":
        score += 10

    # EMA
    if values["ema20"] > values["ema50"]:
        score += 10

    # RSI
    if values["rsi"] > 55:
        score += 10

    if score > 100:
        score = 100

    signal = "WAIT"

    if score >= 85:
        signal = "BUY"

    elif score >= 65:
        signal = "WATCHLIST"

    reasons = []

    if structure != "RANGE":
        reasons.append(structure)

    if liquidity != "NO SWEEP":
        reasons.append(liquidity)

    if fvg != "NO FVG":
        reasons.append(fvg)

    if choch != "NO CHOCH":
        reasons.append(choch)

    if order_block != "NO ORDER BLOCK":
        reasons.append(order_block)

    return score, signal, reasons