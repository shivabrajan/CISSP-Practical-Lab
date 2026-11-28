from nicegui import ui
from registry import LAB_CATALOG, get_visited_set, mark_visited

SHARED_STYLES = """
<style>
body, .q-page {
    background: #0B1120 !important;
    color: #F8FAFC !important;
}

.q-card {
    transition: all 0.25s ease;
}

.q-toggle__label, .q-checkbox__label, .q-tab__label, .q-field__native, .q-radio__label {
    color: #F8FAFC !important;
    font-weight: 600 !important;
}

.mono-box {
    font-family: monospace;
    font-size: 12px;
    background: #060913;
    border: 1px solid #1E293B;
    border-radius: 6px;
    padding: 10px;
    color: #38BDF8;
}

@keyframes dotFlow {
    0%, 15%   { opacity: 0.25; transform: scale(0.85); }
    20%, 85%  { opacity: 1;    transform: scale(1.25); }
    100%      { opacity: 0.25; transform: scale(0.85); }
}

.exfil-dot {
    display: inline-block;
    color: #EF4444 !important;
    font-size: 14px;
    font-weight: bold;
    animation: dotFlow 2.2s infinite;
}
.exfil-dot:nth-child(1) { animation-delay: 0.0s; }
.exfil-dot:nth-child(2) { animation-delay: 0.2s; }
.exfil-dot:nth-child(3) { animation-delay: 0.4s; }
.exfil-dot:nth-child(4) { animation-delay: 0.6s; }
.exfil-dot:nth-child(5) { animation-delay: 0.8s; }

.exfil-arrow {
    display: inline-block;
    color: #FCA5A5 !important;
    font-weight: bold;
    animation: dotFlow 2.2s infinite;
    animation-delay: 1.0s;
}

.exfil-internet {
    display: inline-block;
    color: #FFFFFF !important;
    font-weight: bold;
    animation: dotFlow 2.2s infinite;
    animation-delay: 1.2s;
}

@keyframes rowPulse {
    0%, 100% { background: rgba(127, 29, 29, 0.35); }
    50%      { background: rgba(239, 68, 68, 0.45); }
}

.flow-alert-box {
    animation: rowPulse 2.4s infinite;
}
</style>
"""


def page_shell(page_title: str, lab_id: str | None = None) -> None:
    ui.add_head_html(SHARED_STYLES)
    if lab_id:
        mark_visited(lab_id)

    visited = get_visited_set()
    ready_count = sum(1 for item in LAB_CATALOG if item['status'] == 'Ready')
    wip_count = sum(1 for item in LAB_CATALOG if item['status'] == 'In Progress')

    with ui.header().classes('bg-slate-900 border-b border-slate-800 px-6 py-3 items-center justify-between'):
        with ui.row().classes('items-center gap-3 flex-wrap'):
            ui.link('📚 Lab Index', '/').classes('text-cyan-300 font-bold no-underline text-sm')
            ui.label('/').classes('text-slate-600')
            ui.label(page_title).classes('text-white font-bold text-sm')

        ui.label(
            f'Visited: {len(visited)}/{len(LAB_CATALOG)} • Ready: {ready_count} • In Progress: {wip_count}'
        ).classes('text-xs font-mono text-slate-300')