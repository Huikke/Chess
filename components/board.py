def display(board_pieces):
    # Generate an empty board
    board = []
    for i in range(8):
        board.append([])
        for _ in range(8):
            board[i].append("o")

    # Put pieces on the board
    for piece in board_pieces:
        row, col = piece.position
        board[row][col] = str(piece)

    # Prints letter on top of the board
    print("  A  B  C  D  E  F  G  H")

    # Prints numbers on the side of the board
    # There is two spaces between every piece
    coord_num = 8
    row_display = ""
    for row in board:
        row_display += str(coord_num)
        for tile in row:
            row_display += " " + tile + " "
        row_display += str(coord_num)
        coord_num -= 1
        if coord_num != 0:
            row_display += "\n"
        
    print(row_display)

    # Prints letter on top of the board
    print("  A  B  C  D  E  F  G  H")


# Shows Python coordinates instead of chess system
def dev_display(board_pieces):
    # Generate an empty board
    board = []
    for i in range(8):
        board.append([])
        for _ in range(8):
            board[i].append("o")

    # Put pieces on the board
    for piece in board_pieces:
        row, col = piece.position
        board[row][col] = str(piece)

    # Prints letter on top of the board
    print("  0  1  2  3  4  5  6  7")

    # Prints numbers on the side of the board
    # There is two spaces between every piece
    coord_num = 0
    row_display = ""
    for row in board:
        row_display += str(coord_num)
        for tile in row:
            row_display += " " + tile + " "
        row_display += str(coord_num)
        coord_num += 1
        if coord_num != 8:
            row_display += "\n"
        
    print(row_display)

    # Prints letter on top of the board
    print("  0  1  2  3  4  5  6  7")