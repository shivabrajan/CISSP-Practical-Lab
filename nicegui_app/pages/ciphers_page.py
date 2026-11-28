import random
from nicegui import ui
from layout import page_shell


def rail_fence_encrypt(text: str, rails: int) -> tuple[str, list[str]]:
    if rails <= 1 or not text:
        return text, [text]
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    for ch in text:
        fence[rail].append(ch)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction
    rows = [''.join(r) for r in fence]
    return ''.join(rows), rows


def caesar_encrypt(text: str, shift: int) -> str:
    out = []
    for ch in text.upper():
        if 'A' <= ch <= 'Z':
            out.append(chr((ord(ch) - 65 + shift) % 26 + 65))
        else:
            out.append(ch)
    return ''.join(out)


@ui.page('/labs/ciphers')
def ciphers_page():
    page_shell('Ciphers, OTP & Stream/Block (In Progress)', lab_id='ciphers')

    state = {
        'trans_text': 'CONFIDENTIALPAYROLL',
        'rails': 3,
        'sub_text': 'ATTACKATDAWN',
        'shift': 3,
        'otp_text': 'SECRET',
        'otp_key': ''.join(chr(random.randint(65, 90)) for _ in range(6)),
        'lfsr': [1, 0, 1, 1],
        'keystream': [],
    }

    def regen_otp(length: int):
        state['otp_key'] = ''.join(chr(random.randint(65, 90)) for _ in range(max(1, length)))

    def step_lfsr():
        reg = state['lfsr']
        feedback = reg[0] ^ reg[3]
        out_bit = reg[-1]
        state['lfsr'] = [feedback] + reg[:-1]
        state['keystream'].append(str(out_bit))
        if len(state['keystream']) > 16:
            state['keystream'] = state['keystream'][-16:]
        render_ciphers.refresh()

    @ui.refreshable
    def render_ciphers():
        rails = max(2, min(6, int(state['rails'] or 2)))
        shift = max(1, min(25, int(state['shift'] or 1)))
        rf_cipher, rf_rows = rail_fence_encrypt(state['trans_text'], rails)
        sub_cipher = caesar_encrypt(state['sub_text'], shift)

        otp_plain = state['otp_text'].upper()
        otp_key = state['otp_key'].upper().ljust(len(otp_plain), 'K')[:len(otp_plain)]
        hex_bytes = [f'{ord(p) ^ ord(k):02X}' for p, k in zip(otp_plain, otp_key)]

        shifted_alpha = ' '.join(chr((i + shift) % 26 + 65) for i in range(26))
        ks_display = ' '.join(state['keystream']) if state['keystream'] else '(click Step LFSR to generate bits)'

        with ui.column().classes('w-full gap-4'):
            with ui.row().classes('w-full gap-4 items-stretch flex-wrap'):
                # 1. Transposition
                with ui.card().classes('grow basis-80 bg-slate-900 border border-slate-700 p-4'):
                    ui.label('6. Transposition Cipher (Rail Fence)').classes('text-xs font-bold text-cyan-300 uppercase')
                    ui.label('Rearranges character positions without changing characters (Diffusion).').classes('text-xs text-gray-300 mt-1')
                    ui.input('Plaintext', value=state['trans_text'],
                             on_change=lambda e: (state.update({'trans_text': e.value}), render_ciphers.refresh())).props('dark dense').classes('mt-2')
                    ui.number('Rails', value=rails, min=2, max=6,
                              on_change=lambda e: (state.update({'rails': int(e.value or 2)}), render_ciphers.refresh())).props('dark dense').classes('mt-2')
                    ui.label(f'Ciphertext: {rf_cipher}').classes('text-sm font-bold text-amber-300 mt-2')
                    ui.label('\n'.join(f'Rail {i + 1}: {r}' for i, r in enumerate(rf_rows))).classes('mono-box mt-2')

                # 2. Substitution
                with ui.card().classes('grow basis-80 bg-slate-900 border border-slate-700 p-4'):
                    ui.label('7. Substitution Cipher (Caesar Shift)').classes('text-xs font-bold text-cyan-300 uppercase')
                    ui.label('Replaces characters with shifted letters (Confusion); vulnerable to frequency analysis.').classes('text-xs text-gray-300 mt-1')
                    ui.input('Plaintext', value=state['sub_text'],
                             on_change=lambda e: (state.update({'sub_text': e.value}), render_ciphers.refresh())).props('dark dense').classes('mt-2')
                    ui.number('Shift Key', value=shift, min=1, max=25,
                              on_change=lambda e: (state.update({'shift': int(e.value or 1)}), render_ciphers.refresh())).props('dark dense').classes('mt-2')
                    ui.label(f'Ciphertext: {sub_cipher}').classes('text-sm font-bold text-amber-300 mt-2')
                    ui.label(f'A-Z Shift:\n{shifted_alpha}').classes('mono-box mt-2')

            with ui.row().classes('w-full gap-4 items-stretch flex-wrap'):
                # 3. One-Time Pad
                with ui.card().classes('grow basis-80 bg-slate-900 border border-slate-700 p-4'):
                    ui.label('8. One-Time Pad (Vernam XOR)').classes('text-xs font-bold text-cyan-300 uppercase')
                    ui.label('Requires truly random key, length >= plaintext, and single use only.').classes('text-xs text-gray-300 mt-1')
                    ui.input('Plaintext', value=state['otp_text'],
                             on_change=lambda e: (state.update({'otp_text': e.value}), regen_otp(len(e.value)), render_ciphers.refresh())).props('dark dense').classes('mt-2')
                    ui.button('Generate New Random Key', on_click=lambda: (regen_otp(len(state['otp_text'])), render_ciphers.refresh())).props('dense no-caps color=purple').classes('mt-2')
                    ui.label(f'Pad Key   : {otp_key}\nXOR (Hex) : {" ".join(hex_bytes)}').classes('mono-box mt-2')

                # 4. Stream vs Block & Confusion vs Diffusion
                with ui.card().classes('grow basis-80 bg-slate-900 border border-slate-700 p-4'):
                    ui.label('9. Stream vs. Block & Confusion / Diffusion').classes('text-xs font-bold text-cyan-300 uppercase')
                    ui.label(f'LFSR Register: {state["lfsr"]}').classes('mono-box mt-2')
                    ui.button('Step LFSR (1 Clock)', on_click=step_lfsr).props('dense no-caps color=cyan text-color=dark').classes('mt-2')
                    ui.label(f'Keystream Bits: {ks_display}').classes('text-xs font-mono text-emerald-300 mt-2')

                    ui.label('• Stream Cipher: Bit/byte-by-bit (low latency); Block Cipher: Fixed blocks (e.g., AES).').classes('text-xs text-gray-200 mt-2')
                    ui.label('• Confusion: Obscures key-to-ciphertext relation; Diffusion: Spreads plaintext structure.').classes('text-xs text-amber-200 mt-1')

    with ui.column().classes('w-full max-w-6xl mx-auto p-6 gap-4'):
        with ui.row().classes('items-center justify-between w-full flex-wrap gap-2'):
            with ui.row().classes('items-center gap-3'):
                ui.label('🔀 Ciphers, One-Time Pad & Stream/Block').classes('text-2xl font-bold text-white')
                ui.label('IN PROGRESS').classes('text-xs font-bold px-2.5 py-0.5 rounded border bg-amber-950 text-amber-300 border-amber-700')
            ui.label('Domain 3 — Classical & Modern Ciphers').classes('text-xs text-cyan-300 font-semibold')
        render_ciphers()