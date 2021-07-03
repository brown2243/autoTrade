import websocket, json, pprint, talib, numpy
import config
from binance.client import Client
from datetime import datetime

client = Client(config.API_KEY, config.API_SECRET, tld='com')

# status = client.get_system_status()
# input_klines = map(str, input.split(' '))

# klines_spot = json.loads(json.dumps(client._historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1MONTH, "1 Jan, 2021", None,1000,"SPOT"), indent=4))
klines_spot = json.loads(json.dumps(client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2021", None,1000), indent=4))
klines_furture = json.loads(json.dumps(client.futures_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2021", None, 1000), indent=4))

# print(client.ping())
# print(client.get_server_time())



# print("klines_spot", len(klines_spot))
# print("klines_furture", len(klines_furture))
for i in range(len(klines_spot)):
    # print(datetime.fromtimestamp(klines_spot[i][0]),":",round(float(klines_furture[i][1]) / float(klines_spot[i][1]), 5))
    print(datetime.fromtimestamp(klines_spot[i][0]/1000),":",round(float(klines_furture[i][1]) / float(klines_spot[i][1]), 5))
# info = client.get_all_tickers()
# print(info)