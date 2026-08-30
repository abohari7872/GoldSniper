def build_trade_plan(price, signal, support, resistance):

    if signal == "WAIT":
        return None

    entry = round(price - 2.0, 2)

    sl = round(entry - 2.0, 2)

    tp = round(entry + 6.0, 2)

    return {
        "entry": entry,
        "sl": sl,
        "tp": tp,
        "status": "WAIT FOR ENTRY"
    }