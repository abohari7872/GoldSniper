from mt5_market_data import get_mt5_data
from order_block_v2 import detect_order_block_v2

data = get_mt5_data()

print()

print("===== ORDER BLOCK =====")

print()

print("H1  :", detect_order_block_v2(data["H1"]))
print("M15 :", detect_order_block_v2(data["M15"]))
print("M5  :", detect_order_block_v2(data["M5"]))
print("M1  :", detect_order_block_v2(data["M1"]))