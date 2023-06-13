import components.pieces as pieces

class Chess():
    @staticmethod
    def starting_board():
        board = []
        board.append(pieces.King("W", (7, 4)))
        board.append(pieces.King("B", (0, 4)))
        board.append(pieces.Queen("W", (7, 3)))
        board.append(pieces.Queen("B", (0, 3)))
        board.append(pieces.Rook("W", (7, 0)))
        board.append(pieces.Rook("W", (7, 7)))
        board.append(pieces.Rook("B", (0, 0)))
        board.append(pieces.Rook("B", (0, 7)))
        board.append(pieces.Bishop("W", (7, 2)))
        board.append(pieces.Bishop("W", (7, 5)))
        board.append(pieces.Bishop("B", (0, 2)))
        board.append(pieces.Bishop("B", (0, 5)))
        board.append(pieces.Knight("W", (7, 1)))
        board.append(pieces.Knight("W", (7, 6)))
        board.append(pieces.Knight("B", (0, 1)))
        board.append(pieces.Knight("B", (0, 6)))
        for i in range(8):
            board.append(pieces.Pawn("W", (6, i)))
            board.append(pieces.Pawn("B", (1, i)))
        return board

    def __init__(self):
        self.board_pieces = self.starting_board()
        self.turn = "W" #TODO
        self.castling = ["K", "Q", "k", "q"] #TODO
        self.en_passant = "-"
        self.halfmove_clock = 0 #TODO
        self.fullmove_counter = 1 #TODO

    def state(self):
        return self.board_pieces

    def move(self, str_coord, dest_coord, testing=False):
        en_passant_check = self.en_passant

        for piece in self.board_pieces:
            if piece.position == str_coord:
                row_distance, col_distance = piece.coord_distance(dest_coord)
                # Each if clauses check the legality of the move
                if piece.movement(row_distance, col_distance) == False:
                    return False
                if piece.obstacle_check(row_distance, col_distance, self) == False and isinstance(piece, pieces.Knight) == False:
                    return False
                destination_check = piece.destination_check(dest_coord, self)
                # Returns False when move isn't legal
                if destination_check == False:
                    return False
                # Returns None when move is legal, but no pieces are captured
                elif destination_check == None:
                    pass
                # Else returns captured piece stored in destination_check
                else:
                    self.board_pieces.remove(destination_check)
                piece.position = dest_coord
                # If check is True, undo the all changes made so far and return
                if self.check_check() == True:
                    piece.position = str_coord
                    if destination_check != None:
                        self.board_pieces.append(destination_check)
                    return "Check"

                if testing == False:
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

                    # Checks whether the game has ended
                    if self.check_check() == True:
                        if self.checkmate_check() == True:
                            print("Checkmate!")
                            return "checkmate"
                        else:
                            print("Check!")
                else: # Revert the changes
                    piece.position = str_coord
                    if destination_check != None:
                        self.board_pieces.append(destination_check)

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
    
    def checkmate_check(self):
        for piece in self.board_pieces:
            if piece.color == self.turn:
                for x in range(8):
                    for y in range(8):
                        if self.move(piece.position, (x, y), True) == True:
                            return False
        return True