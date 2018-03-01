from yahoo_finance import Share

stocks = [
    'YHOO',
    'AAPL',
    'AMAT',
    'TSM',
    'MSFT',
    'SPY'
]

for s in stocks:
    stock = Share(s)
    print(stock.get_open())
