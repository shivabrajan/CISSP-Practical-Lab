import streamlit as st
from streamlit_card import card

st.set_page_config(page_title="Card Test")

st.title("Card Test")

clicked = card(
    title="🔒 Confidentiality",
    text="Protect sensitive data"
)

st.write("Clicked:", clicked)