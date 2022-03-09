# Cryto Trading Bot

## 개발 목적

1. **돈을 벌고 싶어서**
2. 겸사 겸사 개발실력 향상

## 기능 구상

1. 원하는 상품, 계약의 봉 데이터 수집이 가능해야 한다.
   1. 1분,5분,15분,30분, 1시간, 1일
   2. 현물, 선물
2. 전략의 백테스팅이 가능해야 한다.
3. 전략의 다중 사용이 가능해야 한다.(분리된 봇들이 각각 전략을 사용)
4. 수익, 손실이 기록 되어야 한다.

## 설정

```
node - v14.17.0
mongoDB : MongoDB shell version v4.4.5
Build Info: {
    "version": "4.4.5",
    "gitVersion": "ff5cb77101b052fa02da43b8538093486cf9b3f7",
    "modules": [],
    "allocator": "system",
    "environment": {
        "distarch": "x86_64",
        "target_arch": "x86_64"
    }
}
```

```
mongoDB 사용법

brew services start mongodb-community@4.4 // 서버 실행
http://localhost:27017 // 체크
brew services stop mongodb-community@4.4 // 서버 종료

https://meanbymin.tistory.com/77

2개의 터미널에서
mongod, mongo(여기서 사용)

use DB명; // 데이터 베이스 만들기
show dbs; // 데이터 베이스 보여주기

db.createCollection('컬렉션명');
show collections;  //컬렉션 확인
db.컬렉션명.drop(); //컬렉션 삭제

contracts : {
    spot: {
        ticker : {
            1: 1m kline data
            5: 5m kline data
            15: 15m kline data
            60: 60m kline data
            1D: 1D kline data
        }
    }
    Futures: {
        ticker : {
            1: 1m kline data
            5: 5m kline data
            15: 15m kline data
            60: 60m kline data
            1D: 1D kline data
        }
    }
}
tradeLog : {
    [전략] :  {
        idx:'',
        ticker:'',
        포지션:'',
        매매금액: '',
        손익:'',
        시간:'',
    }
}
errorLog : {
    system : {
        idx
        ...
    }
    [전략] : {
        idx
        ...
    }
}

```
