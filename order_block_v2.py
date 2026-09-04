def detect_order_block_v2(data, displacement_threshold=5.0):
    required_columns = {"open", "close"}

    if not required_columns.issubset(data.columns):
        return "NO ORDER BLOCK"

    candles = data.tail(20).reset_index(drop=True)

    if len(candles) < 4:
        return "NO ORDER BLOCK"

    for i in range(len(candles) - 4, -1, -1):
        candle_open = float(candles.loc[i, "open"])
        candle_close = float(candles.loc[i, "close"])
        future_close = float(candles.loc[i + 3, "close"])

        # Last bearish candle before bullish displacement
        if candle_close < candle_open:
            bullish_move = future_close - candle_close

            if bullish_move > displacement_threshold:
                return "BULLISH ORDER BLOCK"

        # Last bullish candle before bearish displacement
        if candle_close > candle_open:
            bearish_move = candle_close - future_close

            if bearish_move > displacement_threshold:
                return "BEARISH ORDER BLOCK"

    return "NO ORDER BLOCK"