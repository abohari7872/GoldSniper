from market_data import get_gold_data
from indicators import calculate_indicators
from signal_engine import generate_signal
from risk_engine import validate_trade
from support_resistance import get_support_resistance
from session_engine import get_session
from structure_engine import detect_structure
from liquidity_engine import detect_liquidity_sweep
from fvg_engine import detect_fvg
from trade_planner import build_trade_plan
from choch_engine import detect_choch
from order_block_engine import detect_order_block
from daily_target import check_daily_target
from trade_history import add_trade
from trade_history import get_trade_count
from trade_history import can_take_trade
from telegram_engine import send_signal

print("GoldSniper Starting...")

data = get_gold_data()
structure = detect_structure(data)
liquidity = detect_liquidity_sweep(data)
fvg = detect_fvg(data)
choch = detect_choch(data)
order_block = detect_order_block(data)


values = calculate_indicators(data)
support, resistance = get_support_resistance(data)

current_session = get_session()

score, signal, reasons = generate_signal(
    values,
    structure,
    liquidity,
    fvg,
    choch,
    order_block,
    current_session
)

if not can_take_trade():
    signal = "MAX TRADES REACHED"

if signal == "BUY":

    add_trade(
        signal,
        values["price"],
        score
    )

    send_signal(
        f"""
GoldSniper BUY Signal

Price: {values["price"]:.2f}

Confidence: {score}%

Reasons:
{chr(10).join("✅ " + r for r in reasons)}
"""
    )

trade_plan = build_trade_plan(
    values["price"],
    signal
)

today_pips = 65

daily_status = check_daily_target(today_pips)

print("\n===== GOLDSNIPER =====")

print(f'Current Price : {values["price"]:.2f}')
print(f'EMA20         : {values["ema20"]:.2f}')
print(f'EMA50         : {values["ema50"]:.2f}')
print(f'EMA200        : {values["ema200"]:.2f}')
print(f'RSI           : {values["rsi"]:.2f}')
print(f"Session       : {current_session}")
print(f"Structure     : {structure}")
print(f"Liquidity     : {liquidity}")
print(f"FVG           : {fvg}")
print(f"CHOCH         : {choch}")
print(f"Order Block   : {order_block}")
print(f'Support      : {support:.2f}')
print(f'Resistance   : {resistance:.2f}')

print(f'\nConfidence Score : {score}%')
print(f'Signal : {signal}')

print("\nReasons:")

for reason in reasons:
    print(f"✅ {reason}")

print("\n===== DAILY TARGET =====")
print(f"Today's Pips : {today_pips}")
print(f"Status       : {daily_status}")
print(f"Trades Today : {get_trade_count()}")

if trade_plan:

    print("\n===== TRADE PLAN =====")

    print(f'Entry Zone : {trade_plan["entry"]}')
    print(f'SL         : {trade_plan["sl"]}')
    print(f'TP         : {trade_plan["tp"]}')

print("\n===== RISK TEST =====")

entry = 4525
sl = 4510
tp = 4585

trade = validate_trade(entry, sl, tp)

print(f"Entry  : {entry}")
print(f"SL     : {sl}")
print(f"TP     : {tp}")

print(f"Risk   : {trade['risk']}")
print(f"Reward : {trade['reward']}")
print(f"RR     : {trade['rr']:.2f}")

if trade["valid"]:
    print("Trade Approved ✅")
else:
    print("Trade Rejected ❌")