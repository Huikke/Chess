class Rook:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def movement(self, coord):
        if self.position[0] == coord[0] or self.position[1] == coord[1]:
            self.position = coord
            return True
        return False

    def __str__(self):
        if self.color == "W":
            return "R"
        if self.color == "B":
            return "r"