import dotenv from "dotenv";
import { makeBinanceInstance } from "./modules/binanceFetcher.js";
dotenv.config();

const binance = makeBinanceInstance(
  process.env.BINANCE_API_KEY,
  process.env.BINANCE_API_KEY
);

let ticker = await binance.prices();
console.log(ticker);
