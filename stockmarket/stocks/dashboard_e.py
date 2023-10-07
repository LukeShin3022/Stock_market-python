import streamlit as st
import requests

st.title("Fundamental Dashboard")

symbol = st.sidebar.text_input("symbol", value="AAPL")

screen = st.sidebar.selectbox("View", ('Overview', 'Fundamentals', 'News', 'Ownership'))
st.write(symbol)