import streamlit as st
import requests

st.set_page_config(page_title="GBTNetwork", layout="wide")
st.title("🌐 GBTNetwork Layer 1")

backend = "https://gbtnetwork-render.onrender.com"

st.markdown("##### Chain ID Check")
if st.button("🔍 Check Chain ID"):
    try:
        res = requests.get(f"{backend}/chain-id")
        st.success(res.json())
    except:
        st.error("Failed to connect to RPC backend")

st.markdown("##### Balance Checker")
address = st.text_input("Wallet Address")
if st.button("🔍 Get Balance") and address:
    try:
        res = requests.get(f"{backend}/balance/{address}")
        st.info(res.json())
    except:
        st.error("RPC connection error")

st.markdown("---")
st.markdown("✅ [Add GBTNetwork to MetaMask](https://chainlist.org/?search=GBTNetwork)")
