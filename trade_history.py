trade_history = []

def add_trade(signal, price, confidence):

    trade_history.append({
        "signal": signal,
        "price": price,
        "confidence": confidence
    })

def get_trade_count():
    return len(trade_history)