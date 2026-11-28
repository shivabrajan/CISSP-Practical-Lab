import hashlib
import random
from nicegui import ui
from layout import page_shell


@ui.page('/labs/primitives')
def primitives_page():
    page_shell('Boolean Math & Primitives (In Progress)', lab_id='primitives')

    state = {
        'a': 0b10101100,       # 172
        'b': 0b11001010,       # 202
        'shift_bits': 2,
        'val': 29,
        'mod': 7,
        'work_iters': 5000,
        'nonce': random.randint(100000, 999999),
        'used_nonces': set(),
        'replay_status': 'Fresh nonce ready — test replay protection below.',
        'zkp_step': 0,         # 0 = idle, 1 = commitment, 2 = challenge, 3 = response verified
        'split_m': 2,
        'split_n': 3,
        'custodians_present': 2,
    }

    def test_nonce(candidate: int, is_replay: bool):
        if is_replay:
            if candidate in state['used_nonces']:
                state['replay_status'] = f'BLOCKED: Nonce {candidate} already seen — Replay Attack prevented!'
            else:
                state['used_nonces'].add(candidate)
                state['replay_status'] = f'ACCEPTED (first use): Nonce {candidate} recorded in cache.'
        else:
            fresh = random.randint(100000, 999999)
            state['nonce'] = fresh
            state['used_nonces'].add(fresh)
            state['replay_status'] = f'ACCEPTED: Fresh single-use Nonce {fresh} issued.'
        render_body.refresh()

    def advance_zkp():
        state['zkp_step'] = (state['zkp_step'] % 3) + 1
        render_body.refresh()

    @ui.refreshable
    def render_body():
        a = int(state['a']) & 0xFF
        b = int(state['b']) & 0xFF
        shift = max(1, min(4, int(state['shift_bits'] or 1)))
        v = int(state['val'] or 0)
        m = max(2, int(state['mod'] or 2))
        iters = max(100, min(50000, int(state['work_iters'] or 1000)))

        # One-way digest + simulated work function (PBKDF2-HMAC-SHA256)
        raw_digest = hashlib.sha256(str(v).encode()).hexdigest()
        stretched = hashlib.pbkdf2_hmac(
            'sha256', str(v).encode(), b'goatify-salt', iters
        ).hex()

        custodians = int(state['custodians_present'])
        m_req = int(state['split_m'])
        n_tot = int(state['split_n'])
        secret_unlocked = custodians >= m_req

        with ui.column().classes('w-full gap-4'):
            # Row 1: Bitwise Operations & Modulo
            with ui.row().classes('w-full gap-4 items-stretch flex-wrap'):
                with ui.card().classes('grow basis-80 bg-slate-900 border border-slate-700 p-4'):
                    ui.label('1. Boolean Logic & Bit Shifts').classes('text-xs font-bold text-cyan-300 uppercase')
                    ui.label(f'A = {a:08b} ({a}) | B = {b:08b} ({b})').classes('mono-box mt-2')

                    ui.number('Left Shift Bits (A << k)', value=shift, min=1, max=4,
                              on_change=lambda e: (state.update({'shift_bits': int(e.value or 1)}), render_body.refresh())).props('dark dense').classes('mt-2')

                    ui.label(f'A AND B : {a & b:08b} ({a & b})  [Masking / Filtering]').classes('text-xs font-mono text-gray-200 mt-2')
                    ui.label(f'A OR  B : {a | b:08b} ({a | b})  [Setting Bits / Flags]').classes('text-xs font-mono text-gray-200')
                    ui.label(f'A XOR B : {a ^ b:08b} ({a ^ b})  [Toggle / Stream & OTP]').classes('text-xs font-mono text-amber-300 font-bold')
                    ui.label(f'A << {shift}  : {(a << shift) & 0xFF:08b} ({(a << shift) & 0xFF}) [8-bit wrap]').classes('text-xs font-mono text-cyan-200 mt-1')

                with ui.card().classes('grow basis-80 bg-slate-900 border border-slate-700 p-4'):
                    ui.label('2. Modulo Arithmetic & Work Function').classes('text-xs font-bold text-cyan-300 uppercase')
                    with ui.row().classes('gap-3 mt-1'):
                        ui.number('Dividend', value=v, min=0, max=99999,
                                  on_change=lambda e: (state.update({'val': e.value or 0}), render_body.refresh())).props('dark dense').classes('w-32')
                        ui.number('Modulus (N)', value=m, min=2, max=256,
                                  on_change=lambda e: (state.update({'mod': e.value or 2}), render_body.refresh())).props('dark dense').classes('w-32')

                    ui.label(f'Remainder: {v} mod {m} = {v % m}').classes('text-sm font-bold text-emerald-400 mt-2')
                    ui.label(f'One-Way SHA-256: {raw_digest[:28]}...').classes('mono-box mt-2')

                    ui.number('Key Stretching Iterations', value=iters, min=500, max=50000, step=500,
                              on_change=lambda e: (state.update({'work_iters': int(e.value or 1000)}), render_body.refresh())).props('dark dense').classes('mt-2')
                    ui.label(f'Work Function (PBKDF2 {iters}x): {stretched[:28]}...').classes('text-[11px] font-mono text-purple-300 mt-1')

            # Row 2: Nonce, Zero-Knowledge Proof, Split Knowledge
            with ui.row().classes('w-full gap-4 items-stretch flex-wrap'):
                with ui.card().classes('grow basis-80 bg-slate-900 border border-slate-700 p-4'):
                    ui.label('3. Cryptographic Nonce & Replay Defense').classes('text-xs font-bold text-cyan-300 uppercase')
                    ui.label('A nonce ("number used once") prevents attackers from replaying captured auth/API requests.').classes('text-xs text-gray-300 mt-1')
                    ui.label(f'Current Nonce: {state["nonce"]}').classes('mono-box mt-2')

                    with ui.row().classes('gap-2 mt-3 flex-wrap'):
                        ui.button('Issue Fresh Nonce', on_click=lambda: test_nonce(state['nonce'], False)).props('dense no-caps color=cyan text-color=dark')
                        ui.button('Simulate Replay Attack', on_click=lambda: test_nonce(state['nonce'], True)).props('dense no-caps color=negative')

                    ui.label(state['replay_status']).classes('text-xs font-semibold text-amber-200 mt-2')

                with ui.card().classes('grow basis-80 bg-slate-900 border border-slate-700 p-4'):
                    ui.label('4. Zero-Knowledge Proof (ZKP) Handshake').classes('text-xs font-bold text-cyan-300 uppercase')
                    ui.label('Prover demonstrates knowledge of a secret without disclosing the secret itself.').classes('text-xs text-gray-300 mt-1')

                    step = state['zkp_step']
                    steps_text = {
                        0: 'Step 0 (Ready): Secret payroll credential stays hidden locally.',
                        1: 'Step 1 (Commitment): Prover sends a cryptographic commitment (hides secret).',
                        2: 'Step 2 (Challenge): Verifier issues a random challenge bit/value.',
                        3: 'Step 3 (Response & Verify): Prover answers challenge; Verifier confirms validity with 0 secret leak.',
                    }
                    ui.label(steps_text[step]).classes('mono-box mt-2')
                    ui.button('Next ZKP Step', on_click=advance_zkp).props('dense no-caps color=purple').classes('mt-3')

                with ui.card().classes('grow basis-80 bg-slate-900 border border-slate-700 p-4'):
                    ui.label('5. Split Knowledge (M-of-N Quorum)').classes('text-xs font-bold text-cyan-300 uppercase')
                    ui.label('Splits root key/master secret into N shares; M shares are required to reconstruct.').classes('text-xs text-gray-300 mt-1')

                    ui.slider(min=0, max=n_tot, value=custodians,
                              on_change=lambda e: (state.update({'custodians_present': int(e.value)}), render_body.refresh())).props('label-always color=cyan').classes('mt-4')
                    ui.label(f'Key Custodians Present: {custodians} of {n_tot} (Required: {m_req})').classes('text-xs font-bold text-white')

                    status_cls = 'text-emerald-400' if secret_unlocked else 'text-amber-300'
                    status_msg = 'QUORUM MET: Master key reconstructed.' if secret_unlocked else 'LOCKED: Need more shares to reconstruct.'
                    ui.label(status_msg).classes(f'text-xs font-bold {status_cls} mt-2')

    with ui.column().classes('w-full max-w-6xl mx-auto p-6 gap-4'):
        with ui.row().classes('items-center justify-between w-full flex-wrap gap-2'):
            with ui.row().classes('items-center gap-3'):
                ui.label('⚙ Boolean Math & Cryptographic Primitives').classes('text-2xl font-bold text-white')
                ui.label('IN PROGRESS').classes('text-xs font-bold px-2.5 py-0.5 rounded border bg-amber-950 text-amber-300 border-amber-700')
            ui.label('Domain 3 — Cryptography Primitives').classes('text-xs text-cyan-300 font-semibold')
        render_body()