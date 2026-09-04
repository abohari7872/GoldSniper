import MetaTrader5 as mt5
import pandas as pd


def get_mt5_data():

    if not mt5.initialize():
        return None

    symbol = "GOLD.i#"

    data = {

        "M1": pd.DataFrame(
            mt5.copy_rates_from_pos(
                symbol,
                mt5.TIMEFRAME_M1,
                0,
                500
            )
        ),

        "M5": pd.DataFrame(
            mt5.copy_rates_from_pos(
                symbol,
                mt5.TIMEFRAME_M5,
                0,
                500
            )
        ),

        "M15": pd.DataFrame(
            mt5.copy_rates_from_pos(
                symbol,
                mt5.TIMEFRAME_M15,
                0,
                500
            )
        ),

        "M30": pd.DataFrame(
            mt5.copy_rates_from_pos(
                symbol,
                mt5.TIMEFRAME_M30,
                0,
                500
            )
        ),

        "H1": pd.DataFrame(
            mt5.copy_rates_from_pos(
                symbol,
                mt5.TIMEFRAME_H1,
                0,
                500
            )
        ),

        "H4": pd.DataFrame(
            mt5.copy_rates_from_pos(
                symbol,
                mt5.TIMEFRAME_H4,
                0,
                500
            )
        ),

        "D1": pd.DataFrame(
            mt5.copy_rates_from_pos(
                symbol,
                mt5.TIMEFRAME_D1,
                0,
                500
            )
        ),

        "MN1": pd.DataFrame(
            mt5.copy_rates_from_pos(
                symbol,
                mt5.TIMEFRAME_MN1,
                0,
                500
            )
        )
    }

    return data
