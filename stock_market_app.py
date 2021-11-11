#Choose any 2 companies from yahoo finance and build an app to present the stock market
#performance details of the company as a dashboard.

import yfinance as yf
import pandas as pd
from yahoofinancials import YahooFinancials
aapl_df = yf.download("AAPL", start="2021-01-01",end="2021-11-09")
print(aapl_df.head())
aapl_df.to_csv("apple.csv")

#generating trend graphs using ticker functionality
#5y = 5 years in ticker.history
ticker = yf.Ticker("AAPL")
aapl_hist_df = ticker.history(period="5y")
aapl_hist_df["Close"].plot(title="Apple trends")
from matplotlib import pyplot as plt
plt.savefig("apple_trends.png")

msft = yf.Ticker("MSFT")

# get stock info
msft.info

# get historical market data
hist = msft.history(period="max")

# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends

# show splits
msft.splits

# show financials
msft.financials
msft.quarterly_financials

# show major holders
msft.major_holders

# show institutional holders
msft.institutional_holders

# show balance sheet
msft.balance_sheet
msft.quarterly_balance_sheet

# show cashflow
msft.cashflow
msft.quarterly_cashflow

# show earnings
msft.earnings
msft.quarterly_earnings

# show sustainability
msft.sustainability

# show analysts recommendations
msft.recommendations

# show next event (earnings, etc)
msft.calendar

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options

# show news
msft.news

