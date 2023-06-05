from components.print_board import print_board
from components.input_converter import input_converter
import components.pieces as pieces

board = []
for i in range(8):
    board.append([])
    for j in range(8):
        board[i].append("o")

board[3][4] = "R"
print_board(board)

move = " "
while move != "":
    move = input("Move piece: ") # Start coord and end coord like E1E7
    start_coord = input_converter(move[:2])
    x1, y1 = start_coord
    end_coord = input_converter(move[2:])
    x2, y2 = end_coord

    if board[x1][y1] == "R":
        move_check = pieces.rook(start_coord, end_coord)
        if move_check == True:
            board[x2][y2] = board[x1][y1]
            board[x1][y1] = "o"

    print_board(board)