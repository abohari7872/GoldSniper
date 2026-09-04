import MetaTrader5 as mt5
import pandas as pd

if not mt5.initialize():
    print("Connection Failed")
    quit()

symbol = "GOLD.i#"

rates = mt5.copy_rates_from_pos(
    symbol,
    mt5.TIMEFRAME_H1,
    0,
    10
)

df = pd.DataFrame(rates)

print(df[["open", "high", "low", "close"]])

mt5.shutdown()