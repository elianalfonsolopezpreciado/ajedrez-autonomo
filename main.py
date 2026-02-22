from __future__ import annotations

import argparse

from ajedrez_autonomo.renderer import render_side_by_side
from ajedrez_autonomo.simulation import MultiBoardSimulation


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Simulador de ajedrez en paralelo por terminal. "
            "Explora múltiples ramas de juego y muestra tableros ASCII en simultáneo."
        )
    )
    parser.add_argument("--depth", type=int, default=3, help="Profundidad de búsqueda minimax")
    parser.add_argument("--branches", type=int, default=3, help="Cantidad de escenarios paralelos")
    parser.add_argument("--plies", type=int, default=12, help="Máximo de medios movimientos por escenario")
    parser.add_argument("--fen", type=str, default=None, help="Posición inicial en formato FEN")
    return parser


def main() -> None:
    args = build_parser().parse_args()

    simulation = MultiBoardSimulation(depth=args.depth, branches=args.branches, max_plies=args.plies)
    scenarios = simulation.run(fen=args.fen)

    print("=" * 100)
    print("AJEDREZ AUTÓNOMO (APROXIMACIÓN)")
    print("Nota: en ajedrez perfecto no existe garantía de 'siempre ganar' desde la posición inicial.")
    print("El motor aplica minimax + poda alpha-beta para aproximar jugadas robustas.")
    print("=" * 100)
    print(render_side_by_side(scenarios))


if __name__ == "__main__":
    main()
