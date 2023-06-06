class Rook:
    def __init__(self, color, position):
        if color == "W":
            self.color = "R"
        elif color == "B":
            self.color = "r"
        self.position = position

    def movement(self, coord):
        if self.position[0] == coord[0] or self.position[1] == coord[1]:
            self.position = coord
            return True
        return False