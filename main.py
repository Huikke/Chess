import components.board as board
from components.game import Chess
from components.input_converter import input_converter

game = Chess()
board.display(game.board_pieces)

while True:
    move = input("Move piece: ") # Start coord and end coord like E1E7
    str_coord = input_converter(move[:2])
    dest_coord = input_converter(move[2:])
    if str_coord == ValueError or dest_coord == ValueError:
        print("Invalid input!")
        continue

    game_move = game.move(str_coord, dest_coord)

    if game_move == True:
        board.display(game.board_pieces)
    else:
        print("Invalid move!")