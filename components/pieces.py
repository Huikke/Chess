class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.letter = "?" # Gets replaced in subclass

    def __str__(self):
        if self.color == "W":
            return self.letter
        if self.color == "B":
            return self.letter.lower()

    def coord_distance(self, destination):
        row_distance = destination[0] - self.position[0]
        col_distance = destination[1] - self.position[1]
        return row_distance, col_distance

    # Checks whether there is obstacles in piece's path
    def obstacle_check(self, row, col, board_pieces):
        for i in range(1, 8):
            current_row = row - i if row > 0 else row + i if row < 0 else row
            current_col = col - i if col > 0 else col + i if col < 0 else col
            check_position = ((self.position[0] + current_row), (self.position[1] + current_col))

            if current_row == 0 and current_col == 0:
                return True
            for piece in board_pieces:
                if piece.position == check_position:
                    return False

    # Checks whether destination can be moved into
    def destination_check(self, destination, board_pieces):
        for piece in board_pieces:
            if piece.position == destination:
                # Doesn't capture ally piece
                if self.color == piece.color:
                    return False
                # Do capture enemy piece
                elif self.color == "W" and piece.color == "B" or self.color == "B" and piece.color == "W":
                    # Pawn doesn't capture if capturing is not on
                    if isinstance(self, Pawn) and self.capturing == False:
                        return False
                    # Removes eaten piece from the game
                    board_pieces.remove(piece)
                    return True
        # Pawn doesn't move to empty position, it is capturing
        if isinstance(self, Pawn) and self.capturing == True:
            return False
        return True


class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "R"

    def movement(self, destination, board_pieces):
        row_distance, col_distance = self.coord_distance(destination)

        if row_distance == 0 or col_distance == 0:
            if self.obstacle_check(row_distance, col_distance, board_pieces) == False:
                return False
            if self.destination_check(destination, board_pieces) == False:
                return False
            self.position = destination
            return True
        else:
            return False

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "B"

    def movement(self, destination, board_pieces):
        row_distance, col_distance = self.coord_distance(destination)

        if abs(row_distance) == abs(col_distance):
            if self.obstacle_check(row_distance, col_distance, board_pieces) == False:
                return False
            if self.destination_check(destination, board_pieces) == False:
                return False
            self.position = destination
            return True
        else:
            return False

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "Q"

    def movement(self, destination, board_pieces):
        row_distance, col_distance = self.coord_distance(destination)

        if row_distance == 0 or col_distance == 0 or abs(row_distance) == abs(col_distance):
            if self.obstacle_check(row_distance, col_distance, board_pieces) == False:
                return False
            if self.destination_check(destination, board_pieces) == False:
                return False
            self.position = destination
            return True
        else:
            return False

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "N"

    def movement(self, destination, board_pieces):
        row_distance, col_distance = self.coord_distance(destination)

        if abs(row_distance) == 2 and abs(col_distance) == 1 or abs(row_distance) == 1 and abs(col_distance) == 2:
            if self.destination_check(destination, board_pieces) == False:
                return False
            self.position = destination
            return True
        else:
            return False

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "K"

    def movement(self, destination, board_pieces):
        row_distance, col_distance = self.coord_distance(destination)

        if abs(row_distance) <= 1 and abs(col_distance) <= 1:
            if self.destination_check(destination, board_pieces) == False:
                return False
            self.position = destination
            return True
        else:
            return False

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "P"
        self.first_move = True
        self.capturing = False

    # TODO:
    # promotion
    # en passant
    def movement(self, destination, board_pieces):
        self.capturing = False
        row_distance, col_distance = self.coord_distance(destination)
        move_distance = 1
        if self.first_move:
            move_distance = 2

        if self.color == "W":
            if row_distance > 0:
                return False
        elif self.color == "B":
            if row_distance < 0:
                return False

        if abs(col_distance) <= 1 and abs(row_distance) <= move_distance:
            # If pawn moves diagonally
            if abs(row_distance) == 1 and abs(col_distance) == 1:
                self.capturing = True
            if abs(row_distance) != 1 and abs(col_distance) == 1:
                return False

            if self.obstacle_check(row_distance, col_distance, board_pieces) == False:
                return False
            if self.destination_check(destination, board_pieces) == False:
                return False
            self.position = destination
            self.first_move = False
            return True
        else:
            return False