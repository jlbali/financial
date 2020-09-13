# -*- coding: utf-8 -*-

import yfinance as yf
import os

symbols = ["MMM", "ABT", "ABBV", "ACN", "ATVI", "ADBE",
           "AMD", "AAP", "AES", "AFL", "AKAM", "IBM", "GOOG",
           "SBUX", "AAPL", "SPY", "MELI", "DESP",
           "WFC", "WDC", "ZION"    
]

symbols.append("SPY")

if __name__ == "__main__":
    for symbol in symbols:
        data = yf.download(symbol, start="2010-01-01", end="2018-12-31")
        if data.size > 0:
            data.to_csv(f"../../datasets/symbols/{symbol}.csv")
            


