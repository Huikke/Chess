import components.board as board
from components.game import Chess
from components.input_converter import input_converter

game = Chess()
board.display(game.board_pieces)

while True:
    turn = "White" if game.turn == "w" else "Black"
    move = input(f"{turn}'s turn to move: ") # Start coord and end coord like E1E7
    str_coord = input_converter(move[:2])
    dest_coord = input_converter(move[2:])
    if str_coord == ValueError or dest_coord == ValueError:
        print("Invalid input!")
        continue

    # Fifth character tells which piece Pawn promotes to
    promotion = False
    if len(move) >= 5:
        promotion = move[4]

    game_move = game.move(str_coord, dest_coord, promotion)

    if game_move == True:
        board.display(game.board_pieces)
        print(board.game_to_fen(game))
    elif game_move == "checkmate":
        board.display(game.board_pieces)
        if game.turn == "b":
            print("White wins!")
        else:
            print("Black wins!")
        break
    elif game_move == "draw":
        board.display(game.board_pieces)
        print("Draw!")
        break
    else:
        print(f"Invalid move! Explaination: {game_move}")