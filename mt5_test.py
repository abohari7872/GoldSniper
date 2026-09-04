import MetaTrader5 as mt5

if not mt5.initialize():
    print("MT5 connection failed")
else:
    print("MT5 connected successfully")

    symbols = mt5.symbols_get()

    print(f"Symbols found: {len(symbols)}")

    mt5.shutdown()