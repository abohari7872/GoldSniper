from mt5_market_data import get_mt5_data
from trend_engine import get_trend

data = get_mt5_data()

print()

print("===== GOLD TREND =====")

print()

print("Monthly :", get_trend(data["MN1"]))

print("Daily   :", get_trend(data["D1"]))

print("H4      :", get_trend(data["H4"]))

print("H1      :", get_trend(data["H1"]))