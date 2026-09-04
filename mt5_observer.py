import csv
import os
import time
from datetime import datetime

from mt5_market_data import get_mt5_data
from trend_engine import get_trend
from structure_v2 import detect_structure_v2
from choch_v2 import detect_choch_v2
from fvg_v2 import detect_fvg_v2
from order_block_v2 import detect_order_block_v2


LOG_FILE = "mt5_observations.csv"
CHECK_INTERVAL_SECONDS = 300


def count_direction(results):
    bullish = 0
    bearish = 0

    for result in results:
        if "BULLISH" in result:
            bullish += 1

        if "BEARISH" in result:
            bearish += 1

    return bullish, bearish


def get_snapshot():
    data = get_mt5_data()

    if data is None:
        raise RuntimeError("MT5 data could not be loaded.")

    required_timeframes = [
        "M1",
        "M5",
        "M15",
        "M30",
        "H1",
        "H4",
        "D1",
        "MN1",
    ]

    for timeframe in required_timeframes:
        if timeframe not in data:
            raise RuntimeError(
                f"Missing timeframe: {timeframe}"
            )

        if data[timeframe].empty:
            raise RuntimeError(
                f"No candles received for: {timeframe}"
            )

    trends = {
        "MN1": get_trend(data["MN1"]),
        "D1": get_trend(data["D1"]),
        "H4": get_trend(data["H4"]),
        "H1": get_trend(data["H1"]),
    }

    structures = {
        "H4": detect_structure_v2(data["H4"]),
        "H1": detect_structure_v2(data["H1"]),
        "M15": detect_structure_v2(data["M15"]),
        "M5": detect_structure_v2(data["M5"]),
    }

    choch = {
        "H1": detect_choch_v2(data["H1"]),
        "M15": detect_choch_v2(data["M15"]),
        "M5": detect_choch_v2(data["M5"]),
        "M1": detect_choch_v2(data["M1"]),
    }

    fvg = {
        "H1": detect_fvg_v2(data["H1"]),
        "M15": detect_fvg_v2(data["M15"]),
        "M5": detect_fvg_v2(data["M5"]),
        "M1": detect_fvg_v2(data["M1"]),
    }

    order_blocks = {
        "H1": detect_order_block_v2(data["H1"]),
        "M15": detect_order_block_v2(data["M15"]),
        "M5": detect_order_block_v2(data["M5"]),
        "M1": detect_order_block_v2(data["M1"]),
    }

    higher_results = [
        trends["MN1"],
        trends["D1"],
        trends["H4"],
        trends["H1"],
    ]

    setup_results = [
        structures["H1"],
        structures["M15"],
        choch["H1"],
        choch["M15"],
        fvg["H1"],
        fvg["M15"],
        order_blocks["H1"],
        order_blocks["M15"],
    ]

    entry_results = [
        structures["M5"],
        choch["M5"],
        choch["M1"],
        fvg["M5"],
        fvg["M1"],
        order_blocks["M5"],
        order_blocks["M1"],
    ]

    htf_bullish, htf_bearish = count_direction(
        higher_results
    )

    setup_bullish, setup_bearish = count_direction(
        setup_results
    )

    entry_bullish, entry_bearish = count_direction(
        entry_results
    )

    decision = "WAIT"

    if (
        htf_bullish >= 3
        and setup_bullish >= 5
        and entry_bullish >= 4
    ):
        decision = "POTENTIAL BUY SETUP"

    elif (
        htf_bearish >= 3
        and setup_bearish >= 5
        and entry_bearish >= 4
    ):
        decision = "POTENTIAL SELL SETUP"

    return {
        "timestamp": datetime.now().isoformat(
            timespec="seconds"
        ),
        "symbol": "GOLD.i#",
        "price": round(
            float(data["M1"]["close"].iloc[-1]),
            2
        ),
        "monthly_trend": trends["MN1"],
        "daily_trend": trends["D1"],
        "h4_trend": trends["H4"],
        "h1_trend": trends["H1"],
        "h1_structure": structures["H1"],
        "m15_structure": structures["M15"],
        "m5_structure": structures["M5"],
        "h1_choch": choch["H1"],
        "m15_choch": choch["M15"],
        "m5_choch": choch["M5"],
        "m1_choch": choch["M1"],
        "h1_fvg": fvg["H1"],
        "m15_fvg": fvg["M15"],
        "m5_fvg": fvg["M5"],
        "m1_fvg": fvg["M1"],
        "h1_order_block": order_blocks["H1"],
        "m15_order_block": order_blocks["M15"],
        "m5_order_block": order_blocks["M5"],
        "m1_order_block": order_blocks["M1"],
        "htf_bullish": htf_bullish,
        "htf_bearish": htf_bearish,
        "setup_bullish": setup_bullish,
        "setup_bearish": setup_bearish,
        "entry_bullish": entry_bullish,
        "entry_bearish": entry_bearish,
        "decision": decision,
    }


def save_snapshot(snapshot):
    file_exists = os.path.exists(LOG_FILE)

    with open(
        LOG_FILE,
        "a",
        newline="",
        encoding="utf-8",
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=snapshot.keys(),
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(snapshot)


def main():
    print("GoldSniper MT5 Observer started.")
    print("A snapshot will be saved every 5 minutes.")
    print("Press Ctrl + C to stop.")

    while True:
        try:
            snapshot = get_snapshot()
            save_snapshot(snapshot)

            print()
            print(
                f'{snapshot["timestamp"]} | '
                f'Price: {snapshot["price"]} | '
                f'Decision: {snapshot["decision"]}'
            )

        except Exception as error:
            print()
            print(f"Observer error: {error}")

        time.sleep(CHECK_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()

    def main():
     print("GoldSniper MT5 Observer started.")
     print("A snapshot will be saved every 5 minutes.")
     print("Press Ctrl + C to stop.")

    try:
        while True:
            try:
                snapshot = get_snapshot()
                save_snapshot(snapshot)

                print()
                print(
                    f'{snapshot["timestamp"]} | '
                    f'Price: {snapshot["price"]} | '
                    f'Decision: {snapshot["decision"]}'
                )

            except Exception as error:
                print()
                print(f"Observer error: {error}")

            time.sleep(CHECK_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        print()
        print("GoldSniper MT5 Observer stopped safely.")


if __name__ == "__main__":
    main()