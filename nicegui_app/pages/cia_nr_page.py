from nicegui import ui
from layout import page_shell

OBJECTIVES = [
    ('confidentiality', '🔒 Confidentiality'),
    ('integrity', '🛡 Integrity'),
    ('availability', '⚡ Availability'),
    ('non_repudiation', '✍ Non-Repudiation'),
]

SIMULATOR_DATA = {
    'confidentiality': {
        'secure_key': 'protected',
        'compromised_key': 'breached',
        'cissp': {
            'domain': 'Domain 3: Security Architecture & Engineering',
            'concepts': ['Data Classification', 'Encryption (AES-256 / TLS 1.3)', 'Network Segmentation & DLP', 'Least Privilege / RBAC'],
        },
        'actor': {
            'secure': {
                'name': 'No Active Threat Actor',
                'category': 'Zero-Trust Enforced',
                'root_cause': 'Payroll DB is isolated in a private subnet with encryption and RBAC enforced.',
            },
            'compromised': {
                'name': 'External Attacker + Cloud Misconfiguration',
                'category': 'Misconfiguration / External Threat',
                'root_cause': 'Publicly exposed storage/DB endpoint allowed unauthenticated external queries to exfiltrate salary records.',
            },
        },
        'telemetry': {
            'protected': {
                'led': '#22C55E',
                'led_label': 'ENCRYPTED',
                'connection': 'Private VPC Only (0 Public Ingress)',
                'hash_or_sig': 'AES-256-GCM Active',
                'health': 'Confidentiality Intact',
            },
            'breached': {
                'led': '#EF4444',
                'led_label': 'EXFILTRATING',
                'connection': '0.0.0.0/0 Exposed -> Internet',
                'hash_or_sig': 'Cleartext / Unauth Read',
                'health': 'Breach Active',
            },
        },
        'controls_catalog': [
            {'id': 'vpc_firewall', 'label': 'Lock Down Firewall / Private Subnet', 'effective': True},
            {'id': 'aes_tls', 'label': 'Enforce AES-256 & TLS 1.3 + DLP', 'effective': True},
            {'id': 'ui_theme', 'label': 'Change Dashboard Banner Color Only', 'effective': False},
        ],
        'protected': {
            'data': {'title': 'Protected Payroll Data', 'details': 'Salary records remain encrypted at rest and in transit, accessible only to authorised HR staff.'},
            'impact': {'title': 'Business Impact: Low', 'details': 'Employee privacy is preserved and regulatory compliance is maintained.'},
            'controls': {'title': 'Active Security Controls', 'details': 'Encryption, RBAC, MFA, private subnets and auditing protect sensitive information.'},
            'incident': {'title': 'Data Protected', 'details': 'No confidentiality incident has occurred.'},
        },
        'breached': {
            'data': {'title': 'Payroll Database Exposed to Internet', 'details': 'Unauthenticated external access exposed employee names, IDs, and salaries.'},
            'impact': {'title': 'Business Impact: High', 'details': 'Regulatory fines, phishing/extortion targeting employees, and severe reputational damage.'},
            'controls': {'title': 'Required Remediation Controls', 'details': 'Select and apply network isolation and encryption/DLP controls to contain exposure.'},
            'incident': {'title': 'Equifax Data Breach (2017)', 'details': 'Sensitive personal and financial data was exposed, impacting millions of records.'},
        },
    },
    'integrity': {
        'secure_key': 'verified',
        'compromised_key': 'tampered',
        'cissp': {
            'domain': 'Domain 3 & Domain 7: Engineering & Security Operations',
            'concepts': ['Cryptographic Hashing (SHA-256)', 'Change Control', 'File/Database Integrity Monitoring (FIM)', 'Dual Control'],
        },
        'actor': {
            'secure': {
                'name': 'No Unauthorized Modification',
                'category': 'Integrity Baseline Verified',
                'root_cause': 'Cryptographic hashes and change-control workflows match approved payroll batches.',
            },
            'compromised': {
                'name': 'Malicious Insider / Privileged Abuse',
                'category': 'Insider Threat',
                'root_cause': 'Unauthorized modification of salary figures bypassed standard approval checks and broke hash parity.',
            },
        },
        'telemetry': {
            'verified': {
                'led': '#22C55E',
                'led_label': 'HASH MATCH',
                'connection': 'Ledger Sync: Verified',
                'hash_or_sig': 'SHA-256: MATCHED',
                'health': 'Data Untampered',
            },
            'tampered': {
                'led': '#F59E0B',
                'led_label': 'TAMPERED',
                'connection': 'Ledger Sync: Mismatch',
                'hash_or_sig': 'SHA-256: MISMATCH!',
                'health': 'Integrity Compromised',
            },
        },
        'controls_catalog': [
            {'id': 'hash_fim', 'label': 'Enforce SHA-256 Checksums & FIM Alerts', 'effective': True},
            {'id': 'change_ctrl', 'label': 'Require Dual Approval & Change Control', 'effective': True},
            {'id': 'clear_cache', 'label': 'Refresh Browser Cache Only', 'effective': False},
        ],
        'verified': {
            'data': {'title': 'Verified Payroll Records', 'details': 'Payroll amounts and cryptographic checksums match baseline records with zero tampering.'},
            'impact': {'title': 'Business Impact: Low', 'details': 'Financial reporting and employee pay disbursements remain accurate.'},
            'controls': {'title': 'Active Security Controls', 'details': 'SHA-256 checksums, change control processes, and immutable audit trails.'},
            'incident': {'title': 'Data Integrity Maintained', 'details': 'Records remain accurate and trustworthy.'},
        },
        'tampered': {
            'data': {'title': 'Payroll Figures Altered Without Authorisation', 'details': 'Salary amounts were altered, causing checksum mismatches and corrupted payout figures.'},
            'impact': {'title': 'Business Impact: High', 'details': 'Incorrect salary payouts, tax reporting errors, and unreliable financial statements.'},
            'controls': {'title': 'Required Remediation Controls', 'details': 'Apply checksum/FIM validation and strict change control to restore verified records.'},
            'incident': {'title': 'Financial Record Manipulation', 'details': 'Unauthorized alterations compromised trusted financial and payroll entries.'},
        },
    },
    'availability': {
        'secure_key': 'online',
        'compromised_key': 'offline',
        'cissp': {
            'domain': 'Domain 3 & Domain 7: Resilience & Business Continuity',
            'concepts': ['High Availability (HA)', 'Redundancy & Failover', 'Disaster Recovery (RTO/RPO)', 'Fault Tolerance'],
        },
        'actor': {
            'secure': {
                'name': 'Normal Operations',
                'category': 'Redundant & Healthy',
                'root_cause': 'Active nodes and health probes are operating within SLA targets.',
            },
            'compromised': {
                'name': 'Bad Deployment / Infrastructure Outage',
                'category': 'System Outage',
                'root_cause': 'Failed health probes and cascading service errors tripped the circuit breaker and took payroll offline.',
            },
        },
        'telemetry': {
            'online': {
                'led': '#22C55E',
                'led_label': 'ONLINE',
                'connection': 'API Gateway: HTTP 200 OK',
                'hash_or_sig': 'Failover Standby: Ready',
                'health': 'Uptime 99.99% (18ms)',
            },
            'offline': {
                'led': '#EF4444',
                'led_label': 'OFFLINE',
                'connection': 'API Gateway: HTTP 503',
                'hash_or_sig': 'Circuit Breaker: OPEN',
                'health': 'Service Unavailable',
            },
        },
        'controls_catalog': [
            {'id': 'failover_ha', 'label': 'Trigger Failover & Restore Active Nodes', 'effective': True},
            {'id': 'rollback_dr', 'label': 'Roll Back Faulty Release & Verify DR', 'effective': True},
            {'id': 'mute_alerts', 'label': 'Mute Monitoring Alerts Only', 'effective': False},
        ],
        'online': {
            'data': {'title': 'Payroll System Available', 'details': 'Employees and HR staff can access salary records and payroll services normally.'},
            'impact': {'title': 'Business Impact: Low', 'details': 'Business and payroll operations continue without interruption.'},
            'controls': {'title': 'Active Security Controls', 'details': 'Redundancy, automated failover, backups, and disaster recovery planning.'},
            'incident': {'title': 'System Available', 'details': 'Services are functioning normally.'},
        },
        'offline': {
            'data': {'title': 'Payroll System Unavailable', 'details': 'Timeouts and 503 errors prevent users from accessing payroll portals and APIs.'},
            'impact': {'title': 'Business Impact: High', 'details': 'Delayed payroll runs, missed SLAs, and operational disruption across teams.'},
            'controls': {'title': 'Required Remediation Controls', 'details': 'Engage failover/rollback controls and verify service health to bring payroll back online.'},
            'incident': {'title': 'CrowdStrike Outage (2024)', 'details': 'A widespread outage disrupted business operations across multiple industries.'},
        },
    },
    'non_repudiation': {
        'secure_key': 'signed',
        'compromised_key': 'unsigned',
        'cissp': {
            'domain': 'Domain 3 & Domain 5: Cryptography & IAM',
            'concepts': ['Digital Signatures (PKI)', 'Asymmetric Cryptography', 'Non-Repudiation & Auditability', 'Certificate Validation'],
        },
        'actor': {
            'secure': {
                'name': 'Verified Signer Identity',
                'category': 'PKI Authenticated',
                'root_cause': 'Actions are cryptographically signed with a valid key and bound to a known user.',
            },
            'compromised': {
                'name': 'Unverified / Disputed Actor',
                'category': 'Failed Authentication / Signing Process',
                'root_cause': 'Missing or invalid digital signature prevents proving who authorized the payroll change.',
            },
        },
        'telemetry': {
            'signed': {
                'led': '#22C55E',
                'led_label': 'SIGNED',
                'connection': 'Audit Log: Signer Bound',
                'hash_or_sig': 'PKI Cert: VALID',
                'health': 'Non-Repudiation Proven',
            },
            'unsigned': {
                'led': '#A855F7',
                'led_label': 'UNSIGNED',
                'connection': 'Audit Log: Origin Unproven',
                'hash_or_sig': 'PKI Cert: MISSING/INVALID',
                'health': 'Dispute Risk High',
            },
        },
        'controls_catalog': [
            {'id': 'pki_sign', 'label': 'Enforce PKI Digital Signatures on Actions', 'effective': True},
            {'id': 'cert_audit', 'label': 'Validate Cert Chain & Immutable Audit Log', 'effective': True},
            {'id': 'skip_sig', 'label': 'Allow Unsigned Express Approvals', 'effective': False},
        ],
        'signed': {
            'data': {'title': 'Digitally Signed Transaction', 'details': 'Actions are linked to a verified user through digital signatures and PKI.'},
            'impact': {'title': 'Business Impact: Low', 'details': 'Transactions can be trusted, audited, and legally verified.'},
            'controls': {'title': 'Active Security Controls', 'details': 'Digital signatures, X.509 certificates, and PKI infrastructure.'},
            'incident': {'title': 'Verified Transaction', 'details': 'The origin and integrity of the transaction are cryptographically proven.'},
        },
        'unsigned': {
            'data': {'title': 'Unsigned Transaction', 'details': 'Actions lack cryptographic proof of origin and can be disputed or denied.'},
            'impact': {'title': 'Business Impact: High', 'details': 'Disputes, stalled fraud investigations, and weak audit/legal accountability.'},
            'controls': {'title': 'Required Remediation Controls', 'details': 'Enable PKI digital signatures and certificate/audit enforcement to restore proof.'},
            'incident': {'title': 'Disputed Transaction', 'details': 'An actor denies performing an action and there is insufficient cryptographic proof.'},
        },
    },
}


@ui.page('/labs/cia-nr')
def cia_nr_page():
    page_shell('CIA & Non-Repudiation Triad', lab_id='cia_nr')

    selected_objective = {'value': 'confidentiality'}
    system_states = {
        'confidentiality': 'protected',
        'integrity': 'verified',
        'availability': 'online',
        'non_repudiation': 'signed',
    }
    pending_remediation = {k: False for k, _ in OBJECTIVES}
    selected_controls = {k: set() for k, _ in OBJECTIVES}
    explored_objectives = {'confidentiality'}
    remediated_count = {'value': 0}
    remediation_feedback = {'message': 'Select a compromised state or apply controls to test remediation.'}

    def is_compromised(obj: str) -> bool:
        return system_states[obj] == SIMULATOR_DATA[obj]['compromised_key']

    def get_posture_score() -> int:
        return sum(1 for obj, _ in OBJECTIVES if not is_compromised(obj))

    def get_risk_level(score: int) -> tuple[str, str]:
        if score == 4:
            return ('LOW RISK', 'text-emerald-400 bg-emerald-950/80 border-emerald-700')
        if score >= 2:
            return ('MODERATE RISK', 'text-amber-300 bg-amber-950/80 border-amber-700')
        return ('HIGH RISK', 'text-red-300 bg-red-950/80 border-red-700')

    def refresh_all():
        header_status_row.refresh()
        objective_tabs.refresh()
        failure_toggle_bar.refresh()
        workspace.refresh()
        timeline_section.refresh()

    def on_objective_tab_change(obj_key: str):
        if not obj_key:
            return
        selected_objective['value'] = obj_key
        explored_objectives.add(obj_key)
        refresh_all()

    def on_failure_switch_change(fail_enabled: bool):
        obj = selected_objective['value']
        info = SIMULATOR_DATA[obj]
        explored_objectives.add(obj)
        if fail_enabled:
            system_states[obj] = info['compromised_key']
            pending_remediation[obj] = True
            selected_controls[obj] = set()
            remediation_feedback['message'] = (
                f'{dict(OBJECTIVES)[obj]} is now COMPROMISED. Select effective controls and apply remediation.'
            )
        elif is_compromised(obj):
            remediation_feedback['message'] = (
                'Use "Apply Selected Controls" in the Remediation panel to verify controls and restore posture.'
            )
        refresh_all()

    def toggle_control_selection(obj: str, ctrl_id: str, checked: bool):
        if checked:
            selected_controls[obj].add(ctrl_id)
        else:
            selected_controls[obj].discard(ctrl_id)
        remediation_panel.refresh()

    def apply_remediation():
        obj = selected_objective['value']
        info = SIMULATOR_DATA[obj]
        chosen_ids = selected_controls[obj]

        if not is_compromised(obj):
            remediation_feedback['message'] = f'{dict(OBJECTIVES)[obj]} is already in a secure state.'
            refresh_all()
            return

        effective_ids = {c['id'] for c in info['controls_catalog'] if c['effective']}
        ineffective_chosen = {c['id'] for c in info['controls_catalog'] if not c['effective'] and c['id'] in chosen_ids}
        applied_effective = chosen_ids & effective_ids

        if applied_effective and not ineffective_chosen:
            system_states[obj] = info['secure_key']
            pending_remediation[obj] = False
            remediated_count['value'] += 1
            remediation_feedback['message'] = (
                f'Remediation successful! Effective controls applied for {dict(OBJECTIVES)[obj]} — Security Posture restored.'
            )
        elif applied_effective and ineffective_chosen:
            remediation_feedback['message'] = (
                'Remove ineffective controls (e.g., banner/cache/mute-only actions) and apply valid security controls.'
            )
        else:
            remediation_feedback['message'] = (
                'No effective security control selected yet. Choose a valid control and try again.'
            )
        refresh_all()

    @ui.refreshable
    def header_status_row():
        score = get_posture_score()
        risk_text, risk_badge_cls = get_risk_level(score)
        score_color = (
            'text-emerald-400' if score == 4
            else 'text-amber-300' if score >= 2
            else 'text-red-400'
        )
        with ui.row().classes('w-full gap-4 items-stretch flex-wrap'):
            with ui.card().classes('grow basis-72 bg-slate-900 border border-slate-700 p-4 justify-between'):
                with ui.row().classes('items-center justify-between w-full flex-wrap gap-2'):
                    ui.label('🏢 Goatify Payroll Management System').classes('text-base font-bold text-white')
                    ui.label(
                        f'Progress: {len(explored_objectives)} / {len(OBJECTIVES)} Explored • {remediated_count["value"]} Remediated'
                    ).classes('text-xs font-bold text-cyan-300 bg-slate-800 px-3 py-1 rounded-full border border-slate-700')
                ui.label(
                    'Target Asset: Payroll DB & Portal | Sample Record: John Doe (GF-10452) | Classification: Confidential'
                ).classes('text-xs text-gray-300 mt-1')
                with ui.row().classes('gap-2 mt-2 flex-wrap'):
                    for key, title in OBJECTIVES:
                        visited = key in explored_objectives
                        comp = is_compromised(key)
                        chip_cls = (
                            'bg-red-950/90 text-red-200 border-red-600' if comp
                            else 'bg-emerald-950/80 text-emerald-200 border-emerald-700' if visited
                            else 'bg-slate-800 text-gray-300 border-slate-700'
                        )
                        tag = 'Compromised' if comp else ('Explored' if visited else 'Unexplored')
                        ui.label(f'{title}: {tag}').classes(f'text-[11px] font-semibold px-2.5 py-0.5 rounded border {chip_cls}')
            with ui.card().classes('w-56 bg-slate-900 border border-slate-700 p-4 items-center justify-center'):
                ui.label('🛡 Security Posture').classes('text-xs font-bold text-gray-300 uppercase tracking-wider')
                ui.label(f'{score} / 4').classes(f'text-4xl font-extrabold {score_color} my-1')
                ui.label(risk_text).classes(f'text-[11px] font-extrabold px-2.5 py-0.5 rounded border {risk_badge_cls}')

    @ui.refreshable
    def objective_tabs():
        with ui.card().classes('w-full bg-slate-900 border border-slate-700 p-2 rounded-xl'):
            with ui.tabs(
                value=selected_objective['value'],
                on_change=lambda e: on_objective_tab_change(e.value)
            ).classes('w-full').props('dense active-color=cyan indicator-color=cyan align=justify'):
                for key, label in OBJECTIVES:
                    comp = is_compromised(key)
                    badge = ' [FAIL]' if comp else ' [OK]'
                    ui.tab(key, label=f'{label}{badge}').classes('text-red-300' if comp else 'text-white')

    @ui.refreshable
    def failure_toggle_bar():
        obj = selected_objective['value']
        comp = is_compromised(obj)
        obj_title = dict(OBJECTIVES)[obj]
        actor = SIMULATOR_DATA[obj]['actor']['compromised' if comp else 'secure']
        cissp = SIMULATOR_DATA[obj]['cissp']

        with ui.card().classes('w-full bg-slate-900 border border-slate-700 p-4 rounded-xl'):
            with ui.row().classes('items-center justify-between w-full flex-wrap gap-4'):
                with ui.row().classes('items-center gap-3'):
                    ui.label(f'Simulate Failure ({obj_title}):').classes('text-sm font-bold text-white')
                    ui.switch(
                        text='Failure Active' if comp else 'Secure Baseline',
                        value=comp,
                        on_change=lambda e: on_failure_switch_change(e.value)
                    ).props('color=red keep-color')
                ui.label(f'CISSP Mapping: {cissp["domain"]}').classes('text-xs font-semibold text-cyan-300')

            with ui.row().classes('w-full gap-4 mt-3 pt-3 border-t border-slate-800 flex-wrap'):
                with ui.column().classes('grow basis-64 gap-0.5'):
                    ui.label('🎭 Threat Actor & Root Cause').classes('text-[11px] font-bold text-amber-300 uppercase')
                    ui.label(f'{actor["name"]} ({actor["category"]})').classes('text-xs font-bold text-white')
                    ui.label(actor['root_cause']).classes('text-xs text-gray-300')

                with ui.column().classes('grow basis-64 gap-1'):
                    ui.label('📘 Exam Concepts').classes('text-[11px] font-bold text-cyan-300 uppercase')
                    with ui.row().classes('gap-1.5 flex-wrap'):
                        for concept in cissp['concepts']:
                            ui.label(concept).classes(
                                'text-[11px] font-semibold text-slate-100 bg-slate-800 border border-slate-700 px-2 py-0.5 rounded'
                            )

    def render_attack_flow_visual(obj: str, state: str):
        if obj == 'confidentiality':
            if state == 'protected':
                ui.label('🔒 Encrypted & Isolated').classes('text-xs font-bold text-emerald-400 mt-2')
                ui.html("""
                    <div style="background:#060913; border:1px solid #1e293b; border-radius:8px; padding:10px; margin-top:6px; font-family:monospace; font-size:12px; color:#e2e8f0;">
                        <div>[Payroll DB] ──(AES-256)──► [Private VPC] ──(Blocked)──► 🌐 Internet</div>
                        <div style="color:#4ade80; margin-top:6px;">John Doe: ████████ 🔒 | Salary: ████████ 🔒</div>
                    </div>
                """)
            else:
                ui.label('🚨 Data Exfiltration Flow').classes('text-xs font-bold text-red-300 mt-2')
                ui.html("""
                    <div class="flow-alert-box" style="background:#450a0a; border:1px solid #f87171; border-radius:8px; padding:10px; margin-top:6px; font-family:monospace; font-size:12px; color:#ffffff;">
                        <div style="font-weight:bold; color:#fca5a5;">
                            Exposed
                            <span class="exfil-dot">●</span><span class="exfil-dot">●</span><span class="exfil-dot">●</span><span class="exfil-dot">●</span><span class="exfil-dot">●</span>
                            <span class="exfil-arrow">►</span><span class="exfil-internet">🌐 Internet</span>
                        </div>
                        <div style="margin-top:8px; padding-top:6px; border-top:1px solid rgba(248,113,113,0.35); color:#ffffff;">
                            <div>1. John Doe (GF-10452) — ₹850,000</div>
                            <div>2. Sarah Smith (GF-10453) — ₹920,000</div>
                            <div>3. Mike Wilson (GF-10454) — ₹780,000</div>
                        </div>
                    </div>
                """)
        elif obj == 'integrity':
            if state == 'verified':
                ui.label('✅ Integrity Check Passed').classes('text-xs font-bold text-emerald-400 mt-2')
                ui.html("""
                    <div style="background:#060913; border:1px solid #1e293b; border-radius:8px; padding:10px; margin-top:6px; font-family:monospace; font-size:12px; color:#e2e8f0;">
                        <div>[Record GF-10452] ──► [SHA-256] ──► [Baseline Match]</div>
                        <div style="color:#4ade80; margin-top:6px;">₹850,000 | Hash Verified (No Alteration)</div>
                    </div>
                """)
            else:
                ui.label('⚠ Data Tampering Detection').classes('text-xs font-bold text-amber-300 mt-2')
                ui.html("""
                    <div class="flow-alert-box" style="background:#451a03; border:1px solid #f59e0b; border-radius:8px; padding:10px; margin-top:6px; font-family:monospace; font-size:12px; color:#ffffff;">
                        <div style="font-weight:bold; color:#fde68a;">[Altered Row] ──► [Hash Recalc] ──► [MISMATCH!]</div>
                        <div style="margin-top:8px; padding-top:6px; border-top:1px solid rgba(251,191,36,0.35); color:#ffffff;">
                            <div>John Doe: ₹850,000 ──► ₹9,850,000</div>
                            <div>Sarah Smith: ₹920,000 ──► ₹4,920,000</div>
                            <div>Mike Wilson: ₹780,000 ──► ₹7,780,000</div>
                        </div>
                    </div>
                """)
        elif obj == 'availability':
            if state == 'online':
                ui.label('🟢 Service Path Healthy').classes('text-xs font-bold text-emerald-400 mt-2')
                ui.html("""
                    <div style="background:#060913; border:1px solid #1e293b; border-radius:8px; padding:10px; margin-top:6px; font-family:monospace; font-size:12px; color:#e2e8f0;">
                        <div>[Client] ──► [Load Balancer] ──► [Payroll API: 200 OK]</div>
                        <div style="color:#4ade80; margin-top:6px;">All 3 Nodes Healthy • SLA Met</div>
                    </div>
                """)
            else:
                ui.label('🔴 Service Outage Progression').classes('text-xs font-bold text-red-300 mt-2')
                ui.html("""
                    <div class="flow-alert-box" style="background:#450a0a; border:1px solid #f87171; border-radius:8px; padding:10px; margin-top:6px; font-family:monospace; font-size:12px; color:#ffffff;">
                        <div style="font-weight:bold; color:#fca5a5;">[Timeout] ──► [503 Error] ──► [Circuit OPEN / Offline]</div>
                        <div style="margin-top:8px; padding-top:6px; border-top:1px solid rgba(248,113,113,0.35); color:#ffffff;">
                            <div>Payslip Portal: Unreachable (503)</div>
                            <div>Payroll Batch Job: Halted</div>
                        </div>
                    </div>
                """)
        else:
            if state == 'signed':
                ui.label('✍ Cryptographic Attribution Valid').classes('text-xs font-bold text-emerald-400 mt-2')
                ui.html("""
                    <div style="background:#060913; border:1px solid #1e293b; border-radius:8px; padding:10px; margin-top:6px; font-family:monospace; font-size:12px; color:#e2e8f0;">
                        <div>[Approval] ──► [Private Key Sign] ──► [Cert Verified]</div>
                        <div style="color:#4ade80; margin-top:6px;">Signer: hr.lead@goatify.io (Non-Repudiable)</div>
                    </div>
                """)
            else:
                ui.label('⚠ Signature Verification Failure').classes('text-xs font-bold text-purple-300 mt-2')
                ui.html("""
                    <div class="flow-alert-box" style="background:#3b0764; border:1px solid #c084fc; border-radius:8px; padding:10px; margin-top:6px; font-family:monospace; font-size:12px; color:#ffffff;">
                        <div style="font-weight:bold; color:#f3e8ff;">[Action] ──► [Missing/Bad Cert] ──► [Origin Unproven]</div>
                        <div style="margin-top:8px; padding-top:6px; border-top:1px solid rgba(192,132,252,0.35); color:#ffffff;">
                            <div>Bonus Adjustment: Unsigned / Disputed</div>
                            <div>Audit Proof: Insufficient for Repudiation Defense</div>
                        </div>
                    </div>
                """)

    @ui.refreshable
    def remediation_panel():
        obj = selected_objective['value']
        comp = is_compromised(obj)
        info = SIMULATOR_DATA[obj]
        content = info[system_states[obj]]

        with ui.card().classes('grow basis-64 bg-slate-900 border border-slate-700 min-h-80 p-4 justify-between'):
            with ui.column().classes('gap-2'):
                ui.label('🛠 Interactive Remediation & Controls').classes('text-xs font-bold text-emerald-300 uppercase tracking-wider')
                ui.label(content['controls']['title']).classes('font-bold text-white text-sm')
                ui.label(content['controls']['details']).classes('text-xs text-gray-300')

                if comp:
                    ui.label('Select controls to apply:').classes('text-xs font-bold text-cyan-300 mt-2')
                    for ctrl in info['controls_catalog']:
                        is_checked = ctrl['id'] in selected_controls[obj]
                        ui.checkbox(
                            text=ctrl['label'],
                            value=is_checked,
                            on_change=lambda e, c_id=ctrl['id']: toggle_control_selection(obj, c_id, e.value)
                        ).classes('text-xs text-white')
                else:
                    ui.label('All security controls for this objective are currently active.').classes('text-xs text-emerald-300 mt-2')

            with ui.column().classes('gap-2 mt-3 pt-3 border-t border-slate-800'):
                if comp:
                    ui.button(
                        'Apply Selected Controls & Remediate',
                        on_click=apply_remediation
                    ).props('color=positive unelevated no-caps').classes('w-full font-bold')
                ui.label(remediation_feedback['message']).classes('text-[11px] text-amber-200')

    @ui.refreshable
    def workspace():
        obj = selected_objective['value']
        state = system_states[obj]
        info = SIMULATOR_DATA[obj]
        content = info[state]
        tel = info['telemetry'][state]

        with ui.row().classes('w-full gap-4 items-stretch'):
            with ui.card().classes('grow basis-72 bg-slate-900 border border-slate-700 min-h-80 p-4'):
                with ui.row().classes('items-center justify-between w-full'):
                    ui.label('📄 Data & Telemetry').classes('text-xs font-bold text-cyan-300 uppercase tracking-wider')
                    with ui.row().classes('items-center gap-1.5 bg-slate-950 px-2.5 py-1 rounded-full border border-slate-700'):
                        ui.html(
                            f'<span style="display:inline-block;width:9px;height:9px;border-radius:999px;background:{tel["led"]};box-shadow:0 0 8px {tel["led"]};"></span>'
                        )
                        ui.label(tel['led_label']).classes('text-[11px] font-extrabold text-white')

                with ui.column().classes('gap-1 mt-2 p-2.5 rounded bg-slate-950 border border-slate-800 text-xs font-mono'):
                    ui.label(f'Conn : {tel["connection"]}').classes('text-gray-200')
                    ui.label(f'Check: {tel["hash_or_sig"]}').classes('text-cyan-200')
                    ui.label(f'State: {tel["health"]}').classes('text-gray-200')

                render_attack_flow_visual(obj, state)
                ui.label(content['data']['title']).classes('font-bold text-white text-sm mt-3')
                ui.label(content['data']['details']).classes('text-gray-300 text-xs mt-1')

            with ui.card().classes('grow basis-56 bg-slate-900 border border-slate-700 min-h-80 p-4'):
                ui.label('📈 Business Impact').classes('text-xs font-bold text-orange-300 uppercase tracking-wider')
                ui.label(content['impact']['title']).classes('font-bold text-white text-base mt-3')
                ui.label(content['impact']['details']).classes('text-gray-200 text-sm mt-2')

            remediation_panel()

            with ui.card().classes('grow basis-56 bg-slate-900 border border-slate-700 min-h-80 p-4'):
                ui.label('📰 Real World Incident').classes('text-xs font-bold text-red-300 uppercase tracking-wider')
                ui.label(content['incident']['title']).classes('font-bold text-white text-base mt-3')
                ui.label(content['incident']['details']).classes('text-gray-200 text-sm mt-2')

    @ui.refreshable
    def timeline_section():
        obj = selected_objective['value']
        comp = is_compromised(obj)
        was_remediated = (not comp) and (remediated_count['value'] > 0) and (not pending_remediation[obj])

        stages = [
            ('1. Secure Baseline', 'Controls active and system operating normally.',
             'border-emerald-600 bg-emerald-950/50 text-emerald-200' if not comp else 'border-slate-700 bg-slate-800/60 text-gray-300'),
            ('2. Detection', 'Telemetry or hash/health/cert check flags anomaly.',
             'border-amber-500 bg-amber-950/60 text-amber-200' if comp else 'border-slate-700 bg-slate-800/50 text-gray-300'),
            ('3. Business Impact', 'Exposure, tampering, downtime, or dispute risk occurs.',
             'border-red-500 bg-red-950/70 text-red-200' if comp else 'border-slate-700 bg-slate-800/50 text-gray-300'),
            ('4. Remediation', 'Verified controls applied and posture restored.',
             'border-cyan-400 bg-cyan-950/60 text-cyan-200' if was_remediated else 'border-slate-700 bg-slate-800/50 text-gray-300'),
        ]

        with ui.card().classes('w-full bg-slate-900 border border-slate-700 p-4 rounded-xl'):
            ui.label('⏱ Incident & Remediation Timeline').classes('text-xs font-bold text-cyan-300 uppercase tracking-wider mb-2')
            with ui.row().classes('w-full gap-3 flex-wrap'):
                for title, desc, style_cls in stages:
                    with ui.card().classes(f'grow basis-52 p-3 border rounded-lg {style_cls}'):
                        ui.label(title).classes('text-xs font-extrabold')
                        ui.label(desc).classes('text-xs mt-1 text-gray-200')

    with ui.column().classes('w-full max-w-7xl mx-auto p-4 gap-4'):
        ui.label('🔐 CISSP Practical Lab — CIA & Non-Repudiation').classes('text-3xl font-bold text-white')
        ui.label('Domain 3 — Security Architecture & Engineering').classes('text-sm text-gray-300')
        header_status_row()
        objective_tabs()
        failure_toggle_bar()
        workspace()
        timeline_section()