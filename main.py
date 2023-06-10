import components.board as board
from components.input_converter import input_converter
from components.game import game_turn

board_state = board.generate()
board.display(board_state)

while True:
    move = input("Move piece: ") # Start coord and end coord like E1E7
    str_coord = input_converter(move[:2])
    dest_coord = input_converter(move[2:])
    if str_coord == ValueError or dest_coord == ValueError:
        print("Invalid input!")
        continue

    game_move = game_turn(board_state, str_coord, dest_coord)

    if game_move == True:
        board.display(board_state)
    else:
        print("Invalid move!")