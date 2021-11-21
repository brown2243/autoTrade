from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import websocket, json, pprint, talib, numpy
import config
from binance.client import Client
from datetime import date, datetime
import backtrader as bt
import pandas as pd
import numpy as np


def main():
    client = Client(config.API_KEY, config.API_SECRET, tld='com')
    # 데이터 가져오기
    klines_spot = json.loads(json.dumps(client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, "1 Jul, 2021", None, 1000), indent=4))
    # klines_furture = json.loads(json.dumps(client.futures_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2021", None, 1000), indent=4))

    # 데이터 pandas frame에 넣기
    idx = []
    open = []
    high = []
    low = []
    close = []
    volume = []

    for i in range(len(klines_spot)):
        idx.append((klines_spot[i][0]))
        open.append(klines_spot[i][1])
        high.append(klines_spot[i][2])
        low.append(klines_spot[i][3])
        close.append(klines_spot[i][4])
        volume.append(klines_spot[i][5])


    klines_spot_data = {

        0:open,
        1:high,
        2:low,
        3:close,
        4:volume
    }

    pd_klines_spot_data = pd.DataFrame(klines_spot_data, index=idx)
    print(pd_klines_spot_data)
    
    # # # 백트레이더스

    cerebro = bt.Cerebro()
    cerebro.broker.setcash(100000.0)
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())


    data = bt.feeds.PandasData(dataname=pd_klines_spot_data,timeframe=1,openinterest=None)
    cerebro.adddata(data)

    # Run over everything
    cerebro.run()
    # Plot the result
    cerebro.plot(style='bar')

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

main()