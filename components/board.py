def generate():
    board = []
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append("o")

    board[0][0] = "r"
    board[0][7] = "r"
    board[7][0] = "R"
    board[7][7] = "R"
    
    return board


def display(board):
    # Prints letter on top of the board
    print("  A  B  C  D  E  F  G  H")
    
    coord_num = 8
    # Prints numbers on the side of the board
    # There is two spaces between every piece
    for row in board:
        print(coord_num, row[0], "",row[1], "",row[2], "",row[3], "",row[4], 
              "",row[5], "",row[6], "", row[7], coord_num)
        coord_num -= 1

    # Prints letter on top of the board
    print("  A  B  C  D  E  F  G  H")