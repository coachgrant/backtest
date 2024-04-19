import vectorbt as vbt
import datetime

end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days = 3)

btc_price = vbt.YFData.download(
    'BTC-USD', #can make a list of multiple symbols []
    interval = '1m',
    start = start_date,
    end = end_date,
    missing_index='drop').get('Close')

#print(btc_price)

rsi = vbt.RSI.run(btc_price, window =14) #can optimize with a list [14,21 ] of multiple windows
#print(rsi.rsi)

entries = rsi.rsi_crossed_below(30)
#print(entries.to_string())
exits = rsi.rsi_crossed_above(70)

pf = vbt.Portfolio.from_signals(btc_price, entries, exits)
#print(pf.stats())
#print(pf.total_return())
pf.plot().show()