import components.board as board
from components.game import Chess
from components.input_converter import input_converter

game = Chess()
board.display(game.board_pieces)

while True:
    turn = "White" if game.turn == "W" else "Black"
    move = input(f"{turn}'s turn to move: ") # Start coord and end coord like E1E7
    str_coord = input_converter(move[:2])
    dest_coord = input_converter(move[2:])
    if str_coord == ValueError or dest_coord == ValueError:
        print("Invalid input!")
        continue

    game_move = game.move(str_coord, dest_coord)

    if game_move == True:
        board.display(game.board_pieces)
    elif game_move == "checkmate":
        if game.turn == "B":
            print("White wins!")
        else:
            print("Black wins!")
        break
    else:
        print(f"Invalid move! Explaination: {game_move}")
        board.display(game.board_pieces)