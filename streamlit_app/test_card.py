import streamlit as st
from streamlit_card import card

st.set_page_config(layout="wide")

c1, c2, c3, c4 = st.columns(4)

with c1:
    card(
        title="🔒 Confidentiality",
        text="Protect sensitive information"
    )

with c2:
    card(
        title="🛡 Integrity",
        text="Prevent unauthorised changes"
    )

with c3:
    card(
        title="⚡ Availability",
        text="Keep services operational"
    )

with c4:
    card(
        title="✍ Non‑Repudiation",
        text="Provide proof of action"
    )