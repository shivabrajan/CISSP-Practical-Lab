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

st.subheader("Lab 1 - CIA Triad Simulator")

with st.expander("🎯 Learning Goal", expanded=False):
    st.write("""
You are a Security Architect at Goatify.

Observe the impact when:

🔒 Confidentiality fails

🛡 Integrity fails

⚡ Availability fails

and understand how real security incidents affect businesses.
""")

# ==================================================
# SECURITY SCORE
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
# STATUS DASHBOARD
# ==================================================

s1, s2, s3 = st.columns(3)

with s1:
    if st.session_state.confidentiality_broken:
        st.error("🔒 Confidentiality")
    else:
        st.success("🔒 Confidentiality")

with s2:
    if st.session_state.integrity_broken:
        st.error("🛡 Integrity")
    else:
        st.success("🛡 Integrity")

with s3:
    if st.session_state.availability_broken:
        st.error("⚡ Availability")
    else:
        st.success("⚡ Availability")

# ==================================================
# RESET BUTTON
# ==================================================

if st.button("🔄 Reset Simulation"):
    st.session_state.confidentiality_broken = False
    st.session_state.integrity_broken = False
    st.session_state.availability_broken = False
    st.rerun()

st.divider()

# ==================================================
# BUSINESS SCENARIO
# ==================================================

st.warning("""
GOATIFY PAYROLL MANAGEMENT SYSTEM

Employee : John Doe
Employee ID : GF-10452

Data Classification : Confidential

This system stores employee salaries,
bonus information and payroll records.

Use the simulations below to understand CIA Triad failures.
""")

st.divider()

# ==================================================
# TABS
# ==================================================

tab1, tab2, tab3 = st.tabs(
    [
        "🔒 Confidentiality",
        "🛡 Integrity",
        "⚡ Availability"
    ]
)

# ==================================================
# CONFIDENTIALITY
# ==================================================

with tab1:

    st.subheader("Confidentiality Breach Simulation")

    if st.button(
        "Launch Confidentiality Breach",
        key="conf_btn"
    ):
        st.session_state.confidentiality_broken = True

    if not st.session_state.confidentiality_broken:

        st.success("✅ Payroll Record Protected")

        st.info("""
Status: Protected

Contents Hidden

Only authorised users can access payroll data.
""")

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

• Sensitive payroll information exposed

• Privacy breach

• Identity theft risk

• Employee confidence reduced
""")

        st.success("""
Recommended Controls

✅ Encryption

✅ Role Based Access Control (RBAC)

✅ Multi-Factor Authentication (MFA)
""")

        if st.button(
            "📰 Real World Incident",
            key="conf_incident"
        ):

            st.info("""
EQUIFAX DATA BREACH (2017)

Attackers exploited an unpatched vulnerability.

Impact:

• Personal information exposed

• Millions of individuals affected

• Major reputational damage

CIA Principle Impacted:

🔒 Confidentiality

Connection to Goatify:

Just like John Doe's payroll information became visible,
customer records were exposed to unauthorised parties.
""")

# ==================================================
# INTEGRITY
# ==================================================

with tab2:

    st.subheader("Integrity Breach Simulation")

    if st.button(
        "Launch Integrity Breach",
        key="int_btn"
    ):
        st.session_state.integrity_broken = True

    if not st.session_state.integrity_broken:

        st.success("✅ Integrity Verified")

        st.info("""
Hash Verification : VALID

Employee Record Trusted

Stored Hash : A84F7B92
""")

    else:

        st.error("⚠ Integrity Compromised")

        st.code("""
ORIGINAL RECORD

Employee      : John Doe
Salary        : £250,000
Bonus         : £25,000
Bank Account  : XXXX7821
""")

        st.code("""
MODIFIED RECORD

Employee      : John Doe
Salary        : £500,000
Bonus         : £250,000
Bank Account  : XXXX9999
""")

        st.code("""
HASH VERIFICATION

Stored Hash : A84F7B92

Current Hash: C76D11A1

Status      : FAILED
""")

        st.warning("""
Business Impact

• Payroll information altered

• Incorrect salary payments possible

• Financial loss

• Audit findings likely

• Records can no longer be trusted
""")

        st.success("""
Recommended Controls

✅ SHA-256 Hashing

✅ Digital Signatures

✅ Audit Trails

✅ Change Control
""")

        if st.button(
            "📰 Real World Incident",
            key="int_incident"
        ):

            st.info("""
PAYROLL FRAUD SCENARIO

Integrity failures occur when business
records are modified without authorisation.

Examples:

• Salary changes

• Bank account changes

• Bonus manipulation

CIA Principle Impacted:

🛡 Integrity

Connection to Goatify:

John Doe's salary, bonus and banking
information were altered.

Although the data is visible,
it can no longer be trusted.
""")

# ==================================================
# AVAILABILITY
# ==================================================

with tab3:

    st.subheader("Availability Failure Simulation")

    if st.button(
        "Launch Availability Failure",
        key="avail_btn"
    ):
        st.session_state.availability_broken = True

    if not st.session_state.availability_broken:

        st.success("✅ Payroll Platform Available")

        st.info("""
System Status : ONLINE

Employees can:

• View payslips

• Download tax documents

• Verify salary payments
""")

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

• Download tax records

• Verify payments

• Access payroll portal

Business operations are disrupted.
""")

        st.success("""
Recommended Controls

✅ Backups

✅ Disaster Recovery

✅ High Availability Design

✅ Redundant Infrastructure
""")

        if st.button(
            "📰 Real World Incident",
            key="avail_incident"
        ):

            st.info("""
CROWDSTRIKE OUTAGE (2024)

A faulty update caused widespread
Windows system failures.

Impact:

• Airlines disrupted

• Hospitals affected

• Banking services interrupted

• Millions of systems unavailable

CIA Principle Impacted:

⚡ Availability

Connection to Goatify:

Just as Goatify Payroll became unavailable,
organisations worldwide temporarily lost
access to critical business services.
""")