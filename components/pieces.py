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

    def obstacle_check(self, row, col, board):
        # Pawn destination check
        x = self.position[0] + row
        y = self.position[1] + col
        if board[x][y] != "o" and isinstance(self, Pawn):
            return False

        for i in range(1, 8):
            current_row = row - i if row > 0 else row + i if row < 0 else row
            current_col = col - i if col > 0 else col + i if col < 0 else col
            x = self.position[0] + current_row
            y = self.position[1] + current_col

            if current_row == 0 and current_col == 0:
                return True
            if board[x][y] != "o":
                return False

    def destination_check(self, coord, board):
        d_tile = board[coord[0]][coord[1]]

        if d_tile == "o":
            return True
        elif self.color == d_tile.color:
            return False
        else:
            return True
            

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "R"

    def movement(self, destination, board):
        row_distance, col_distance = self.coord_distance(destination)

        if row_distance == 0 or col_distance == 0:
            if self.obstacle_check(row_distance, col_distance, board) == False:
                return False
            if self.destination_check(destination, board) == False:
                return False
            self.position = destination
            return True
        else:
            return False

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "B"

    def movement(self, destination, board):
        row_distance, col_distance = self.coord_distance(destination)

        if abs(row_distance) == abs(col_distance):
            if self.obstacle_check(row_distance, col_distance, board) == False:
                return False
            if self.destination_check(destination, board) == False:
                return False
            self.position = destination
            return True
        else:
            return False

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "Q"

    def movement(self, destination, board):
        row_distance, col_distance = self.coord_distance(destination)

        if row_distance == 0 or col_distance == 0 or abs(row_distance) == abs(col_distance):
            if self.obstacle_check(row_distance, col_distance, board) == False:
                return False
            if self.destination_check(destination, board) == False:
                return False
            self.position = destination
            return True
        else:
            return False

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "N"

    def movement(self, destination, board):
        row_distance, col_distance = self.coord_distance(destination)

        if abs(row_distance) == 2 and abs(col_distance) == 1 or abs(row_distance) == 1 and abs(col_distance) == 2:
            if self.destination_check(destination, board) == False:
                return False
            self.position = destination
            return True
        else:
            return False

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "K"

    def movement(self, destination, board):
        row_distance, col_distance = self.coord_distance(destination)

        if abs(row_distance) <= 1 and abs(col_distance) <= 1:
            if self.destination_check(destination, board) == False:
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

    # TODO:
    # capturing
    # promotion
    # en passant
    def movement(self, destination, board):
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

        if col_distance == 0 and abs(row_distance) <= move_distance:
            if self.obstacle_check(row_distance, col_distance, board) == False:
                return False
            if self.destination_check(destination, board) == False:
                return False
            self.position = destination
            self.first_move = False
            return True
        else:
            return False