def build_trade_plan(price, signal):

    if signal == "WAIT":
        return None

    if signal == "WATCHLIST":

        return {
            "entry": round(price - 1.0, 2),
            "sl": round(price - 3.0, 2),
            "tp": round(price + 6.0, 2)
        }

    if signal == "BUY":

        return {
            "entry": round(price - 0.5, 2),
            "sl": round(price - 2.0, 2),
            "tp": round(price + 6.0, 2)
        }

    return None