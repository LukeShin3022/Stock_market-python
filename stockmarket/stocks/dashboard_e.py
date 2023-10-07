import streamlit as st
import requests
import config_e



symbol = st.sidebar.text_input("symbol", value="AAPL")

screen = st.sidebar.selectbox("View", ('Overview', 'Fundamentals', 'News', 'Ownership'))
st.title(screen)


if screen == 'Overview':
    url = f"https://api.iex.cloud/v1/stock/{symbol}/logo?token={config_e.IEX_TOKEN}"
    r = requests.get(url)
    logo = r.json()
    # response_json = response_json[0]

    url = f"https://api.iex.cloud/v1/data/core/company/{symbol}?token={config_e.IEX_TOKEN}"
    r = requests.get(url)
    response_json = r.json()
    response_json = response_json[0]

    col1, col2 = st.columns([1, 4])

    with col1:
        st.image(logo['url'])

    with col2:
        st.subheader(response_json['companyName'])
        st.subheader('Description')
        st.write(response_json['longDescription'])
        st.subheader('Industry')
        st.write(response_json['industry'])
        st.subheader('CEO')
        st.write(response_json['ceo'])


