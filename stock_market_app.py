# Choose any 2 companies from yahoo finance and build an app to present the stock market
# performance details of the company as a dashboard.

import yfinance as yf
import pandas as pd
from yahoofinancials import YahooFinancials
from matplotlib import pyplot as plt
import streamlit as st
import seaborn as sns
import plotly_express as px
# import plotly.graph_objs as go
# import plotly.subplots as sp


st.title("Stock Performance Dashboard")
# st.write("Select company from sidebar to view performance plots")
st.sidebar.title("Select a Company")
dpdwn = st.sidebar.selectbox("",[  
                                "Apple Stock Market",
                                "Microsoft Stock Market",
                                "Tesla Stock Market",
                                ])


# ---------------------- APPLE STOCKS ----------------------

aapl_df = yf.download("AAPL", start="2021-01-01",end="2021-11-09")
aapl_df.to_csv("apple.csv")

# Generating trend graphs using ticker functionality
# 5y = 5 years in ticker.history
ticker = yf.Ticker("AAPL")
aapl_hist_df = ticker.history(period="5y")
# aapl_hist_df["Close"].plot(title="Apple trends")
# plt.savefig("apple_trends.png")

# 
fig1 = px.line(aapl_hist_df, y="Close")

# Plotting Adj Close Values
fig2 = px.line(aapl_df, y="Adj Close") 

# Plotting Close Values
# fig2 = px.histogram(aapl_df, x="Close") 
fig3 = px.line(aapl_df, y="Close") 

# Plotting Dividends
fig4 = px.histogram(aapl_hist_df, x="Dividends") 




# ---------------------- MICROSOFT STOCKS ----------------------

msft_df = yf.download("MSFT", start="2021-01-01",end="2021-11-09")
msft_df.to_csv("microsoft.csv")

# Generating trend graphs using ticker functionality
# 5y = 5 years in ticker.history
msft = yf.Ticker("MSFT")
msft_hist_df = msft.history(period="5y")
# aapl_hist_df["Close"].plot(title="Apple trends")
# plt.savefig("microsoft_trends.png")



fig5 = px.line(msft_hist_df, y="Close")

# Plotting Adj Close Values
fig6 = px.histogram(msft_df, x="Adj Close") 

# Plotting Close Values
fig7 = px.line(msft_df, y="Close") 

# Plotting Dividends
fig8 = px.histogram(msft_hist_df, x="Dividends") 


# ---------------------- TESLA STOCKS ----------------------

tesla_df = yf.download("TSLA", start="2021-01-01",end="2021-11-09")
print(tesla_df.head())
tesla_df.to_csv("tesla.csv")

# Generating trend graphs using ticker functionality
# 5y = 5 years in ticker.history
ticker3 = yf.Ticker("TSLA")
tesla_hist_df = ticker3.history(period="5y")
# tesla_hist_df["Close"].plot(title="Tesla vs Apple Stocks 5y Comparison")
print(tesla_hist_df.head())

plt.savefig("tesla_trends.png")

fig9 = px.line(tesla_hist_df, y="Close")

# Plotting Adj Close Values
fig10 = px.histogram(tesla_df, x="Adj Close") 

# Plotting Close Values
fig11 = px.line(tesla_df, y="Close") 

# Plotting Dividends
fig12 = px.histogram(tesla_hist_df, x="Dividends") 


# ---------------------- APP DROPDOWN MENU ----------------------


if dpdwn == "Apple Stock Market":
    st.subheader("Apple Stock Market Performance Analysis")
    st.subheader("1. Closing trend 5-years")
    st.plotly_chart(fig1)
    st.subheader("2. Adj Closing trend 2021")
    st.plotly_chart(fig2) 
    st.subheader("3. Closing trend 2021")
    st.plotly_chart(fig3)
    st.subheader("4. Dividends Histogram 2021")
    st.plotly_chart(fig4)
    
    
if dpdwn == "Microsoft Stock Market":
    st.subheader("Microsoft Stock Market Performance Analysis") 
    st.subheader("1. Closing trend 5-years")
    st.plotly_chart(fig5)  
    st.subheader("2. Adj Closing trend 2021")
    st.plotly_chart(fig6)  
    st.subheader("3. Closing trend 2021")
    st.plotly_chart(fig7)
    st.subheader("4. Dividends Histogram 2021")
    st.plotly_chart(fig8)
    
    # ------------ Detailed Analysis for Microsoft Stocks --------------
    
    # get stock info
    st.subheader("5. Stock Info")
    msft.info
    
    # get historical market data
    st.subheader("6. Historical Market Data")
    hist = msft.history(period="max")
    
    # show actions (dividends, splits)
    st.subheader("7. Dividends & Splits")
    msft.actions
    
    # show dividends
    st.subheader("8. Dividends")
    msft.dividends
    
    # show splits
    st.subheader("9. Splits")
    msft.splits
    
    # show financials
    st.subheader("10. Quarterly Financials")
    # msft.financials
    msft.quarterly_financials
    
    # show major holders
    st.subheader("11. Major Holders")
    msft.major_holders
    
    # show institutional holders
    st.subheader("12. Institutional Holders")
    msft.institutional_holders
    
    # show balance sheet
    st.subheader("13. Balance Sheet")
    msft.balance_sheet
    st.subheader("14. Quarterly Balance Sheets")
    msft.quarterly_balance_sheet
    
    # show cashflow
    st.subheader("15. Cashflow")
    msft.cashflow
    st.subheader("16. Quarterly Cashflow")
    msft.quarterly_cashflow
    
    # show earnings
    st.subheader("17. Earnings")
    msft.earnings
    st.subheader("18. Quarterly Earnings")
    msft.quarterly_earnings
    
    # show sustainability
    # msft.sustainability
    
    # show analysts recommendations
    st.subheader("19. Recommendations")
    msft.recommendations
    
    # show next event (earnings, etc)
    st.subheader("20. Revenue Calendar")
    msft.calendar
    
    # show ISIN code - *experimental*
    # ISIN = International Securities Identification Number
    # msft.isin
    
    # show options expirations
    # msft.options
    
    # show news
    # msft.news

     
    
if dpdwn == "Tesla Stock Market":
    st.subheader("Tesla Stock Market Performance Analysis")
    st.subheader("1. Closing trend 5-years")
    st.plotly_chart(fig9)  
    st.subheader("2. Adj Closing trend 2021")
    st.plotly_chart(fig10)  
    st.subheader("3. Closing trend 2021")
    st.plotly_chart(fig11)
    st.subheader("4. Dividends Histogram 2021")
    st.plotly_chart(fig12)  
    






