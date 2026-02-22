from __future__ import annotations

from dataclasses import dataclass
from math import inf
from typing import List, Optional

from .chess_core import Board, Move

PIECE_VALUES = {
    "p": 100,
    "n": 320,
    "b": 330,
    "r": 500,
    "q": 900,
    "k": 20000,
}


@dataclass(slots=True)
class SearchResult:
    best_move: Optional[Move]
    score: float
    principal_variation: List[Move]


class ParallelSearchEngine:
    def __init__(self, depth: int = 3) -> None:
        self.depth = depth

    def evaluate(self, board: Board) -> float:
        if not board.king_exists("w"):
            return -inf
        if not board.king_exists("b"):
            return inf

        score = 0.0
        for row in board.grid:
            for piece in row:
                if piece == ".":
                    continue
                value = PIECE_VALUES[piece.lower()]
                score += value if piece.isupper() else -value

        mobility = len(board.legal_moves())
        score += 0.1 * mobility if board.turn == "w" else -0.1 * mobility
        return score

    def _minimax(self, board: Board, depth: int, alpha: float, beta: float, maximizing: bool) -> tuple[float, List[Move]]:
        if depth == 0 or board.is_game_over():
            return self.evaluate(board), []

        moves = board.legal_moves()
        if not moves:
            return self.evaluate(board), []

        best_line: List[Move] = []

        if maximizing:
            best = -inf
            for move in moves:
                clone = board.copy()
                clone.apply_move(move)
                score, line = self._minimax(clone, depth - 1, alpha, beta, False)
                if score > best:
                    best = score
                    best_line = [move] + line
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
            return best, best_line

        best = inf
        for move in moves:
            clone = board.copy()
            clone.apply_move(move)
            score, line = self._minimax(clone, depth - 1, alpha, beta, True)
            if score < best:
                best = score
                best_line = [move] + line
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best, best_line

    def best_move(self, board: Board) -> SearchResult:
        maximizing = board.turn == "w"
        score, line = self._minimax(board, self.depth, -inf, inf, maximizing)
        return SearchResult(best_move=line[0] if line else None, score=score, principal_variation=line)

    def top_candidate_moves(self, board: Board, count: int = 3) -> List[SearchResult]:
        maximizing = board.turn == "w"
        candidates: List[SearchResult] = []
        for move in board.legal_moves():
            clone = board.copy()
            clone.apply_move(move)
            score, line = self._minimax(clone, self.depth - 1, -inf, inf, not maximizing)
            candidates.append(SearchResult(best_move=move, score=score, principal_variation=[move] + line))

        candidates.sort(key=lambda x: x.score, reverse=maximizing)
        return candidates[:count]
