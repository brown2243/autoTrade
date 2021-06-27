# autoTrade

파이썬과 코인으로 돈을 벌어보자!

## 준비과정

설치
맥은 그냥 python을 치면 2버전이 나옴;;
brew install python3

기본으로 python3를 사용하고 싶으면 아래 코드를 순서대로

```
sudo vim ~/.bash_profile$

---
// 수정모드 i 누르기
alias python='python3'
alias pip='python3 -m pip'

export PATH=/usr/local/bin:/usr/local/sbin:$PATH
export PATH

// 나가기 esc 버튼 → :wq! (수정모드 종료 → w = 저장 → q 종료)
---

// 저장한거 실행?느낌
source ~/.bash_profile
// 다시 버전 체크
python --version
pip install ccxt
```

참조
https://dejavuqa.tistory.com/132

## ccxt 사용하기

ccxt는 엄청 많은? 코인거래소 API를 지원함

```
import ccxt

binance = ccxt.binance()
markets = binance.fetch_tickers()
print(markets.keys())
// 바이낸스에서 거래 되는 모든 티커가 나옴

ticker = binance.fetch_ticker('ETH/BTC')
// 개별

print(ticker)
// {'symbol': 'ETH/USDT', 'timestamp': 1624103332251, 'datetime': '2021-06-19T11:48:52.251Z', 'high': 2326.2, 'low': 2139.0, 'bid': 2239.89, 'bidVolume': 1.37879, 'ask': 2239.9, 'askVolume': 18.29906, 'vwap': 2221.36205388, 'open': 2321.78, 'close': 2239.9, 'last': 2239.9, 'previousClose': 2321.78, 'change': -81.88, 'percentage': -3.527, 'average': None, 'baseVolume': 752850.17236, 'quoteVolume': 1672352805.1350799, 'info': {'symbol': 'ETHUSDT', 'priceChange': '-81.88000000', 'priceChangePercent': '-3.527', 'weightedAvgPrice': '2221.36205388', 'prevClosePrice': '2321.78000000', 'lastPrice': '2239.90000000', 'lastQty': '0.42615000', 'bidPrice': '2239.89000000', 'bidQty': '1.37879000', 'askPrice': '2239.90000000', 'askQty': '18.29906000', 'openPrice': '2321.78000000', 'highPrice': '2326.20000000', 'lowPrice': '2139.00000000', 'volume': '752850.17236000', 'quoteVolume': '1672352805.13507980', 'openTime': '1624016932251', 'closeTime': '1624103332251', 'firstId': '489258676', 'lastId': '490276130', 'count': '1017455'}}
```

과거 데이터 조회

```
import ccxt
from datetime import datetime

binance = ccxt.binance()
ohlcvs = binance.fetch_ohlcv('ETH/USDT')

for ohlc in ohlcvs:
    print(datetime.fromtimestamp(ohlc[0]/1000).strftime('%Y-%m-%d %H:%M:%S'), ohlc[1])
```

잔고 조회

```
binance = ccxt.binance({
    'apiKey' : KEY.key('api'),
    'secret' : KEY.key('sct'),
})

balance = binance.fetch_balance()
// 보유 중인 코인('free'), 거래 진행 중인 코인('used'), 전체 코인('total')의 개수가 딕셔너리로 저장되어 있습니다.

print(balance['BTC']['free'], balance['BTC']['used'], balance['BTC']['total']) // 0.87433992 0.0 0.87433992

```

```

```

```

```

```

```

```

```

` `
` `
` `
