import components.board as board
from components.game import Chess
from components.input_converter import input_converter

while True:
    start = input("New game ("") or load FEN?: ")
    if start == "":
        game = Chess()
        break
    else:
        try:
            game = board.fen_to_game(start)
            break
        except:
            print("Invalid FEN")

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

    move_result, move_message = game.move(str_coord, dest_coord, promotion)

    if move_result == True:
        board.display(game.board_pieces)
        print(board.game_to_fen(game))
        if move_message == "Checkmate":
            if game.turn == "b":
                print("Checkmate!\nWhite wins!")
            else:
                print("Checkmate!\nBlack wins!")
            break
        elif move_message == "Stalemate":
            print("Draw!\nStalemate")
            break
        elif move_message == "Insufficient material":
            print("Draw!\nInsufficient material")
            break
        elif move_message == "Halfmove clock is full":
            print("Draw!\nHalfmove clock is full")
            break
    else:
        print(f"Invalid move!\nExplaination: {move_message}")