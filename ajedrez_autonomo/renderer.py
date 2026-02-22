from __future__ import annotations

from typing import Iterable, List

from .simulation import Scenario, StrategyPlan

PIECE_GLYPHS = {
    "K": "WK",
    "Q": "WQ",
    "R": "WR",
    "B": "WB",
    "N": "WN",
    "P": "WP",
    "k": "BK",
    "q": "BQ",
    "r": "BR",
    "b": "BB",
    "n": "BN",
    "p": "BP",
    ".": "..",
}


def _make_box(title: str, lines: List[str], width: int = 44) -> List[str]:
    inner = max(width - 4, len(title) + 2, *(len(line) for line in lines))
    top = f"+{'-' * (inner + 2)}+"
    header = f"| {title.ljust(inner)} |"
    separator = f"+{'=' * (inner + 2)}+"
    body = [f"| {line.ljust(inner)} |" for line in lines]
    return [top, header, separator, *body, top]


def board_to_ascii_lines(board_grid: List[List[str]]) -> List[str]:
    lines = []
    for r, row in enumerate(board_grid):
        cells = " | ".join(PIECE_GLYPHS[p] for p in row)
        lines.append(f"{8-r} | {cells} |")
    lines.append("    a    b    c    d    e    f    g    h")
    return lines


def format_scenario(scenario: Scenario) -> List[str]:
    lines = [
        f"Turno: {'Blancas' if scenario.board.turn == 'w' else 'Negras'}",
        f"Score estimado: {scenario.score:.2f}",
        f"Estado: {'Finalizada' if scenario.finished else 'En juego'}",
        "",
        *board_to_ascii_lines(scenario.board.grid),
    ]
    if scenario.board.move_stack:
        lines.append(f"Último movimiento: {scenario.board.move_stack[-1].uci()}")
    else:
        lines.append("Último movimiento: -")
    return _make_box(scenario.name, lines)


def render_side_by_side(scenarios: Iterable[Scenario], spacing: int = 4) -> str:
    blocks = [format_scenario(s) for s in scenarios]
    if not blocks:
        return "(sin escenarios)"

    max_height = max(len(block) for block in blocks)
    normalized = [block + [""] * (max_height - len(block)) for block in blocks]
    widths = [max(len(line) for line in block) for block in normalized]

    output = []
    for row in range(max_height):
        output.append((" " * spacing).join(normalized[col][row].ljust(widths[col]) for col in range(len(normalized))))
    return "\n".join(output)


def render_strategy_playbook(plans: List[StrategyPlan]) -> str:
    if not plans:
        return "No hay planes disponibles."

    lines = []
    for idx, plan in enumerate(plans, start=1):
        lines.append(f"PLAN {idx}: juega {plan.recommended_move.uci()}  (score proyectado: {plan.projected_score:.2f})")
        if not plan.responses:
            lines.append("  - Sin respuestas rivales registradas.")
            lines.append("")
            continue

        for branch in plan.responses:
            response = branch.our_response.uci() if branch.our_response else "(sin respuesta)"
            lines.append(
                "  - Si rival juega "
                f"{branch.opponent_move.uci()} (score: {branch.opponent_score:.2f}), "
                f"responde con {response} (nuevo score: {branch.response_score:.2f})"
            )
        lines.append("")
    return "\n".join(lines).strip()
