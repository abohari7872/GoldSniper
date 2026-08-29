def get_support_resistance(data):

    recent_lows = data["Low"].tail(50)
    recent_highs = data["High"].tail(50)

    support = recent_lows.min()
    resistance = recent_highs.max()

    return support, resistance