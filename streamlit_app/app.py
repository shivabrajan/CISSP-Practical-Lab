import streamlit as st

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="CISSP Practical Lab",
    page_icon="🔐",
    layout="wide"
)

# ==================================================
# SESSION STATE
# ==================================================

if "selected" not in st.session_state:
    st.session_state.selected = "conf"

if "confidentiality_broken" not in st.session_state:
    st.session_state.confidentiality_broken = False

if "integrity_broken" not in st.session_state:
    st.session_state.integrity_broken = False

if "availability_broken" not in st.session_state:
    st.session_state.availability_broken = False

# ==================================================
# HEADER
# ==================================================

st.title("🔐 CISSP Practical Lab")
st.header("Domain 3 - Security Architecture & Engineering")
st.subheader("Lab 1 - CIA + Non-Repudiation Simulator")

# ==================================================
# SCORE
# ==================================================

score = 3

if st.session_state.confidentiality_broken:
    score -= 1

if st.session_state.integrity_broken:
    score -= 1

if st.session_state.availability_broken:
    score -= 1

st.metric("Security Posture Score", f"{score}/3 Secure")

# ==================================================
# STATUS BAR
# ==================================================

status = []

status.append(
    "🔴 Confidentiality"
    if st.session_state.confidentiality_broken
    else "🟢 Confidentiality"
)

status.append(
    "🔴 Integrity"
    if st.session_state.integrity_broken
    else "🟢 Integrity"
)

status.append(
    "🔴 Availability"
    if st.session_state.availability_broken
    else "🟢 Availability"
)

st.info(" | ".join(status))

# ==================================================
# RESET
# ==================================================

col_reset, col_empty = st.columns([1, 5])

with col_reset:
    if st.button("🔄 Reset"):
        st.session_state.confidentiality_broken = False
        st.session_state.integrity_broken = False
        st.session_state.availability_broken = False
        st.rerun()

# ==================================================
# GOATIFY BANNER
# ==================================================

st.caption(
    "🏢 Goatify Payroll System | "
    "Employee: John Doe | "
    "ID: GF-10452 | "
    "Classification: Confidential"
)

st.divider()

# ==================================================
# SECURITY CARDS
# ==================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    conf_status = (
        "Compromised"
        if st.session_state.confidentiality_broken
        else "Protected"
    )

    if st.button(
        f"🔒\n\nConfidentiality\n\n{conf_status}",
        use_container_width=True
    ):
        st.session_state.selected = "conf"

with col2:

    int_status = (
        "Compromised"
        if st.session_state.integrity_broken
        else "Trusted"
    )

    if st.button(
        f"🛡\n\nIntegrity\n\n{int_status}",
        use_container_width=True
    ):
        st.session_state.selected = "int"

with col3:

    avail_status = (
        "Offline"
        if st.session_state.availability_broken
        else "Online"
    )

    if st.button(
        f"⚡\n\nAvailability\n\n{avail_status}",
        use_container_width=True
    ):
        st.session_state.selected = "avail"

with col4:

    if st.button(
        "✍\n\nNon-Repudiation\n\nVerified",
        use_container_width=True
    ):
        st.session_state.selected = "nr"

st.divider()

# ==================================================
# CONFIDENTIALITY
# ==================================================

if st.session_state.selected == "conf":

    st.subheader("🔒 Confidentiality")

    if st.button("Launch Confidentiality Breach"):

        st.session_state.confidentiality_broken = True
        st.rerun()

    if not st.session_state.confidentiality_broken:

        st.success("✅ Payroll records are protected.")

    else:

        st.error("⚠ Confidentiality Compromised")

        st.code("""
Employee      : John Doe
Employee ID   : GF-10452
Salary        : £250,000
Bonus         : £25,000
Bank Account  : XXXX7821
National ID   : XX123456
""")

        st.warning("""
Business Impact

• Sensitive payroll data exposed

• Privacy violation

• Identity theft risk

• Employee trust reduced
""")

        st.success("""
Controls

✅ Encryption

✅ RBAC

✅ MFA
""")

        with st.expander("📰 Real World Incident"):

            st.write("""
Equifax Data Breach (2017)

Sensitive personal information of millions
of individuals was exposed.

CIA Principle Impacted:
Confidentiality
""")

# ==================================================
# INTEGRITY
# ==================================================

elif st.session_state.selected == "int":

    st.subheader("🛡 Integrity")

    if st.button("Launch Integrity Breach"):

        st.session_state.integrity_broken = True
        st.rerun()

    if not st.session_state.integrity_broken:

        st.success("✅ Record integrity verified.")

        st.code("""
Hash Status : VALID

Stored Hash : A84F7B92
""")

    else:

        st.error("⚠ Integrity Compromised")

        c1, c2 = st.columns(2)

        with c1:

            st.write("### Original Record")

            st.code("""
Employee      : John Doe
Salary        : £250,000
Bonus         : £25,000
Bank Account  : XXXX7821
""")

        with c2:

            st.write("### Modified Record")

            st.code("""
Employee      : John Doe
Salary        : £500,000
Bonus         : £250,000
Bank Account  : XXXX9999
""")

        st.code("""
Hash Status : FAILED

Stored Hash : A84F7B92
Current Hash: C76D11A1
""")

        st.warning("""
Business Impact

• Salary altered

• Bonus altered

• Bank details changed

• Records can no longer be trusted

• Audit findings likely
""")

        st.success("""
Controls

✅ SHA-256 Hashing

✅ Digital Signatures

✅ Audit Trails

✅ Change Management
""")

        with st.expander("📰 Real World Incident"):

            st.write("""
Payroll Fraud Scenario

Unauthorised modification of payroll records
can result in financial loss and audit findings.

CIA Principle Impacted:
Integrity
""")

# ==================================================
# AVAILABILITY
# ==================================================

elif st.session_state.selected == "avail":

    st.subheader("⚡ Availability")

    if st.button("Launch Availability Failure"):

        st.session_state.availability_broken = True
        st.rerun()

    if not st.session_state.availability_broken:

        st.success("✅ Goatify payroll platform online.")

    else:

        st.error("⚠ Availability Lost")

        st.code("""
GOATIFY PAYROLL PLATFORM

STATUS : OFFLINE

Payroll Processing : FAILED

Employee Portal : UNAVAILABLE
""")

        st.warning("""
Business Impact

John Doe did not receive salary.

15,000 employees did not receive payroll.

Employees cannot:

• View payslips
• Download tax documents
• Verify payment status

Operations disrupted.
""")

        st.success("""
Controls

✅ Backup Systems

✅ Disaster Recovery

✅ High Availability

✅ Redundant Infrastructure
""")

        with st.expander("📰 Real World Incident"):

            st.write("""
CrowdStrike Outage (2024)

Millions of systems became unavailable,
disrupting airlines, healthcare,
banking and other services.

CIA Principle Impacted:
Availability
""")

# ==================================================
# NON-REPUDIATION
# ==================================================

elif st.session_state.selected == "nr":

    st.subheader("✍ Non-Repudiation")

    st.code("""
Payroll Approval Record

Employee         : John Doe
Employee ID      : GF-10452

Action           : Payroll Approved

Date             : 23-Nov-2026
Time             : 08:00

Digital Signature : VERIFIED
""")

    st.info("""
John Doe approved the payroll transaction.

Because a digital signature exists:

• The signer is identified

• The action is verifiable

• The approval cannot later be denied
""")

    st.success("""
Controls

✅ Digital Signatures

✅ PKI

✅ Certificates

✅ Audit Logs
""")

    with st.expander("📰 Real World Usage"):

        st.write("""
Banks and financial institutions use
digital signatures for:

• Transactions
• Contracts
• Loan Approvals

This provides:

• Authentication
• Integrity
• Non-Repudiation
""")