# import KEY
# import ccxt


# binance = ccxt.binance({
#     'apiKey' : KEY.key('api'),
#     'secret' : KEY.key('sct'),
# })

# # order = binance.create_limit_buy_order('ETH/USDT', 10, 2000)
# # print(order)
# # for ohlc in ohlcvs:
#     # print(datetime.fromtimestamp(ohlc[0]/1000).strftime('%Y-%m-%d %H:%M:%S'), ohlc[1])

# markets = binance.fetch_tickers()
# print(markets.keys())

import talib
import numpy


c = numpy.random.randn(100)

print(c)
# this is the library function
k, d = talib.STOCHRSI(c)
print(k,d)

# this produces the same result, calling STOCHF
rsi = talib.RSI(c)
k, d = talib.STOCHF(rsi, rsi, rsi)



# you might want this instead, calling STOCH
rsi = talib.RSI(c)
k, d = talib.STOCH(rsi, rsi, rsi)