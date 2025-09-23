import pandas as pd
import matplotlib as plt
import seaborn as sns
import yfinance as yf
import streamlit as st

st.write(
    """
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Aple!

"""
)

tickerSymbol = "AAPL"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(start="2010-5-31", end="2020-5-31")

st.write(
    """
## Closing Price
"""
)
st.line_chart(tickerDf.Close)
st.write(
    """
## Volume Price
"""
)
st.line_chart(tickerDf.Volume)
