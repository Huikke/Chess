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

    # def validity_check(self, ):


class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "R"

    def movement(self, destination):
        row_distance, col_distance = self.coord_distance(destination)
        
        if row_distance == 0 or col_distance == 0:
            self.position = destination
            return True
        else:
            return False

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "B"

    def movement(self, destination):
        row_distance, col_distance = self.coord_distance(destination)
        
        if abs(row_distance) == abs(col_distance):
            self.position = destination
            return True
        else:
            return False

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "Q"

    def movement(self, destination):
        row_distance, col_distance = self.coord_distance(destination)
        
        if row_distance == 0 or col_distance == 0 or abs(row_distance) == abs(col_distance):
            self.position = destination
            return True
        else:
            return False

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "N"

    def movement(self, destination):
        row_distance, col_distance = self.coord_distance(destination)
        
        if abs(row_distance) == 2 and abs(col_distance) == 1 or abs(row_distance) == 1 and abs(col_distance) == 2:
            self.position = destination
            return True
        else:
            return False

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.letter = "K"

    def movement(self, destination):
        row_distance, col_distance = self.coord_distance(destination)
        
        if abs(row_distance) <= 1 and abs(col_distance) <= 1:
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
    def movement(self, destination):
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
            self.position = destination
            self.first_move = False
            return True
        else:
            return False