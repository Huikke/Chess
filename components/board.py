import components.pieces as pieces

def generate():
    board = []
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append("o")

    board[0][0] = pieces.Rook("B", (0, 0))
    board[0][1] = pieces.Knight("B", (0, 1))
    board[0][2] = pieces.Bishop("B", (0, 2))
    board[0][3] = pieces.King("B", (0, 3))
    board[0][4] = pieces.Queen("B", (0, 4))
    board[0][5] = pieces.Bishop("B", (0, 5))
    board[0][6] = pieces.Knight("B", (0, 6))
    board[0][7] = pieces.Rook("B", (0, 7))

    board[7][0] = pieces.Rook("W", (7, 0))
    board[7][1] = pieces.Knight("W", (7, 1))
    board[7][2] = pieces.Bishop("W", (7, 2))
    board[7][3] = pieces.Queen("W", (7, 3))
    board[7][4] = pieces.King("W", (7, 4))
    board[7][5] = pieces.Bishop("W", (7, 5))
    board[7][6] = pieces.Knight("W", (7, 6))
    board[7][7] = pieces.Rook("W", (7, 7))

    for i in range(8):
        board[1][i] = pieces.Pawn("B", (1, i))
        board[6][i] = pieces.Pawn("W", (6, i))
    
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


# Shows Python coordinates instead of chess system
def dev_display(board):
    # Prints letter on top of the board
    print("  0  1  2  3  4  5  6  7")

    # Prints numbers on the side of the board
    # There is two spaces between every piece
    coord_num = 0
    row_display = ""
    for row in board:
        row_display += str(coord_num)
        for tile in row:
            row_display += " " + str(tile) + " "
        row_display += str(coord_num)
        coord_num += 1
        if coord_num != 8:
            row_display += "\n"
        
    print(row_display)

    # Prints letter on top of the board
    print("  0  1  2  3  4  5  6  7")