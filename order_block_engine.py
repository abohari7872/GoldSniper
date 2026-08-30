def detect_order_block(data):

    candles = data.tail(10)

    open_price = candles["Open"].tolist()
    close_price = candles["Close"].tolist()

    for i in range(len(candles) - 2, -1, -1):

        # Bullish Order Block
        if close_price[i] < open_price[i]:
            return "BULLISH ORDER BLOCK"

        # Bearish Order Block
        if close_price[i] > open_price[i]:
            return "BEARISH ORDER BLOCK"

    return "NO ORDER BLOCK"