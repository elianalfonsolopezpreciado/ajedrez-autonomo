from __future__ import annotations

from typing import Iterable, List

from .simulation import Scenario


def board_to_ascii_lines(board_grid: List[List[str]]) -> List[str]:
    lines = []
    for r, row in enumerate(board_grid):
        lines.append(f"{8-r} " + " ".join(row))
    lines.append("  a b c d e f g h")
    return lines


def format_scenario(scenario: Scenario) -> List[str]:
    lines = [
        scenario.name,
        f"Turno: {'Blancas' if scenario.board.turn == 'w' else 'Negras'}",
        f"Score: {scenario.score:.2f}",
        f"Estado: {'Finalizada' if scenario.finished else 'En juego'}",
    ]
    lines.extend(board_to_ascii_lines(scenario.board.grid))
    if scenario.board.move_stack:
        lines.append(f"Último movimiento: {scenario.board.move_stack[-1].uci()}")
    else:
        lines.append("Último movimiento: -")
    return lines


def render_side_by_side(scenarios: Iterable[Scenario], spacing: int = 6) -> str:
    blocks = [format_scenario(s) for s in scenarios]
    if not blocks:
        return "(sin escenarios)"
    max_height = max(len(b) for b in blocks)
    blocks = [b + [""] * (max_height - len(b)) for b in blocks]
    widths = [max(len(line) for line in b) for b in blocks]

    output = []
    for i in range(max_height):
        output.append((" " * spacing).join(blocks[j][i].ljust(widths[j]) for j in range(len(blocks))))
    return "\n".join(output)
