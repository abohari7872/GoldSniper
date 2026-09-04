from mt5_market_data import get_mt5_data
from structure_v2 import detect_structure_v2

data = get_mt5_data()

print()

print("===== STRUCTURE =====")

print()

print("H4  :", detect_structure_v2(data["H4"]))
print("H1  :", detect_structure_v2(data["H1"]))
print("M15 :", detect_structure_v2(data["M15"]))
print("M5  :", detect_structure_v2(data["M5"]))