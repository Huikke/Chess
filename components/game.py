import components.pieces as pieces

class Chess():
    starting_pieces = [
        pieces.Rook("B", (0, 0)),
        pieces.Knight("B", (0, 1)),
        pieces.Bishop("B", (0, 2)),
        pieces.Queen("B", (0, 3)),
        pieces.King("B", (0, 4)),
        pieces.Bishop("B", (0, 5)),
        pieces.Knight("B", (0, 6)),
        pieces.Rook("B", (0, 7)),
        pieces.Rook("W", (7, 0)),
        pieces.Knight("W", (7, 1)),
        pieces.Bishop("W", (7, 2)),
        pieces.Queen("W", (7, 3)),
        pieces.King("W", (7, 4)),
        pieces.Bishop("W", (7, 5)),
        pieces.Knight("W", (7, 6)),
        pieces.Rook("W", (7, 7)),
        pieces.Pawn("B", (1, 0)),
        pieces.Pawn("B", (1, 1)),
        pieces.Pawn("B", (1, 2)),
        pieces.Pawn("B", (1, 3)),
        pieces.Pawn("B", (1, 4)),
        pieces.Pawn("B", (1, 5)),
        pieces.Pawn("B", (1, 6)),
        pieces.Pawn("B", (1, 7)),
        pieces.Pawn("W", (6, 0)),
        pieces.Pawn("W", (6, 1)),
        pieces.Pawn("W", (6, 2)),
        pieces.Pawn("W", (6, 3)),
        pieces.Pawn("W", (6, 4)),
        pieces.Pawn("W", (6, 5)),
        pieces.Pawn("W", (6, 6)),
        pieces.Pawn("W", (6, 7))
    ]

    def __init__(self):
        self.board_pieces = list(self.starting_pieces)
        self.turn = "W"
        self.castling = ["K", "Q", "k", "q"]
        self.en_passant = "-"
        self.halfmove_clock = 0
        self.fullmove_counter = 1

    def state(self):
        return self.board_pieces

    def move(self, str_coord, dest_coord):
        en_passant_check = self.en_passant

        for piece in self.board_pieces:
            if piece.position == str_coord:
                move_check = piece.movement(dest_coord, self)
                if move_check == True:
                    # Set en passant back to "-" if it wasn't set up this turn
                    if self.en_passant == en_passant_check:
                        self.en_passant = "-"
                    piece.position = dest_coord
                    return True
                else:
                    return False
        return False