from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .chess_core import Board, Move
from .engine import ParallelSearchEngine


@dataclass(slots=True)
class OpponentLine:
    opponent_move: Move
    opponent_score: float
    our_response: Optional[Move]
    response_score: float


@dataclass(slots=True)
class StrategyPlan:
    recommended_move: Move
    projected_score: float
    responses: List[OpponentLine]


@dataclass(slots=True)
class Scenario:
    name: str
    board: Board
    score: float = 0.0
    finished: bool = False


class MultiBoardSimulation:
    def __init__(self, depth: int = 3, branches: int = 3, max_plies: int = 12) -> None:
        self.engine = ParallelSearchEngine(depth=depth)
        self.branches = branches
        self.max_plies = max_plies

    def start(self, fen: Optional[str] = None) -> List[Scenario]:
        base = Board.from_fen(fen) if fen else Board()
        openings = self.engine.top_candidate_moves(base, count=self.branches)
        scenarios: List[Scenario] = []

        for idx, candidate in enumerate(openings, start=1):
            board = base.copy()
            if candidate.best_move:
                board.apply_move(candidate.best_move)
            scenarios.append(Scenario(name=f"Escenario {idx}", board=board, score=candidate.score))
        return scenarios

    def build_strategy_playbook(self, fen: Optional[str] = None, response_count: int = 3) -> List[StrategyPlan]:
        base = Board.from_fen(fen) if fen else Board()
        first_moves = self.engine.top_candidate_moves(base, count=self.branches)
        plans: List[StrategyPlan] = []

        for candidate in first_moves:
            if not candidate.best_move:
                continue
            board_after_our_move = base.copy()
            board_after_our_move.apply_move(candidate.best_move)

            opponent_options = self.engine.top_candidate_moves(board_after_our_move, count=response_count)
            lines: List[OpponentLine] = []

            for option in opponent_options:
                if not option.best_move:
                    continue
                board_after_opponent = board_after_our_move.copy()
                board_after_opponent.apply_move(option.best_move)

                best_response = self.engine.best_move(board_after_opponent)
                lines.append(
                    OpponentLine(
                        opponent_move=option.best_move,
                        opponent_score=option.score,
                        our_response=best_response.best_move,
                        response_score=best_response.score,
                    )
                )

            plans.append(
                StrategyPlan(
                    recommended_move=candidate.best_move,
                    projected_score=candidate.score,
                    responses=lines,
                )
            )
        return plans

    def advance(self, scenarios: List[Scenario]) -> None:
        for scenario in scenarios:
            if scenario.finished or scenario.board.is_game_over():
                scenario.finished = True
                continue
            if len(scenario.board.move_stack) >= self.max_plies:
                scenario.finished = True
                continue

            decision = self.engine.best_move(scenario.board)
            if not decision.best_move:
                scenario.finished = True
                continue
            scenario.board.apply_move(decision.best_move)
            scenario.score = decision.score

    def run(self, fen: Optional[str] = None) -> List[Scenario]:
        scenarios = self.start(fen=fen)
        for _ in range(self.max_plies):
            if all(s.finished for s in scenarios):
                break
            self.advance(scenarios)
        return scenarios
