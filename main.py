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

print("GoldSniper Starting...")

data = get_gold_data()
structure = detect_structure(data)
liquidity = detect_liquidity_sweep(data)
fvg = detect_fvg(data)


values = calculate_indicators(data)
support, resistance = get_support_resistance(data)

current_session = get_session()

score, signal = generate_signal(
    values,
    structure,
    liquidity,
    fvg,
    current_session
)

trade_plan = build_trade_plan(
    values["price"],
    signal
)

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
print(f'Support      : {support:.2f}')
print(f'Resistance   : {resistance:.2f}')

print(f'\nConfidence Score : {score}%')
print(f'Signal : {signal}')

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