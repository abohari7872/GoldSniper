from mt5_market_data import get_mt5_data
from trend_engine import get_trend
from structure_v2 import detect_structure_v2
from choch_v2 import detect_choch_v2
from fvg_v2 import detect_fvg_v2
from order_block_v2 import detect_order_block_v2


def count_direction(results):
    bullish = 0
    bearish = 0

    for result in results:
        if "BULLISH" in result:
            bullish += 1

        if "BEARISH" in result:
            bearish += 1

    return bullish, bearish


def create_analysis():
    data = get_mt5_data()

    if data is None:
        print("ERROR: MT5 data could not be loaded.")
        return

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
            print(f"ERROR: Missing timeframe: {timeframe}")
            return

        if data[timeframe].empty:
            print(f"ERROR: No candles received for: {timeframe}")
            return

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

    choch_results = {
        "H1": detect_choch_v2(data["H1"]),
        "M15": detect_choch_v2(data["M15"]),
        "M5": detect_choch_v2(data["M5"]),
        "M1": detect_choch_v2(data["M1"]),
    }

    fvg_results = {
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

    higher_timeframe_results = [
        trends["MN1"],
        trends["D1"],
        trends["H4"],
        trends["H1"],
    ]

    setup_results = [
        structures["H1"],
        structures["M15"],
        choch_results["H1"],
        choch_results["M15"],
        fvg_results["H1"],
        fvg_results["M15"],
        order_blocks["H1"],
        order_blocks["M15"],
    ]

    entry_results = [
        structures["M5"],
        choch_results["M5"],
        choch_results["M1"],
        fvg_results["M5"],
        fvg_results["M1"],
        order_blocks["M5"],
        order_blocks["M1"],
    ]

    htf_bullish, htf_bearish = count_direction(
        higher_timeframe_results
    )

    setup_bullish, setup_bearish = count_direction(
        setup_results
    )

    entry_bullish, entry_bearish = count_direction(
        entry_results
    )

    decision = "WAIT"
    explanation = "Timeframes are not sufficiently aligned."

    if (
        htf_bullish >= 3
        and setup_bullish >= 5
        and entry_bullish >= 4
    ):
        decision = "POTENTIAL BUY SETUP"
        explanation = (
            "Higher timeframe, setup timeframe, and entry "
            "timeframe conditions are predominantly bullish."
        )

    elif (
        htf_bearish >= 3
        and setup_bearish >= 5
        and entry_bearish >= 4
    ):
        decision = "POTENTIAL SELL SETUP"
        explanation = (
            "Higher timeframe, setup timeframe, and entry "
            "timeframe conditions are predominantly bearish."
        )

    current_price = float(data["M1"]["close"].iloc[-1])

    print()
    print("========================================")
    print("        GOLDSNIPER MT5 ANALYSIS")
    print("========================================")
    print()
    print(f"Symbol        : GOLD.i#")
    print(f"Current Price : {current_price:.2f}")

    print()
    print("HIGHER TIMEFRAME TREND")
    print("----------------------------------------")
    print(f"Monthly : {trends['MN1']}")
    print(f"Daily   : {trends['D1']}")
    print(f"H4      : {trends['H4']}")
    print(f"H1      : {trends['H1']}")

    print()
    print("MARKET STRUCTURE")
    print("----------------------------------------")
    print(f"H4      : {structures['H4']}")
    print(f"H1      : {structures['H1']}")
    print(f"M15     : {structures['M15']}")
    print(f"M5      : {structures['M5']}")

    print()
    print("CHANGE OF CHARACTER")
    print("----------------------------------------")
    print(f"H1      : {choch_results['H1']}")
    print(f"M15     : {choch_results['M15']}")
    print(f"M5      : {choch_results['M5']}")
    print(f"M1      : {choch_results['M1']}")

    print()
    print("FAIR VALUE GAPS")
    print("----------------------------------------")
    print(f"H1      : {fvg_results['H1']}")
    print(f"M15     : {fvg_results['M15']}")
    print(f"M5      : {fvg_results['M5']}")
    print(f"M1      : {fvg_results['M1']}")

    print()
    print("ORDER BLOCKS")
    print("----------------------------------------")
    print(f"H1      : {order_blocks['H1']}")
    print(f"M15     : {order_blocks['M15']}")
    print(f"M5      : {order_blocks['M5']}")
    print(f"M1      : {order_blocks['M1']}")

    print()
    print("DIRECTION COUNTS")
    print("----------------------------------------")
    print(
        f"Higher TF     : "
        f"{htf_bullish} bullish / {htf_bearish} bearish"
    )
    print(
        f"Setup Layer   : "
        f"{setup_bullish} bullish / {setup_bearish} bearish"
    )
    print(
        f"Entry Layer   : "
        f"{entry_bullish} bullish / {entry_bearish} bearish"
    )

    print()
    print("FINAL STATUS")
    print("----------------------------------------")
    print(f"Decision      : {decision}")
    print(f"Explanation   : {explanation}")
    print()
    print("DEMO OBSERVATION ONLY")
    print("No automatic order should be placed.")
    print("========================================")


if __name__ == "__main__":
    create_analysis()