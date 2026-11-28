from nicegui import ui
from layout import page_shell


@ui.page('/labs/crypto-concepts')
def crypto_concepts_page():
    page_shell('Cryptographic Concepts & Kerckhoffs', lab_id='crypto_concepts')
    n_users = {'value': 10}

    @ui.refreshable
    def render_calc():
        n = int(n_users['value'] or 2)
        sym_keys = n * (n - 1) // 2
        asym_keys = 2 * n

        with ui.row().classes('w-full gap-4 items-stretch flex-wrap'):
            with ui.card().classes('grow basis-64 bg-slate-900 border border-slate-700 p-4'):
                ui.label('Symmetric Key Distribution: N(N - 1) / 2').classes('text-xs font-bold text-emerald-400 uppercase')
                ui.label('Shared secret key per pair; fast bulk encryption, higher key-exchange overhead as N grows.').classes('text-xs text-gray-300 mt-1')
                ui.label(f'Keys needed for {n} users: {sym_keys:,}').classes('text-lg font-bold text-amber-300 mt-3')

            with ui.card().classes('grow basis-64 bg-slate-900 border border-slate-700 p-4'):
                ui.label('Asymmetric Key Pairs: 2N').classes('text-xs font-bold text-purple-400 uppercase')
                ui.label('Public/private key pair per user; simplifies key distribution and supports digital signatures.').classes('text-xs text-gray-300 mt-1')
                ui.label(f'Key pairs for {n} users: {asym_keys:,}').classes('text-lg font-bold text-cyan-300 mt-3')

    with ui.column().classes('w-full max-w-6xl mx-auto p-6 gap-4'):
        ui.label('🔑 Cryptographic Concepts & Kerckhoffs’ Principle').classes('text-2xl font-bold text-white')
        ui.number(
            'Number of Communicating Users (N)',
            value=n_users['value'],
            min=2,
            max=500,
            on_change=lambda e: (n_users.update({'value': e.value or 2}), render_calc.refresh())
        ).props('dark dense').classes('w-64')
        render_calc()

        with ui.row().classes('w-full gap-4 items-stretch flex-wrap mt-2'):
            with ui.card().classes('grow basis-64 bg-slate-900 border border-emerald-800 p-4'):
                ui.label('✅ Kerckhoffs’ Principle').classes('text-sm font-bold text-emerald-400')
                ui.label('Security rests on keeping the key secret—not hiding the algorithm. Public scrutiny strengthens proven ciphers.').classes('text-xs text-gray-200 mt-1')

            with ui.card().classes('grow basis-64 bg-slate-900 border border-red-800 p-4'):
                ui.label('❌ Security Through Obscurity').classes('text-sm font-bold text-red-400')
                ui.label('Relying on a secret algorithm is brittle: once reverse-engineered or leaked, all protected data is exposed.').classes('text-xs text-gray-200 mt-1')