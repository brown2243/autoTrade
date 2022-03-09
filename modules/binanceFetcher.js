import Binance from "node-binance-api";

export const makeBinanceInstance = (APIKEY, APISECRET) =>
  new Binance().options({
    APIKEY,
    APISECRET,
  });
