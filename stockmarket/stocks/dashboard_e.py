import streamlit as st
import redis
import config_e, json
from iex_e import IEXStock
from helpers_e import format_number
from datetime import datetime, timedelta

symbol = st.sidebar.text_input("symbol", value="AAPL")
stock = IEXStock(config_e.IEX_TOKEN, symbol)
client = redis.Redis(host="localhost", port=6379)

screen = st.sidebar.selectbox("View", ('Overview', 'Fundamentals', 'News', 'Ownership'))
st.title(screen)


if screen == 'Overview':
    logo = stock.get_logo()
    company_info = stock.get_company_info()[0]

    col1, col2 = st.columns([1, 4])

    with col1:
        st.image(logo['url'])

    with col2:
        st.subheader(company_info['companyName'])
        st.subheader('Description')
        st.write(company_info['longDescription'])
        st.subheader('Industry')
        st.write(company_info['industry'])
        st.subheader('CEO')
        st.write(company_info['ceo'])

if screen == 'Fundamentals':
    stats_cache_key = f"{symbol}_stats"
    stats = client.get(stats_cache_key)

    if stats is None:
        stats = stock.get_stats()
        client.set(stats_cache_key, json.dumps(stats))
    else:
        stats = json.loads(stats)

    st.header('Ratios')

    col1, col2 = st.beta_columns(2)

    with col1:
        st.subheader('P/E')
        st.write(stats['peRatio'])
        st.subheader('Forward P/E')
        st.write(stats['forwardPERatio'])
        st.subheader('PEG Ratio')
        st.write(stats['pegRatio'])
        st.subheader('Price to Sales')
        st.write(stats['priceToSales'])
        st.subheader('Price to Book')
        st.write(stats['priceToBook'])
    with col2:
        st.subheader('Revenue')
        st.write(format_number(stats['revenue']))
        st.subheader('Cash')
        st.write(format_number(stats['totalCash']))
        st.subheader('Debt')
        st.write(format_number(stats['currentDebt']))
        st.subheader('200 Day Moving Average')
        st.write(stats['day200MovingAvg'])
        st.subheader('50 Day Moving Average')
        st.write(stats['day50MovingAvg'])

    fundamentals_cache_key = f"{symbol}_fundamentals"
    fundamentals = client.get(fundamentals_cache_key)

    if fundamentals is None:
        fundamentals = stock.get_fundamentals('quarterly')
        client.set(fundamentals_cache_key, json.dumps(fundamentals))
    else:
        fundamentals = json.loads(fundamentals)

    for quarter in fundamentals:
        st.header(f"Q{quarter['fiscalQuarter']} {quarter['fiscalYear']}")
        st.subheader('Filing Date')
        st.write(quarter['filingDate'])
        st.subheader('Revenue')
        st.write(format_number(quarter['revenue']))
        st.subheader('Net Income')
        st.write(format_number(quarter['incomeNet']))

    st.header("Dividends")

    dividends_cache_key = f"{symbol}_dividends"
    dividends = client.get(dividends_cache_key)

    if dividends is None:
        dividends = stock.get_dividends()
        client.set(dividends_cache_key, json.dumps(dividends))
    else:
        dividends = json.loads(dividends)

    for dividend in dividends:
        st.write(dividend['paymentDate'])
        st.write(dividend['amount'])
