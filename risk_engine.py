def validate_trade(entry, stop_loss, take_profit):

    risk = abs(entry - stop_loss)
    reward = abs(take_profit - entry)

    rr = reward / risk

    valid = True

    if risk > 20:
        valid = False

    if reward < 60:
        valid = False

    if rr < 3:
        valid = False

    return {
        "risk": risk,
        "reward": reward,
        "rr": rr,
        "valid": valid
    }
