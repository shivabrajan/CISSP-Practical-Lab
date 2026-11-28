import os
from nicegui import ui
from layout import page_shell
from registry import LAB_CATALOG, get_visited_set
import pages  # noqa: F401 — registers all page routes automatically


@ui.page('/')
def index_page():
    page_shell('CISSP Practical Lab Index')
    visited = get_visited_set()

    with ui.column().classes('w-full max-w-6xl mx-auto p-6 gap-6'):
        ui.label('🔐 CISSP Practical Simulator Suite').classes('text-3xl font-bold text-white')
        ui.label(
            'Central index for your modular CISSP labs. Select a lab below to open its interactive simulator.'
        ).classes('text-sm text-slate-300')

        with ui.grid().classes('w-full grid-cols-1 md:grid-cols-2 gap-4'):
            for lab in LAB_CATALOG:
                is_ready = lab['status'] == 'Ready'
                is_visited = lab['id'] in visited
                status_cls = (
                    'bg-emerald-950 text-emerald-300 border-emerald-700'
                    if is_ready else
                    'bg-amber-950 text-amber-300 border-amber-700'
                )

                with ui.card().classes('bg-slate-900 border border-slate-700 p-5 justify-between gap-3'):
                    with ui.column().classes('gap-2'):
                        with ui.row().classes('items-center justify-between w-full'):
                            ui.label(lab['domain']).classes('text-xs font-bold text-cyan-300 uppercase')
                            with ui.row().classes('gap-2'):
                                if is_visited:
                                    ui.label('VISITED').classes('text-[10px] font-bold px-2 py-0.5 rounded border bg-cyan-950 text-cyan-200 border-cyan-700')
                                ui.label(lab['status'].upper()).classes(f'text-[10px] font-bold px-2 py-0.5 rounded border {status_cls}')

                        ui.label(lab['title']).classes('text-lg font-bold text-white')
                        ui.label(lab['summary']).classes('text-xs text-slate-300')

                    with ui.row().classes('justify-end mt-2'):
                        ui.button(
                            'Launch Lab' if is_ready else 'Open WIP Lab',
                            on_click=lambda r=lab['route']: ui.navigate.to(r)
                        ).props('unelevated no-caps color=cyan text-color=dark').classes('font-bold')


port = int(os.environ.get('PORT', 8080))
ui.run(title='CISSP Practical Lab Suite', host='0.0.0.0', port=port, reload=False)