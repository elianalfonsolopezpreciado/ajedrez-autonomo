from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Optional

FILES = "abcdefgh"
RANKS = "12345678"


@dataclass(frozen=True, slots=True)
class Move:
    from_row: int
    from_col: int
    to_row: int
    to_col: int
    promotion: Optional[str] = None

    def uci(self) -> str:
        return (
            f"{FILES[self.from_col]}{8 - self.from_row}"
            f"{FILES[self.to_col]}{8 - self.to_row}"
            f"{self.promotion.lower() if self.promotion else ''}"
        )


class Board:
    def __init__(self, grid: Optional[List[List[str]]] = None, turn: str = "w") -> None:
        self.grid = grid if grid else self._initial_grid()
        self.turn = turn
        self.move_stack: List[Move] = []

    @staticmethod
    def _initial_grid() -> List[List[str]]:
        return [
            list("rnbqkbnr"),
            list("pppppppp"),
            list("........"),
            list("........"),
            list("........"),
            list("........"),
            list("PPPPPPPP"),
            list("RNBQKBNR"),
        ]

    def copy(self) -> "Board":
        new_board = Board([row[:] for row in self.grid], self.turn)
        new_board.move_stack = self.move_stack[:]
        return new_board

    def piece_at(self, row: int, col: int) -> str:
        return self.grid[row][col]

    def in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < 8 and 0 <= col < 8

    def side_of(self, piece: str) -> Optional[str]:
        if piece == ".":
            return None
        return "w" if piece.isupper() else "b"

    def apply_move(self, move: Move) -> None:
        piece = self.grid[move.from_row][move.from_col]
        self.grid[move.from_row][move.from_col] = "."
        if move.promotion:
            piece = move.promotion if self.turn == "w" else move.promotion.lower()
        self.grid[move.to_row][move.to_col] = piece
        self.move_stack.append(move)
        self.turn = "b" if self.turn == "w" else "w"

    def king_exists(self, side: str) -> bool:
        target = "K" if side == "w" else "k"
        return any(target in row for row in self.grid)

    def is_game_over(self) -> bool:
        if not self.king_exists("w") or not self.king_exists("b"):
            return True
        return len(self.legal_moves()) == 0

    def is_in_check(self, side: str) -> bool:
        king = "K" if side == "w" else "k"
        king_pos = None
        for r in range(8):
            for c in range(8):
                if self.grid[r][c] == king:
                    king_pos = (r, c)
                    break
            if king_pos:
                break
        if king_pos is None:
            return True

        enemy = "b" if side == "w" else "w"
        for move in self.pseudo_legal_moves(enemy):
            if (move.to_row, move.to_col) == king_pos:
                return True
        return False

    def legal_moves(self) -> List[Move]:
        moves = []
        for move in self.pseudo_legal_moves(self.turn):
            clone = self.copy()
            clone.apply_move(move)
            if not clone.is_in_check("b" if clone.turn == "w" else "w"):
                moves.append(move)
        return moves

    def pseudo_legal_moves(self, side: str) -> List[Move]:
        moves: List[Move] = []
        for r in range(8):
            for c in range(8):
                piece = self.grid[r][c]
                if piece == "." or self.side_of(piece) != side:
                    continue
                moves.extend(self._piece_moves(r, c, piece))
        return moves

    def _piece_moves(self, r: int, c: int, piece: str) -> Iterable[Move]:
        side = self.side_of(piece)
        assert side is not None
        lower = piece.lower()

        if lower == "p":
            direction = -1 if side == "w" else 1
            start_row = 6 if side == "w" else 1
            promo_row = 0 if side == "w" else 7

            one = r + direction
            if self.in_bounds(one, c) and self.grid[one][c] == ".":
                if one == promo_row:
                    yield Move(r, c, one, c, "Q")
                else:
                    yield Move(r, c, one, c)
                two = r + 2 * direction
                if r == start_row and self.grid[two][c] == ".":
                    yield Move(r, c, two, c)

            for dc in (-1, 1):
                nr, nc = r + direction, c + dc
                if self.in_bounds(nr, nc):
                    target = self.grid[nr][nc]
                    if target != "." and self.side_of(target) != side:
                        if nr == promo_row:
                            yield Move(r, c, nr, nc, "Q")
                        else:
                            yield Move(r, c, nr, nc)
            return

        if lower == "n":
            for dr, dc in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
                nr, nc = r + dr, c + dc
                if not self.in_bounds(nr, nc):
                    continue
                target = self.grid[nr][nc]
                if target == "." or self.side_of(target) != side:
                    yield Move(r, c, nr, nc)
            return

        if lower in {"b", "r", "q"}:
            directions = []
            if lower in {"b", "q"}:
                directions.extend([(-1, -1), (-1, 1), (1, -1), (1, 1)])
            if lower in {"r", "q"}:
                directions.extend([(-1, 0), (1, 0), (0, -1), (0, 1)])

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while self.in_bounds(nr, nc):
                    target = self.grid[nr][nc]
                    if target == ".":
                        yield Move(r, c, nr, nc)
                    else:
                        if self.side_of(target) != side:
                            yield Move(r, c, nr, nc)
                        break
                    nr += dr
                    nc += dc
            return

        if lower == "k":
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if not self.in_bounds(nr, nc):
                        continue
                    target = self.grid[nr][nc]
                    if target == "." or self.side_of(target) != side:
                        yield Move(r, c, nr, nc)

    @classmethod
    def from_fen(cls, fen: str) -> "Board":
        fields = fen.split()
        piece_field = fields[0]
        turn = fields[1] if len(fields) > 1 else "w"

        grid: List[List[str]] = []
        for rank in piece_field.split("/"):
            row: List[str] = []
            for ch in rank:
                if ch.isdigit():
                    row.extend("." for _ in range(int(ch)))
                else:
                    row.append(ch)
            if len(row) != 8:
                raise ValueError("FEN inválido: columnas incorrectas")
            grid.append(row)
        if len(grid) != 8:
            raise ValueError("FEN inválido: filas incorrectas")
        return cls(grid=grid, turn=turn)
