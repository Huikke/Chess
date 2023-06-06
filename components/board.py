import components.pieces as pieces

def generate():
    board = []
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append("o")

    board[0][0] = pieces.Rook("B", (0, 0))
    board[0][7] = pieces.Rook("B", (0, 7))
    board[7][0] = pieces.Rook("W", (7, 0))
    board[7][7] = pieces.Rook("W", (7, 7))
    
    return board


def display(board):
    # Prints letter on top of the board
    print("  A  B  C  D  E  F  G  H")

    # Prints numbers on the side of the board
    # There is two spaces between every piece
    coord_num = 8
    row_display = ""
    for row in board:
        row_display += str(coord_num)
        for tile in row:
            row_display += " " + str(tile) + " "
        row_display += str(coord_num)
        coord_num -= 1
        if coord_num != 0:
            row_display += "\n"
        
    print(row_display)

    # Prints letter on top of the board
    print("  A  B  C  D  E  F  G  H")