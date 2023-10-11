import streamlit as st
import requests
import config_e
from iex_e import IEXStock

symbol = st.sidebar.text_input("symbol", value="AAPL")
stock = IEXStock(config_e.IEX_TOKEN, symbol)

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
    stats = stock.get_stats()
    st.write()
