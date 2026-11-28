from nicegui import ui

LAB_CATALOG = [
    {
        'id': 'cia_nr',
        'domain': 'Domain 3 — Security Architecture & Engineering',
        'title': '1. CIA & Non-Repudiation Triad Simulator',
        'route': '/labs/cia-nr',
        'status': 'Ready',
        'summary': 'Interactive payroll simulator with attack flows, telemetry LEDs, threat actors, timeline, and control remediation.',
    },
    {
        'id': 'crypto_concepts',
        'domain': 'Domain 3 — Cryptography',
        'title': '2 & 3. Cryptographic Concepts & Kerckhoffs’ Principle',
        'route': '/labs/crypto-concepts',
        'status': 'Ready',
        'summary': 'Symmetric vs. asymmetric key counts and open algorithm vs. security-through-obscurity.',
    },
    {
        'id': 'primitives',
        'domain': 'Domain 3 — Cryptography',
        'title': '4 & 5. Boolean Math, Modulo, Nonce, ZKP & Split Knowledge',
        'route': '/labs/primitives',
        'status': 'In Progress',
        'summary': 'Bitwise AND/OR/XOR, modulo arithmetic, SHA-256 hash, nonces, ZKP, and split knowledge.',
    },
    {
        'id': 'ciphers',
        'domain': 'Domain 3 — Cryptography',
        'title': '6–9. Transposition, Substitution, OTP & Stream/Block',
        'route': '/labs/ciphers',
        'status': 'In Progress',
        'summary': 'Rail Fence, Caesar shift, Vernam XOR One-Time Pad, LFSR stream, and confusion/diffusion.',
    },
]


def get_visited_set() -> set[str]:
    visited = ui.context.client.storage.get('visited_labs')
    if visited is None:
        visited = []
        ui.context.client.storage['visited_labs'] = visited
    return set(visited)


def mark_visited(lab_id: str) -> None:
    visited = get_visited_set()
    visited.add(lab_id)
    ui.context.client.storage['visited_labs'] = sorted(visited)