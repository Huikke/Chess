from components.print_board import print_board
from components.input_converter import input_converter

board = []
for i in range(8):
    board.append([])
    for j in range(8):
        board[i].append("o")


piece = input("Choose a piece: ")
move = input("Place a piece: ")

row, col = input_converter(move)

board[row][col] = piece

print_board(board)