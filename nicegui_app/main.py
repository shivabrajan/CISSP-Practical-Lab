from nicegui import ui
ui.add_head_html("""
<style>
body {
    background: #0B1120;
}

.q-page {
    background: #0B1120;
}

.q-card {
    transition: all 0.3s ease;
}
</style>
""")

SIMULATOR_DATA = {

    'confidentiality': {

        'protected': {

            'data': {
                'title': 'Protected Payroll Data',
                'details': 'Salary records remain encrypted and accessible only to authorised HR staff.'
            },

            'impact': {
                'title': 'Business Impact: Low',
                'details': 'Employee privacy is preserved and regulatory compliance is maintained.'
            },

            'controls': {
                'title': 'Security Controls',
                'details': 'Encryption, RBAC, MFA and auditing protect sensitive information.'
            },

            'incident': {
                'title': 'Data Protected',
                'details': 'No confidentiality incident has occurred.'
            }
        },

        'breached': {

            'data': {
                'title': 'Payroll Database Exposed',
                'details': 'Salary records have been viewed by unauthorised users.'
            },

            'impact': {
                'title': 'Business Impact: High',
                'details': 'Regulatory penalties, reputational damage and employee trust issues.'
            },

            'controls': {
                'title': 'Recommended Controls',
                'details': 'Enable encryption, DLP, MFA and access reviews.'
            },

            'incident': {
                'title': 'Equifax Data Breach (2017)',
                'details': 'Sensitive customer information was exposed affecting millions of users.'
            }
        }
    },

    'integrity': {

        'verified': {

            'data': {
                'title': 'Verified Records',
                'details': 'Payroll calculations remain accurate and untampered.'
            },

            'impact': {
                'title': 'Business Impact: Low',
                'details': 'Financial reporting remains trustworthy.'
            },

            'controls': {
                'title': 'Security Controls',
                'details': 'Checksums, hashing and change control processes.'
            },

            'incident': {
                'title': 'Data Integrity Maintained',
                'details': 'Records remain accurate and trustworthy.'
            }
        },

        'tampered': {

            'data': {
                'title': 'Modified Payroll Records',
                'details': 'Critical financial information was altered.'
            },

            'impact': {
                'title': 'Business Impact: High',
                'details': 'Incorrect salaries and inaccurate financial reporting.'
            },

            'controls': {
                'title': 'Recommended Controls',
                'details': 'Digital signatures, hashing and audit trails.'
            },

            'incident': {
                'title': 'Financial Record Manipulation',
                'details': 'Unauthorised modifications affected trusted records.'
            }
        }
    }
    ,
    'availability': {

        'online': {

            'data': {
                'title': 'Payroll System Available',
                'details': 'Employees can access salary information and HR services normally.'
            },

            'impact': {
                'title': 'Business Impact: Low',
                'details': 'Business operations continue without interruption.'
            },

            'controls': {
                'title': 'Security Controls',
                'details': 'Redundancy, failover systems, backups and disaster recovery planning.'
            },

            'incident': {
                'title': 'System Available',
                'details': 'Services are functioning normally.'
            }
        },

        'offline': {

            'data': {
                'title': 'Payroll System Unavailable',
                'details': 'Users cannot access payroll services due to an outage.'
            },

            'impact': {
                'title': 'Business Impact: High',
                'details': 'Employees cannot access pay records and business operations are disrupted.'
            },

            'controls': {
                'title': 'Recommended Controls',
                'details': 'High availability architecture, failover, backups and disaster recovery testing.'
            },

            'incident': {
                'title': 'CrowdStrike Outage (2024)',
                'details': 'A widespread outage disrupted business operations across industries.'
            }
        }
    }
    ,
    'non_repudiation': {

        'signed': {

            'data': {
                'title': 'Digitally Signed Transaction',
                'details': 'Actions are linked to a verified user through digital signatures.'
            },

            'impact': {
                'title': 'Business Impact: Low',
                'details': 'Transactions can be trusted and legally verified.'
            },

            'controls': {
                'title': 'Security Controls',
                'details': 'Digital signatures, certificates and PKI infrastructure.'
            },

            'incident': {
                'title': 'Verified Transaction',
                'details': 'The origin of the transaction can be proven.'
            }
        },

        'unsigned': {

            'data': {
                'title': 'Unsigned Transaction',
                'details': 'The action cannot be reliably linked to a specific individual.'
            },

            'impact': {
                'title': 'Business Impact: High',
                'details': 'Disputes, fraud investigations and legal challenges may occur.'
            },

            'controls': {
                'title': 'Recommended Controls',
                'details': 'Implement PKI, digital signatures and certificate validation.'
            },

            'incident': {
                'title': 'Disputed Transaction',
                'details': 'A user denies performing an action and there is insufficient proof.'
            }
        }
    }
}


# ==================================================
# STATE
# ==================================================

selected_objective = {
    'value': 'confidentiality'
}
selected_state = {
    'value': 'protected'
}

# ==================================================
# OBJECTIVE SELECTION
# ==================================================

def select_objective(name):

    selected_objective['value'] = name

    if name == 'confidentiality':
        selected_state['value'] = 'protected'

    elif name == 'integrity':
        selected_state['value'] = 'verified'

    elif name == 'availability':
        selected_state['value'] = 'online'

    else:
        selected_state['value'] = 'signed'

    objective_cards.refresh()
    state_cards.refresh()
    workspace.refresh()
  

def select_state(name):

    selected_state['value'] = name

    state_cards.refresh()
    workspace.refresh()
    
# ==================================================
# OBJECTIVE CARDS
# ==================================================

@ui.refreshable
def objective_cards():

    with ui.row().classes('w-full gap-2'):

        cards = [
    (
        'confidentiality',
        '🔒 Confidentiality',
        '#0F5D7A',
        '#0B7DB0'
    ),
    (
        'integrity',
        '🛡 Integrity',
        '#D97706',
        '#F59E0B'
    ),
    (
        'availability',
        '⚡ Availability',
        '#7E22CE',
        '#A855F7'
    ),
    (
        'non_repudiation',
        '✍ Non‑Repudiation',
        '#15803D',
        '#22C55E'
    )
]

        for key, title, normal, active in cards:

            selected = (
                selected_objective['value'] == key
            )

            with ui.card().style(f"""
                background-color:{active if selected else normal};
                border:{f'3px solid {active}' if selected else '1px solid transparent'};
                box-shadow:{f'0 0 25px {active}' if selected else 'none'};
                cursor:pointer;
                min-width:100px;
                padding:8px 12px;
                border-radius:999px;
                transition:all 0.3s ease;
            """).on(
                'click',
                lambda k=key: select_objective(k)
            ):

                ui.label(title).classes(
                    'text-white text-sm font-bold'
                )
@ui.refreshable
def state_cards():

    objective = selected_objective['value']

    if objective == 'confidentiality':
        states = [
            ('protected', '🟢 Protected', '#166534', '#22C55E'),
            ('breached', '🔴 Breached', '#991B1B', '#EF4444'),
        ]

    elif objective == 'integrity':
        states = [
            ('verified', '✅ Verified', '#166534', '#22C55E'),
            ('tampered', '❌ Tampered', '#991B1B', '#EF4444'),
        ]

    elif objective == 'availability':
        states = [
            ('online', '🟢 Online', '#166534', '#22C55E'),
            ('offline', '🔴 Offline', '#991B1B', '#EF4444'),
        ]

    else:
        states = [
            ('signed', '✅ Signed', '#166534', '#22C55E'),
            ('unsigned', '❌ Signature Removed', '#991B1B', '#EF4444'),
        ]

    with ui.row().classes('w-full gap-2'):

        for key, title, normal, active in states:

            selected = (
                selected_state['value'] == key
            )

            with ui.card().style(f"""
                background-color:{active if selected else normal};
                border:{f'3px solid {active}' if selected else '1px solid transparent'};
                box-shadow:{f'0 0 25px {active}' if selected else 'none'};
                cursor:pointer;
                min-width:100px;
                padding:8px 12px;
                border-radius:999px;
            """).on(
                'click',
                lambda k=key: select_state(k)
            ):

                ui.label(title).classes(
                    'text-white text-sm font-bold'
                )
                
@ui.refreshable
def workspace():

    objective = selected_objective['value']
    state = selected_state['value']

    content = SIMULATOR_DATA[objective][state]

    with ui.row().classes('w-full gap-2'):

        # DATA
        with ui.card().classes('grow bg-slate-900 h-72'):

            ui.label(
                '📄 Data'
            ).classes(
                'text-sm font-bold text-cyan-300'
            )

            # Confidentiality Protected
            if (
                objective == 'confidentiality'
                and state == 'protected'
            ):

                ui.label(
                    '🔒 Payroll Database Protected'
                ).classes(
                    'font-bold text-green-400'
                )

                ui.label("""
Employee Name      Salary
██████████ 🔒      ████████ 🔒
██████████ 🔒      ████████ 🔒
██████████ 🔒      ████████ 🔒
""").style(
    'font-family: monospace; white-space: pre; color: #22C55E;'
)

            # Confidentiality Breached
            elif (
                objective == 'confidentiality'
                and state == 'breached'
            ):

                

                ui.html("""
<div style="
background-color:#7f1d1d;
color:white;
padding:10px;
font-weight:bold;
border-radius:8px;
text-align:center;
animation: pulse 1s infinite;
">

<div style="font-size:18px;">
🚨 DATA BREACH DETECTED 🚨
</div>

<div style="font-size:14px; margin-top:4px;">
Confidential Payroll Records Exposed ●●●●●► 🌐 Internet
</div>

</div>

<style>
@keyframes pulse {
  0% { opacity:1; }
  50% { opacity:0.4; }
  100% { opacity:1; }
}
</style>
""")

                ui.label("""
Employee Name      Salary
John Doe           ₹850,000
Sarah Smith        ₹920,000
Mike Wilson        ₹780,000
""").style(
    'font-family: monospace; white-space: pre; color:#EF4444;'
)
                

            else:

                ui.label(
                    content['data']['title']
                ).classes(
                    'font-bold text-white'
                )

                ui.label(
                    content['data']['details']
                ).classes(
                    'text-gray-300'
                )

        # IMPACT
        with ui.card().classes('grow bg-slate-900 h-72'):

            ui.label(
                '📈 Business Impact'
            ).classes(
                'text-sm font-bold text-orange-300'
            )

            ui.label(
                content['impact']['title']
            ).classes(
                'font-bold text-white'
            )

            ui.label(
                content['impact']['details']
            ).classes(
                'text-gray-300 text-sm'
            )

        # CONTROLS
        with ui.card().classes('grow bg-slate-900 h-72'):

            ui.label(
                '🛡 Security Controls'
            ).classes(
                'text-sm font-bold text-green-300'
            )

            ui.label(
                content['controls']['title']
            ).classes(
                'font-bold text-white'
            )

            ui.label(
                content['controls']['details']
            ).classes(
                'text-gray-300 text-sm'
            )

        # INCIDENT
        with ui.card().classes('grow bg-slate-900 h-72'):

            ui.label(
                '📰 Real World Incident'
            ).classes(
                'text-sm font-bold text-red-300'
            )

            ui.label(
                content['incident']['title']
            ).classes(
                'font-bold text-white'
            )

            ui.label(
                content['incident']['details']
            ).classes(
                'text-gray-300 text-sm'
            )

# ==================================================
# HEADER
# ==================================================

ui.page_title('CISSP Practical Lab')

ui.label(
    '🔐 CISSP Practical Lab'
).classes(
    'text-4xl font-bold'
)

ui.label(
    'Domain 3 - Security Architecture & Engineering'
).classes(
    'text-lg text-white'
)

ui.separator()


# ==================================================
# PURPOSE
# ==================================================

with ui.card().classes('w-full'):

    ui.label(
        '🎯 Purpose'
    ).classes(
        'text-xl font-bold'
    )

    ui.label(
        'Explore how security failures impact a business system.'
    )


# ==================================================
# GOATIFY + SECURITY POSTURE
# ==================================================

with ui.row().classes('w-full'):

    with ui.card().classes('grow h-32'):

        ui.label(
            '🏢 Goatify Payroll Management System'
        ).classes(
            'text-sm font-bold'
        )

        ui.label(
            'Employee: John Doe | GF-10452 | Confidential'
        )

    with ui.card().classes('h-32 justify-center items-center'):

        ui.label(
            '🛡 Security Posture'
        ).classes('text-sm  font-bold'
        )

        ui.label(
            '4 / 4'
        ).classes(
            'text-3xl text-green-500 font-bold'
        )


# ==================================================
# SECURITY OBJECTIVES
# ==================================================

ui.separator()

ui.label(
    '🎯 Security Objectives'
).classes(
    'text-xl text-white font-bold'
)

objective_cards()
ui.separator()

ui.label(
    'Simulation State'
).classes(
    'text-xl text-white font-bold'
)

state_cards()

ui.separator()

ui.label(
    'Simulator Workspace'
).classes(
    'text-xl text-white font-bold'
)

workspace()


# ==================================================
# RUN
# ==================================================

ui.run()