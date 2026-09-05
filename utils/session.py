import streamlit as st

def get_store():
    if "payrecover_store" not in st.session_state:
        st.session_state.payrecover_store = {}
    return st.session_state.payrecover_store
