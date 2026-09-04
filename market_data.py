import yfinance as yf

def get_gold_data():

    gold = yf.Ticker("GC=F")

    data = gold.history(
        period="5d",
        interval="5m"
    )

    return data