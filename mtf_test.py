from mt5_market_data import get_mt5_data

data = get_mt5_data()

for tf in data:

    print(
        tf,
        len(data[tf])
    )