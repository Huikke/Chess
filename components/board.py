from components.input_converter import coordinate_converter

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
        for square in row:
            row_display += " " + square + " "
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
        for square in row:
            row_display += " " + square + " "
        row_display += str(coord_num)
        coord_num += 1
        if coord_num != 8:
            row_display += "\n"
        
    print(row_display)

    # Prints letter on top of the board
    print("  0  1  2  3  4  5  6  7")


def fen(game):
    # Generate an empty board
    board = []
    for i in range(8):
        board.append([])
        for _ in range(8):
            board[i].append("o")

    # Put pieces on the board
    for piece in game.board_pieces:
        row, col = piece.position
        board[row][col] = str(piece)
    
    # Create FEN from the board
    fen_str = ""
    # Board pieces
    loop = 0
    for row in board:
        loop += 1
        fen_number = 0
        for square in row:
            if square == "o":
                fen_number += 1
            else:
                if fen_number != 0:
                    fen_str += str(fen_number)
                    fen_number = 0
                fen_str += square
        if fen_number != 0:
            fen_str += str(fen_number)
        if loop != 8:
            fen_str += "/"
    # Turn
    fen_str += " " + game.turn
    # Castling rights
    castling = "".join(game.castling)
    fen_str += " " + (castling if castling != "" else "-")
    # Possible en passant targets
    en_passant = game.en_passant if game.en_passant == "-" else coordinate_converter(game.en_passant)
    fen_str += " " + en_passant
    # Halfmove clock and fullmove counter
    fen_str += " " + str(game.halfmove_clock)
    fen_str += " " + str(game.fullmove_number)

    print(fen_str)