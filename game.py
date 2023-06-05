import components.board as Board
from components.input_converter import input_converter
import components.pieces as Pieces

board = Board.generate()
Board.display(board)

move = " "
while move != "":
    move = input("Move piece: ") # Start coord and end coord like E1E7
    start_coord = input_converter(move[:2])
    x1, y1 = start_coord
    end_coord = input_converter(move[2:])
    x2, y2 = end_coord

    if board[x1][y1] == "R" or board[x1][y1] == "r":
        move_check = Pieces.rook(start_coord, end_coord)
        if move_check == True:
            board[x2][y2] = board[x1][y1]
            board[x1][y1] = "o"
    
    Board.display(board)