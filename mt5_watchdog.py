import time
from datetime import datetime

import MetaTrader5 as mt5

from telegram_engine import send_signal


SYMBOL = "GOLD.i#"

CHECK_INTERVAL_SECONDS = 60

MAX_TICK_AGE_SECONDS = 180


def get_connection_status():

    if not mt5.initialize():

        return (
            False,
            f"MT5 initialization failed: {mt5.last_error()}"
        )

    terminal = mt5.terminal_info()

    account = mt5.account_info()

    if terminal is None:

        return (
            False,
            "MT5 terminal information is unavailable."
        )

    if account is None:

        return (
            False,
            "XM account is not logged in."
        )

    if not terminal.connected:

        return (
            False,
            "MT5 terminal is disconnected from the broker."
        )

    if not mt5.symbol_select(SYMBOL, True):

        return (
            False,
            f"Symbol {SYMBOL} could not be selected."
        )

    tick = mt5.symbol_info_tick(SYMBOL)

    if tick is None:

        return (
            False,
            f"No live tick is available for {SYMBOL}."
        )

    tick_age = int(
        time.time() - tick.time
    )

    if tick_age > MAX_TICK_AGE_SECONDS:

        return (
            False,
            f"The latest {SYMBOL} tick is "
            f"{tick_age} seconds old."
        )

    message = (
        f"XM MT5 connected | "
        f"Account: {account.login} | "
        f"{SYMBOL} bid: {tick.bid:.2f} | "
        f"ask: {tick.ask:.2f}"
    )

    return True, message


def main():

    previous_status = None

    connected, details = get_connection_status()

    previous_status = connected

    if connected:

        send_signal(
            "GOLDSNIPER ONLINE\n\n"
            f"{details}\n"
            "Monitoring mode: DEMO\n"
            "Live XM MT5 watchdog started."
        )

    else:

        send_signal(
            "GOLDSNIPER OFFLINE\n\n"
            f"Reason: {details}"
        )

    print(
        f"{datetime.now().isoformat(timespec='seconds')} | "
        f"{details}"
    )

    try:

        while True:

            time.sleep(
                CHECK_INTERVAL_SECONDS
            )

            connected, details = (
                get_connection_status()
            )

            if connected != previous_status:

                if connected:

                    send_signal(
                        "GOLDSNIPER RECONNECTED\n\n"
                        f"{details}"
                    )

                else:

                    send_signal(
                        "GOLDSNIPER OFFLINE\n\n"
                        f"Reason