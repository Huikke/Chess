import components.pieces as pieces

class Chess():
    starting_pieces = [
        pieces.King("W", (7, 4)),
        pieces.King("B", (0, 4)),
        pieces.Queen("W", (7, 3)),
        pieces.Queen("B", (0, 3)),
        pieces.Rook("W", (7, 0)),
        pieces.Rook("W", (7, 7)),
        pieces.Rook("B", (0, 0)),
        pieces.Rook("B", (0, 7)),
        pieces.Bishop("W", (7, 2)),
        pieces.Bishop("W", (7, 5)),
        pieces.Bishop("B", (0, 2)),
        pieces.Bishop("B", (0, 5)),
        pieces.Knight("B", (0, 1)),
        pieces.Knight("B", (0, 6)),
        pieces.Knight("W", (7, 1)),
        pieces.Knight("W", (7, 6)),
        pieces.Pawn("W", (6, 0)),
        pieces.Pawn("W", (6, 1)),
        pieces.Pawn("W", (6, 2)),
        pieces.Pawn("W", (6, 3)),
        pieces.Pawn("W", (6, 4)),
        pieces.Pawn("W", (6, 5)),
        pieces.Pawn("W", (6, 6)),
        pieces.Pawn("W", (6, 7)),
        pieces.Pawn("B", (1, 0)),
        pieces.Pawn("B", (1, 1)),
        pieces.Pawn("B", (1, 2)),
        pieces.Pawn("B", (1, 3)),
        pieces.Pawn("B", (1, 4)),
        pieces.Pawn("B", (1, 5)),
        pieces.Pawn("B", (1, 6)),
        pieces.Pawn("B", (1, 7))
    ]

    def __init__(self):
        self.board_pieces = list(self.starting_pieces)
        self.previous_board_state = []
        # self.infinite = False
        self.turn = "W" #TODO
        self.castling = ["K", "Q", "k", "q"] #TODO
        self.en_passant = "-"
        self.halfmove_clock = 0 #TODO
        self.fullmove_counter = 1 #TODO

    def state(self):
        return self.board_pieces

    def move(self, str_coord, dest_coord):
        en_passant_check = self.en_passant
        # if self.infinite == False and self.check_check() == True:
        #     self.infinite == True
        #     for piece in self.board_pieces:
        #         if piece.color == self.turn:
        #             for x in range(8):
        #                 for y in range(8):
        #                     if self.move(piece.position, (x, y)) == True:

        #     self.infinite == False

        for piece in self.board_pieces:
            if piece.position == str_coord:
                row_distance, col_distance = piece.coord_distance(dest_coord)
                # Each if clauses check the legality of the move
                if piece.movement(row_distance, col_distance) == False:
                    return False
                if piece.obstacle_check(row_distance, col_distance, self) == False and isinstance(piece, pieces.Knight) == False:
                    return False
                if piece.destination_check(dest_coord, self) == False:
                    return False

                piece.position = dest_coord
                if self.check_check() == True:
                    piece.position = str_coord
                    self.board_pieces = list(self.previous_board_state)
                    return False

                if isinstance(piece, pieces.Pawn):
                    # En passant
                    if abs(row_distance) == 2:
                        move_direction = 1 if piece.color == "W" else -1
                        self.en_passant = (dest_coord[0] + move_direction, dest_coord[1])
                    # Promotion
                    if dest_coord[0] == 0 or dest_coord[0] == 7:
                        while True:
                            promote_to = input("Choose what the pawn promote to: ") # One letter
                            if promote_to == "Q" or promote_to == "q":
                                self.board_pieces.append(pieces.Queen(piece.color, dest_coord))
                            elif promote_to == "R" or promote_to == "r":
                                self.board_pieces.append(pieces.Rook(piece.color, dest_coord))
                            elif promote_to == "N" or promote_to == "n":
                                self.board_pieces.append(pieces.Knight(piece.color, dest_coord))
                            elif promote_to == "B" or promote_to == "b":
                                self.board_pieces.append(pieces.Bishop(piece.color, dest_coord))
                            else:
                                print("Invalid input!")
                                continue
                            # Remove the pawn
                            self.board_pieces.remove(piece)
                            break
                    # Disable double move
                    piece.first_move = False

                # Set en passant back to "-" if it wasn't set up this turn
                if self.en_passant == en_passant_check:
                    self.en_passant = "-"
                self.turn = "B" if self.turn == "W" else "W"
                self.previous_board_state = list(self.board_pieces)
                return True
        return False

    def check_check(self):
        for piece in self.board_pieces:
            if isinstance(piece, pieces.King) and piece.color == self.turn:
                coords = piece.position
                break

        for piece in self.board_pieces:
            row_distance, col_distance = piece.coord_distance(coords)
            # Each if clauses check the legality of the move
            if piece.movement(row_distance, col_distance) == False:
                continue
            if piece.obstacle_check(row_distance, col_distance, self) == False and isinstance(piece, pieces.Knight) == False:
                continue
            if piece.destination_check(coords, self) == False:
                continue

            return True
        return False