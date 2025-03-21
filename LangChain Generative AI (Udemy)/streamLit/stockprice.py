import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
## Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google!

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
""")

# # symbol makes a title in write


# def ticker symbol
tickerSymbol = 'GOOGL'
# get data
tickerData = yf.Ticker(tickerSymbol)
# get historical prices
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
