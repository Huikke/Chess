import components.board as board
from components.input_converter import input_converter
import components.pieces as pieces

board_state = board.generate()
board.display(board_state)

move = " "
while move != "":
    move = input("Move piece: ") # Start coord and end coord like E1E7
    start_coord = input_converter(move[:2])
    x1, y1 = start_coord
    end_coord = input_converter(move[2:])
    x2, y2 = end_coord

    if board_state[x1][y1] != "o":
        move_check = board_state[x1][y1].movement(end_coord)
        if move_check == True:
            board_state[x2][y2] = board_state[x1][y1]
            board_state[x1][y1] = "o"
    
    board.display(board_state)