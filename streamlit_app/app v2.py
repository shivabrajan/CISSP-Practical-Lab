import streamlit as st

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="CISSP Practical Lab V2",
    page_icon="🔐",
    layout="wide"
)

# ==================================================
# SESSION STATE
# ==================================================

if "selected_objective" not in st.session_state:
    st.session_state.selected_objective = "confidentiality"

if "objective_state" not in st.session_state:
    st.session_state.objective_state = "protected"

# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

.block-container {
    padding-top: 1rem;
}

div.stButton > button {
    width:100%;
    height:90px;
    font-weight:bold;
    font-size:16px;
    border-radius:12px;
}

.objective-card {
    padding: 14px;
    border-radius: 12px;
    text-align: center;
    font-weight: bold;
    color: white;
    margin-bottom: 5px;
}

.banner {
    background: #111827;
    padding: 16px;
    border-radius: 12px;
    border-left: 6px solid #3B82F6;
    margin-bottom: 15px;
}

.panel {
    border: 1px solid #374151;
    border-radius: 12px;
    padding: 15px;
    min-height: 260px;
}

.data-panel {
    background: #1F2937;
}

.impact-panel {
    background: #4A3A12;
}

.controls-panel {
    background: #123524;
}

.incident-panel {
    background: #312E81;
}

.metric-box {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================

st.title("🔐 CISSP Practical Lab")
st.subheader("Domain 3 - Security Architecture & Engineering")

# ==================================================
# PURPOSE
# ==================================================

st.markdown("""
<div style="
background:#0F172A;
padding:14px;
border-radius:12px;
border-left:5px solid #F59E0B;
margin-bottom:15px;">

<div style="
font-size:28px;
font-weight:bold;
color:#FBBF24;
margin-bottom:10px;">
🎯 Purpose
</div>

<div style="
font-size:16px;
color:#FFFFFF;
font-weight:500;
margin-bottom:12px;">
Explore how security failures impact a business system.
</div>


</div>
""", unsafe_allow_html=True)

# ==================================================
# GOATIFY BANNER AND SECURITY POSTURE
# ==================================================

left, right = st.columns([3.5, 1.5])

with left:

    st.markdown("""
    <div style="
    background:#111827;
    padding:16px;
    border-radius:12px;
    border-left:6px solid #3B82F6;
    height:105px;">

    <div style="
    font-size:28px;
    font-weight:bold;
    color:white;">
    🏢 Goatify Payroll Management System
    </div>

    <div style="
    font-size:16px;
    color:#E5E7EB;
    margin-top:6px;">
    Employee: John Doe |
    Employee ID: GF-10452 |
    Classification: Confidential
    </div>

    </div>
    """, unsafe_allow_html=True)

with right:

    st.markdown("""
    <div style="
    background:#111827;
    padding:16px;
    border-radius:12px;
    border-left:6px solid #22C55E;
    text-align:center;
    height:105px;">

    <div style="
    font-size:28px;
    font-weight:bold;
    color:#D1D5DB;">
    🛡 SECURITY POSTURE
    </div>

    <div style="
    font-size:24px;
    font-weight:bold;
    color:#22C55E;
    margin-top:0px;">
    4 / 4
    </div>

    </div>
    """, unsafe_allow_html=True)

st.markdown(
    "<div style='height:24px;'></div>",
    unsafe_allow_html=True
)

# ==================================================
# SECURITY OBJECTIVES
# ==================================================

st.markdown("""
<div style="
background:#1E293B;
padding:14px;
border-radius:12px;
border-left:5px solid #38BDF8;
margin-bottom:15px;">

<div style="
font-size:24px;
font-weight:bold;
color:#FFFFFF;
margin-bottom:10px;">
🎯 Security Objectives
</div>

<div style="
font-size:14px;
color:#CBD5E1;
font-weight:500;
margin-bottom:10px;">
Select a security objective and compare Protected and Breached states
</div>

<div style="
display:flex;
gap:8px;
flex-wrap:wrap;">

<div style="
background:#334155;
padding:6px 12px;
border-radius:20px;
font-size:12px;
font-weight:bold;
color:white;">
📄 Data
</div>

<div style="
background:#334155;
padding:6px 12px;
border-radius:20px;
font-size:12px;
font-weight:bold;
color:white;">
📈 Business Impact
</div>

<div style="
background:#334155;
padding:6px 12px;
border-radius:20px;
font-size:12px;
font-weight:bold;
color:white;">
🛡 Security Controls
</div>

<div style="
background:#334155;
padding:6px 12px;
border-radius:20px;
font-size:12px;
font-weight:bold;
color:white;">
📰 Real‑World Incidents
</div>

</div>

</div>
""", unsafe_allow_html=True)
st.markdown(
    "<div style='height:12px;'></div>",
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)



# --------------------------------------------------
# CONFIDENTIALITY
# --------------------------------------------------

with c1:

    bg = (
        "#6B7280"
        if st.session_state.selected_objective == "confidentiality"
        else "#0F5D7A"
    )

    st.markdown(
        f"""
        <div class="objective-card"
        style="background:{bg};">

        🔒<br>
        CONFIDENTIALITY

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Select", key="conf"):

        st.session_state.selected_objective = "confidentiality"
        st.rerun()

# --------------------------------------------------
# INTEGRITY
# --------------------------------------------------

with c2:

    bg = (
        "#6B7280"
        if st.session_state.selected_objective == "integrity"
        else "#D97706"
    )

    st.markdown(
        f"""
        <div class="objective-card"
        style="background:{bg};">

        🛡<br>
        INTEGRITY

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Select", key="int"):

        st.session_state.selected_objective = "integrity"
        st.rerun()

# --------------------------------------------------
# AVAILABILITY
# --------------------------------------------------

with c3:

    bg = (
        "#6B7280"
        if st.session_state.selected_objective == "availability"
        else "#7E22CE"
    )

    st.markdown(
        f"""
        <div class="objective-card"
        style="background:{bg};">

        ⚡<br>
        AVAILABILITY

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Select", key="avail"):

        st.session_state.selected_objective = "availability"
        st.rerun()

# --------------------------------------------------
# NON-REPUDIATION
# --------------------------------------------------

with c4:

    bg = (
        "#6B7280"
        if st.session_state.selected_objective == "non_repudiation"
        else "#15803D"
    )

    st.markdown(
        f"""
        <div class="objective-card"
        style="background:{bg};">

        ✍<br>
        NON-REPUDIATION

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Select", key="nr"):

        st.session_state.selected_objective = "non_repudiation"
        st.rerun()

# ==================================================
# STATE
# ==================================================

st.markdown("### Simulation State")

s1, s2 = st.columns(2)

with s1:

    if st.button(
        "🟢 Protected",
        use_container_width=True
    ):

        st.session_state.objective_state = "protected"

with s2:

    if st.button(
        "🔴 Breached",
        use_container_width=True
    ):

        st.session_state.objective_state = "breached"

st.divider()

# ==================================================
# WORKSPACE
# ==================================================

d1, d2, d3, d4 = st.columns(4)

with d1:

    st.markdown("### 📄 Data")

    st.info("""
Data panel

Sprint 2:
Dynamic content goes here
""")

with d2:

    st.markdown("### 📈 Impact")

    st.info("""
Impact panel

Sprint 2:
Dynamic content goes here
""")

with d3:

    st.markdown("### 🛡 Controls")

    st.info("""
Controls panel

Sprint 2:
Dynamic content goes here
""")

with d4:

    st.markdown("### 📰 Incident")

    st.info("""
Incident panel

Sprint 2:
Dynamic content goes here
""")