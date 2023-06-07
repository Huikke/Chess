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

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "R"

    def movement(self, coord):
        if self.position[0] == coord[0] or self.position[1] == coord[1]:
            self.position = coord
            return True
        else:
            return False

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "B"

    def movement(self, coord):
        row_distance = abs(coord[0] - self.position[0])
        col_distance = abs(coord[1] - self.position[1])
        
        if row_distance == col_distance:
            self.position = coord
            return True
        else:
            return False

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "Q"

    def movement(self, coord):
        row_distance = abs(coord[0] - self.position[0])
        col_distance = abs(coord[1] - self.position[1])
        
        if self.position[0] == coord[0] or self.position[1] == coord[1] or row_distance == col_distance:
            self.position = coord
            return True
        else:
            return False

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "N"

    def movement(self, coord):
        row_distance = abs(coord[0] - self.position[0])
        col_distance = abs(coord[1] - self.position[1])
        
        if row_distance == 2 and col_distance == 1 or row_distance == 1 and col_distance == 2:
            self.position = coord
            return True
        else:
            return False

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "K"

    def movement(self, coord):
        row_distance = abs(coord[0] - self.position[0])
        col_distance = abs(coord[1] - self.position[1])
        
        if row_distance <= 1 and col_distance <= 1:
            self.position = coord
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
    def movement(self, coord):
        row_movement = coord[0] - self.position[0]
        move_distance = 1
        if self.first_move:
            move_distance = 2
            self.first_move = False

        if self.color == "W":
            if row_movement > 0:
                return False
        elif self.color == "B":
            if row_movement < 0:
                return False

        if self.position[1] == coord[1] and abs(row_movement) <= move_distance:
            self.position = coord
            return True
        else:
            return False