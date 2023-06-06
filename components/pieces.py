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
        return False